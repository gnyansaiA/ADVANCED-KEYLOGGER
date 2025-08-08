# Advanced Keylogger

A Python-based keylogger and system information collector for Windows. This project captures keystrokes, clipboard data, audio recordings, screenshots, and system information, then encrypts the collected data for secure storage or transfer.

---

## Features

- **Keystroke Logging:** Records all keystrokes to a log file.
- **Clipboard Capture:** Saves clipboard contents.
- **Audio Recording:** Records audio from the microphone for a set duration.
- **Screenshot Capture:** Takes screenshots at intervals.
- **System Information:** Collects details like hostname, IP addresses, OS, and hardware info.
- **Encryption:** Encrypts all collected data using Fernet symmetric encryption.
- **Extensible Output:** Data can be sent via email, uploaded to cloud storage, or stored in a database (not implemented yet finding a better and more efficient tool or technique to extract.).

---

## Requirements

- Python 3.7+
- Windows OS

### Python Libraries

Install all dependencies with:

```sh
pip install pynput pycryptodome cryptography sounddevice scipy pillow requests pymongo pywin32
```

---

## Usage

1. **Clone the repository** and navigate to the project directory.

2. **Configure settings**  
   Edit `keylogger.py` to set file paths, encryption keys, and other parameters as needed.

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

---

## Encryption & Decryption

- **Key Generation:**  
  Use `cryptography/Keygen.py` to generate a new Fernet key.

- **Decryption:**  
  Use `cryptography/decrypter.py` to decrypt the encrypted files.

---

## Extending Data Retrieval

NOTE: Data retrieval (exfiltration) is not implemented in this version. Still looking for an efficient and functioning tool or technique to securely and reliably retrieve the collected and encrypted data.

---

## Disclaimer

This project is for **educational purposes only**.  
Do not use it to monitor devices or accounts without explicit permission.  
The author is not responsible for any misuse.

---
