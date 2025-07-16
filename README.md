# File Decryption & Encryption Tool

A simple application for encrypting and decrypting files using password-based symmetric encryption (Fernet/AES).

Now available as both a **desktop GUI (PyQt5)** and a **web app (Streamlit)** for browser-based use.  
This project is available on Hackr.io  
[File Encrytion Tool](https://hackr.io/blog/how-to-create-a-python-file-encryption-tool?source=k8mepg2dMy)

## Features
- **Encrypt any file** with a password
- **Decrypt encrypted files** with the same password
- Simple, modern GUI (PyQt5) or web interface (Streamlit)
- Cross-platform (Windows, macOS, Linux)

## Screenshots
![App Screenshot](screenshot.png) <!-- Add a screenshot if available -->

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/QMS85/FileEncryptionTool.git
cd FileEncryptionTool
```

### 2. Set up a Python environment (optional but recommended)
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```
If `requirements.txt` is not present, install manually:
```bash
pip install pyqt5 cryptography streamlit
```

## Usage

### Option 1: Run the Web App (Recommended for Codespaces or Browser Use)
```bash
streamlit run web_app.py
```
- Open the provided local URL in your browser (or use the "Open in Browser" button in Codespaces Ports tab).
- Upload a file, enter a password, and choose to encrypt or decrypt.

### Option 2: Run the Desktop GUI (PyQt5)
```bash
python app.py
```
- Only works on local machines with a desktop environment.
- Not supported in Codespaces browser.

## How to use
1. **Open the app** (web or desktop).
2. **Enter a password** in the input field.
3. **Select a file** to encrypt or decrypt.
4. Click **Encrypt file** or **Decrypt file** as needed.
5. Encrypted files will have a `.enc` extension. Decrypted files will be saved without `.enc`.

## Notes for Codespaces and Remote Environments
- **Streamlit web app is recommended** for Codespaces and browser-based use.
- **PyQt5 desktop GUI** requires a local desktop environment.

## Security Notice
- This tool uses password-based encryption with Fernet (AES-128 in CBC mode with HMAC).
- **Never lose your password!** Files cannot be decrypted without it.
- For sensitive or production use, review the code and cryptography practices.

## License
MIT License

## Author
Jonathan Peters
