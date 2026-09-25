#!/usr/bin/env python3
import os
import sys
import hashlib

def calculate_sha256(filename):
    """Calculates SHA-256 hash for file integrity verification."""
    sha256_hash = hashlib.sha256()
    try:
        with open(filename, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        print(f"[-] Error: File '{filename}' not found.")
        return None

def xor_cipher(input_file, output_file, key_byte=165):
    """Encrypts or decrypts a file using a symmetric key stream byte."""
    try:
        with open(input_file, "rb") as f:
            data = f.read()
        # Perform symmetric byte manipulation
        processed_data = bytes([b ^ key_byte for b in data])
        with open(output_file, "wb") as f:
            f.write(processed_data)
        print(f"[+] Processed: '{input_file}' -> '{output_file}' successfully.")
    except FileNotFoundError:
        print(f"[-] Error: Target file '{input_file}' missing.")
    except Exception as e:
        print(f"[-] Error processing file operations: {str(e)}")

def main():
    if len(sys.argv) < 3:
        print("--- ULK Security Toolkit ---")
        print("Usage:")
        print("  python toolkit.py encrypt [input_file] [output_file]")
        print("  python toolkit.py decrypt [input_file] [output_file]")
        print("  python toolkit.py hash [filename]")
        sys.exit(1)

    action = sys.argv[1].lower()
    
    if action in ["encrypt", "decrypt"]:
        if len(sys.argv) < 4:
            print("[-] Error: Missing output file path argument.")
            sys.exit(1)
        xor_cipher(sys.argv[2], sys.argv[3])
    elif action == "hash":
        file_hash = calculate_sha256(sys.argv[2])
        if file_hash:
            print(f"[+] SHA-256 Integrity Hash: {file_hash}")
    else:
        print("[-] Invalid action command parameter. Use hash, encrypt, or decrypt.")

if __name__ == "__main__":
    main()
