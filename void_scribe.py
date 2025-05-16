#!/usr/bin/env python3
"""
Void Scribe: a minimal console text editor that conceals all input and saves your hidden notes upon interruption.
Enhanced with optional encryption, remote sending, and local deletion.
Perfect for public writing where prying eyes must see nothing.
"""

import sys
import termios
import argparse
import getpass
import subprocess
from datetime import datetime
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

def save_inscription(content, filename):
    try:
        with open(filename, 'wb') as f:
            f.write(content)
        print(f"\n[Enscribed {len(content)} bytes into '{filename}']")
        return True
    except Exception as e:
        print(f"\n[Error during inscription: {e}]")
        return False

def encrypt_content(content: bytes, password: str) -> bytes:
    # AES-GCM encryption
    # Derive key from password (simple, for demo; consider stronger KDF in production)
    from hashlib import sha256
    key = sha256(password.encode()).digest()  # 32 bytes key for AES-256

    aesgcm = AESGCM(key)
    nonce = os.urandom(12)  # 96-bit nonce for AESGCM

    encrypted = aesgcm.encrypt(nonce, content, None)
    # Store nonce + ciphertext together
    return nonce + encrypted

def prompt_password(confirm=False):
    while True:
        pwd = getpass.getpass("Enter password: ")
        if not pwd:
            print("Password cannot be empty.")
            continue
        if confirm:
            pwd2 = getpass.getpass("Confirm password: ")
            if pwd != pwd2:
                print("Passwords do not match. Try again.")
                continue
        return pwd

def send_to_remote(filename, server, remote_path, verbose=False):
    # Using scp for simplicity (requires ssh keys or password)
    # If password needed, user must have sshpass or similar, which is not secure.
    # Here we just call scp and let user enter password interactively if needed.
    remote_target = f"{server}:{remote_path}"
    cmd = ['scp', filename, remote_target]
    if verbose:
        print(f"[Sending '{filename}' to remote server '{server}' at '{remote_path}']")
    try:
        subprocess.run(cmd, check=True)
        if verbose:
            print("[Remote send successful]")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[Error sending file to remote server: {e}]")
        return False

def main():
    parser = argparse.ArgumentParser(description="Void Scribe: Concealed text editor with optional encryption and remote sending.")
    parser.add_argument('--encrypt', action='store_true', help="Encrypt the content before saving.")
    parser.add_argument('--send', action='store_true', help="Send the saved file to a remote server via SCP.")
    parser.add_argument('--delete-local', action='store_true', help="Delete the local file after saving (and sending if enabled).")
    parser.add_argument('--server', type=str, help="Remote server address for sending (required if --send).")
    parser.add_argument('--remote-path', type=str, default='~/', help="Remote path on server to save the file (default: home directory).")
    parser.add_argument('--verbose', action='store_true', help="Enable verbose output.")
    args = parser.parse_args()

    if args.send and not args.server:
        print("Error: --server must be specified if --send is used.")
        sys.exit(1)

    fd = sys.stdin.fileno()
    original = termios.tcgetattr(fd)
    occult = termios.tcgetattr(fd)
    occult[3] &= ~termios.ECHO  # Disable echo

    termios.tcsetattr(fd, termios.TCSADRAIN, occult)

    incantation = []
    print("[==> Entering Void Scribe: your keystrokes are unseen, interrupt with Ctrl+C to inscribe your scripture <==]")

    try:
        while True:
            line = sys.stdin.readline()
            if not line:
                break
            incantation.append(line)
    except KeyboardInterrupt:
        # Interrupted, proceed to inscription
        pass
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, original)

    content_str = ''.join(incantation)
    content_bytes = content_str.encode('utf-8')

    # Encryption step
    if args.encrypt:
        if args.verbose:
            print("[Encryption enabled]")
        password = prompt_password(confirm=True)
        content_bytes = encrypt_content(content_bytes, password)
        if args.verbose:
            print("[Content encrypted]")

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    suffix = '.enc' if args.encrypt else '.txt'
    filename = f"scripture_{timestamp}{suffix}"

    saved = save_inscription(content_bytes, filename)

    # Remote send step
    if saved and args.send:
        if args.verbose:
            print("[Sending to remote server]")
        success = send_to_remote(filename, args.server, args.remote_path, verbose=args.verbose)
        if not success:
            print("[Warning] Remote send failed.")

    # Delete local file if requested
    if saved and args.delete_local:
        try:
            os.remove(filename)
            if args.verbose:
                print(f"[Local file '{filename}' deleted]")
        except Exception as e:
            print(f"[Error deleting local file: {e}]")

if __name__ == '__main__':
    main()

