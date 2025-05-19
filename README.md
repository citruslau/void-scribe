# V̸̭͐͜Ơ̵̢̬̱̫̲͙͙̰̭̹̂͜͝͝I̸̢̨̲̲̖̖͇͙̫̥̼̖̼͔͚̅͂̆͗Ḑ̴̩̤̮̼͈̝̈́ ̵̡̳͖͙̰̹̖̺̣̱͈̣̫́̄̈́̓̃͜ͅS̸̨͍͓̥̳̞̹͎̾̓̀̒̅̉̇͑̏͑̋͝C̵̛̯̲̠͓̑͛̇̉̓̒̔̉͑̉͂̎͐Ȑ̶̙̭͆̒̊͘͜Į̸̛̰̣͕̻̗͈̇̌͛̀̀̑̀̀B̴̢͎̖̮̳̭̠͙͑͗̑̄͂͘ͅḘ̵͕͉̮̥͙̜͍̞͂̊̽̋͒̏́̅͜͝

TYPE INTO THE VOID
---

A Command-line text editor where you type into the void. You see nothing; they see nothing, but you know it's there and will be saved for future reference upong exiting.

<img src="https://github.com/YedTheEmo/void-scribe/blob/main/resource/sample.png" width=100% height=100%>

## Features
- Command-line interface.
- Hidden text
- Option to send to send to a remote SSH server
- Password Protection and Encryption
- Auto deletion of local copy 

## Usage
### Invisible Writing, Encryption, Remote Sending, and Auto-Deletion 
```
 ./void_scribe.py  --help
usage: void_scribe.py [-h] [--encrypt] [--send] [--delete-local]
                      [--server SERVER] [--remote-path REMOTE_PATH]
                      [--verbose]

Void Scribe: Concealed text editor with optional encryption and
remote sending.

options:
  -h, --help            show this help message and exit
  --encrypt             Encrypt the content before saving.
  --send                Send the saved file to a remote server via
                        SCP.
  --delete-local        Delete the local file after saving (and
                        sending if enabled).
  --server SERVER       Remote server address for sending (required
                        if --send).
  --remote-path REMOTE_PATH
                        Remote path on server to save the file
                        (default: home directory).
  --verbose             Enable verbose output.
``` 
### Decryption

```
 ./void_key.py  --help
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

``` 

---

# Keep Your Secrets Yours



