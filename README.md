# File Encryption & Decryption Tool

A simple desktop application built with PyQt5 for encrypting and decrypting files using password-based symmetric encryption (Fernet/AES).

## Features
- **Encrypt any file** with a password
- **Decrypt encrypted files** with the same password
- Simple, modern GUI with custom styling
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
pip install pyqt5 cryptography
```

## Usage

### Run the application
```bash
python app.py
```

### How to use
1. **Open the app**: The main window will appear.
2. **Enter a password** in the input field.
3. **Select a file** to encrypt or decrypt.
4. Click **Encrypt file** or **Decrypt file** as needed.
5. Encrypted files will have a `.enc` extension. Decrypted files will be saved without `.enc`.

## Notes for Codespaces and Remote Environments
- **PyQt5 is a desktop GUI framework.** Codespaces and most remote/devcontainer environments do not support GUI apps natively in the browser.
- To use the GUI, run the app on your local machine.
- If you need browser-based encryption, consider converting the app to use a web framework (e.g., Streamlit, Flask).

## Security Notice
- This tool uses password-based encryption with Fernet (AES-128 in CBC mode with HMAC).
- **Never lose your password!** Files cannot be decrypted without it.
- For sensitive or production use, review the code and cryptography practices.

## License
MIT License

## Author
Jonathan Peters
