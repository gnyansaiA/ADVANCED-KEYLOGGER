from cryptography.fernet import Fernet

key = Fernet.generate_key()
file = open("encryption_key_file", "wb")
file.write(key)
file.close()