import streamlit as st
import base64
import hashlib
from cryptography.fernet import Fernet

st.set_page_config(page_title="File Encryption & Decryption Tool", layout="centered")
st.title("🔒 File Encryption & Decryption Tool")

st.markdown("""
This web app lets you encrypt or decrypt files using a password. Encrypted files use strong symmetric encryption (Fernet/AES).
""")

def derive_key(password):
    digest = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(digest)

def encrypt_file(file_bytes, password):
    key = derive_key(password)
    cipher = Fernet(key)
    return cipher.encrypt(file_bytes)

def decrypt_file(file_bytes, password):
    key = derive_key(password)
    cipher = Fernet(key)
    return cipher.decrypt(file_bytes)

mode = st.radio("Choose mode:", ("Encrypt", "Decrypt"))
password = st.text_input("Enter password", type="password")
file = st.file_uploader("Select a file", type=None)

if file and password:
    file_bytes = file.read()
    filename = file.name
    if mode == "Encrypt":
        try:
            encrypted = encrypt_file(file_bytes, password)
            st.success("File encrypted successfully!")
            st.download_button("Download Encrypted File", encrypted, file_name=filename+".enc")
        except Exception as e:
            st.error("Encryption failed.")
    else:
        try:
            decrypted = decrypt_file(file_bytes, password)
            out_name = filename.replace(".enc", "")
            st.success("File decrypted successfully!")
            st.download_button("Download Decrypted File", decrypted, file_name=out_name)
        except Exception as e:
            st.error("Decryption failed. Check your password and file.")
else:
    st.info("Please select a file and enter a password.")
