#!/usr/bin/env python3
"""
Void Scribe: a minimal console text editor that conceals all input and saves your hidden notes upon interruption.
Perfect for public writing where prying eyes must see nothing.
"""
import sys
import termios
from datetime import datetime


def save_inscription(content):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"scripture_{timestamp}.txt"
    try:
        with open(filename, 'w') as f:
            f.write(content)
        # After terminal restoration, reveal save status
        print(f"\n[Enscribed {len(content)} characters into '{filename}']")
    except Exception as e:
        print(f"\n[Error during inscription: {e}]")


def main():
    fd = sys.stdin.fileno()

    # Preserve the original terminal incantation
    original = termios.tcgetattr(fd)
    occult = termios.tcgetattr(fd)

    # Invoke the silence ritual: disable echo
    occult[3] &= ~termios.ECHO
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
        # Ritual interrupted: proceed to inscription
        pass
    finally:
        # Restore original terminal echo
        termios.tcsetattr(fd, termios.TCSADRAIN, original)
        save_inscription(''.join(incantation))


if __name__ == '__main__':
    main()

