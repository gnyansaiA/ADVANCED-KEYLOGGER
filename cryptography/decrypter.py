from cryptography.fernet import Fernet

key = "7-2oBjGOW2nwL573jvPWQ9w9bcaVR6UA5BZlBqHWX0Q="

key_info_e = "key_log_encrypted.txt"
system_info_e = "sys_info_encrypted.txt"   
clipboard_info_e = "clipboard_encrypted.txt"

encrypted_files = [key_info_e, system_info_e, clipboard_info_e]
count = 0

for decrypting_file in encrypted_files:
    with open(encrypted_files[count], "rb") as f:
        data = f.read()
    
    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)

    with open(decrypting_file, "wb") as f:
        f.write(decrypted)

    count += 1  