import os
import hashlib

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def calculate_hash(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b''):
            sha256_hash.update(chunk)
    return sha256_hash.hexdigest()

def check_integrity(file_path):
    clear_screen()
    if not os.path.isfile(file_path):
        print(f"{file_path} does not exist or is not a file.")
        return

    return calculate_hash(file_path)

if __name__ == "__main__":
    integrity_checksum = input("Enter an integrity checksum: ")
    file_path = input("Enter file path to check integrity: ")
    fPath = file_path.replace('"', "")
    file_hash = check_integrity(fPath)
    
    if file_hash is not None:
        if integrity_checksum == file_hash:
            print(f"✅ SHA256 Signatures Match! ✅\n{integrity_checksum}\n{file_hash}")
        else:
            print(f"❌ SHA256 Signatures Do Not Match! ❌\n{integrity_checksum}\n{file_hash}")