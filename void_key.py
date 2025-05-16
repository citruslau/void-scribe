#!/usr/bin/env python3

"""
void_key.py — Securely decrypts AES-GCM-encrypted Void Scribe .enc files.
Prompts interactively for password (not passed as command-line argument).
Key derivation: SHA-256 digest of password (must match encryption method).
"""

import argparse
import getpass
import hashlib
import sys
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def decrypt_file(filepath: str, password: str) -> None:
    try:
        with open(filepath, 'rb') as f:
            data = f.read()
    except FileNotFoundError:
        print(f"[Error] File not found: {filepath}")
        sys.exit(1)
    except Exception as e:
        print(f"[Error] Failed to read file: {e}")
        sys.exit(1)

    if len(data) < 13:
        print("[Error] File too short to contain valid AES-GCM ciphertext.")
        sys.exit(1)

    nonce, ciphertext = data[:12], data[12:]
    key = hashlib.sha256(password.encode('utf-8')).digest()
    aesgcm = AESGCM(key)

    try:
        decrypted = aesgcm.decrypt(nonce, ciphertext, None)
    except Exception as e:
        print(f"[Decryption failed] Incorrect password or corrupt ciphertext.\nDetails: {e}")
        sys.exit(1)

    try:
        print("\n==== Decrypted Content ====\n")
        print(decrypted.decode('utf-8'))
    except UnicodeDecodeError:
        print("[Decryption succeeded, but content is not valid UTF-8 text.]")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(
        description="Void Key: Decrypt .enc files created by Void Scribe (AES-GCM with SHA-256 key)."
    )
    parser.add_argument('file', help="Path to the encrypted .enc file")
    args = parser.parse_args()

    password = getpass.getpass("Enter decryption password: ")
    if not password:
        print("[Error] Password cannot be empty.")
        sys.exit(1)

    decrypt_file(args.file, password)

if __name__ == '__main__':
    main()

