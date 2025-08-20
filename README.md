# Advanced Keylogger

A Python-based advanced keylogger and system information collector for Windows.  
This project captures keystrokes, clipboard data, audio recordings, screenshots, and system information, encrypts the collected data, and uploads it to a MongoDB database for secure remote retrieval.

---

## Features

- **Keystroke Logging:** Records all keystrokes to a log file.
- **Clipboard Capture:** Saves clipboard contents.
- **Audio Recording:** Records audio from the microphone for a set duration.
- **Screenshot Capture:** Takes screenshots at intervals.
- **System Information:** Collects details like hostname, IP addresses, OS, and hardware info.
- **Encryption:** Encrypts all collected data using Fernet symmetric encryption.
- **MongoDB Upload:** Encrypted files are uploaded to a remote MongoDB database using GridFS.

---

## Requirements

- Python 3.7+
- Windows OS

### Python Libraries

Install all dependencies with:

```sh
pip install pynput pycryptodome cryptography sounddevice scipy pillow requests pymongo gridfs pywin32
```

---

## Usage

1. **Clone the repository** and navigate to the project directory.

2. **Configure settings**  
   - Edit `project/keylogger.py` to set file paths, encryption keys, and MongoDB URI as needed.

3. **Run the keylogger:**

   ```sh
   python project/keylogger.py
   ```

4. **Collected Data:**  
   - Keystrokes: `project/key_log.txt`
   - System info: `project/sys_info.txt`
   - Clipboard: `project/clipboard.txt`
   - Audio: `project/audio_recording.wav`
   - Screenshot: `project/screenshot.png`
   - Encrypted files: `project/key_log_encrypted.txt`, etc.

5. **MongoDB Storage:**  
   - Encrypted files are uploaded to your MongoDB database using GridFS.
   - You can retrieve them from your MongoDB deployment for decryption and analysis.

---

## Encryption & Decryption

- **Key Generation:**  
  Use `cryptography/Keygen.py` to generate a new Fernet key.

- **Decryption:**  
  Use `cryptography/decrypter.py` to decrypt the encrypted files retrieved from MongoDB.

---

## Data Retrieval

- **Current Method:**  
  Encrypted files are uploaded to a MongoDB database using GridFS.
- **Other Methods:**  
  You can adapt the project to use email, Google Drive, Telegram, FTP/SFTP, or HTTP POST for data retrieval.  
  See code comments for integration ideas.

---

## Disclaimer

This project is for **educational purposes only**.  
Do not use it to monitor devices or accounts without explicit permission.  
The author is not responsible for any misuse.

---

## License

This project is licensed under MIT License.
