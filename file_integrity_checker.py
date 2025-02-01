import hashlib
import os
import json

def generate_file_hash(file_path):
    """Generate SHA-256 hash of a file."""
    hasher = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(4096):
            hasher.update(chunk)
    return hasher.hexdigest()

def create_baseline(directory, output_file="baseline.json"):
    """Create a baseline hash for all files in a directory."""
    file_hashes = {}
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hashes[file_path] = generate_file_hash(file_path)
    
    with open(output_file, "w") as f:
        json.dump(file_hashes, f, indent=4)

    print("Baseline created successfully.")

def verify_integrity(baseline_file="baseline.json"):
    """Compare current file hashes with baseline to detect changes."""
    with open(baseline_file, "r") as f:
        baseline_hashes = json.load(f)

    modified_files = []
    for file_path, old_hash in baseline_hashes.items():
        if os.path.exists(file_path):
            new_hash = generate_file_hash(file_path)
            if new_hash != old_hash:
                modified_files.append(file_path)
        else:
            print(f"Warning: File missing - {file_path}")

    if modified_files:
        print("Modified Files Detected:")
        for file in modified_files:
            print(file)
    else:
        print("All files are intact.")

if __name__ == "__main__":
    directory = input("Enter the directory path to monitor: ")
    action = input("Enter 'create' to generate baseline or 'verify' to check integrity: ")
    
    if action.lower() == "create":
        create_baseline(directory)
    elif action.lower() == "verify":
        verify_integrity()
    else:
        print("Invalid option. Use 'create' or 'verify'.")
