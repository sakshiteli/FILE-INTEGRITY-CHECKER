# FILE-INTEGRITY-CHECKER

**COMPANY** : CODTECH IT SOLUTIONS

**NAME**: SAKSHI UMESH TELI

**INTERN ID**:CT08MBS

**DOMAIN**:CYBER SECURITY AND ETHICAL HACKING

**BATCH DURATION**:JANUARY 15TH,2025 TO FEBRUARY 15TH,2025

**MENTOR NAME**:NEELA SANTHOSH

#  DESCRIPTION OF TASK PERFORMED IS:
   
#File Integrity Checker
# Overview
The File Integrity Checker is a Python-based tool designed to monitor changes in files by calculating and comparing hash values. This tool ensures file integrity and detects unauthorized modifications, making it useful for security and system monitoring.

#Features
Computes cryptographic hash values (SHA-256, MD5, etc.)
Detects unauthorized file changes or tampering
Supports multiple files and directories
Logs file status (Unchanged, Modified, or Missing)
Simple and efficient using the hashlib library

#Technologies Used
Python
hashlib (for hash calculations)
os (for file handling)
json (for storing hash records)
  
#How It Works
The tool generates a hash value for each file in a directory.
Stores the hash values in a reference file (JSON or text format).
On the next run, it recalculates the hashes and compares them with the stored values.
Reports any changes, missing, or newly added files.
