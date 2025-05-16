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

---

# Keep Your Secrets Yours



