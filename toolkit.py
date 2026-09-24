#!/usr/bin/env python3
import os
import sys
import hashlib

def calculate_sha256(filename):
    """Calculates the SHA-256 hash of a file to check for changes."""
    sha256_hash = hashlib.sha256()
    try:
        with open(filename, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        print(f"[-] Error: The file '{filename}' was not found.")
        return None
    except Exception as e:
        print(f"[-] Error tracking file: {str(e)}")
        return None

def main():
    if len(sys.argv) < 3:
        print("ULK Security Toolkit")
        print("Usage: python3 toolkit.py hash [filename]")
        print("Example: python3 toolkit.py hash risk_assessment.md")
        sys.exit(1)

    action = sys.argv[1].lower()
    target_file = sys.argv[2]

    if action == "hash":
        file_hash = calculate_sha256(target_file)
        if file_hash:
            print(f"[+] SHA-256 Integrity Hash: {file_hash}")
    else:
        print("[-] Invalid action. Use 'hash'.")

if __name__ == "__main__":
    main()
