# FILE-INTEGRITY-CHECKER

**COMPANY** : CODTECH IT SOLUTIONS

**NAME**: SAKSHI UMESH TELI

**INTERN ID**:CT08MBS

**DOMAIN**:CYBER SECURITY AND ETHICAL HACKING

**BATCH DURATION**:JANUARY 15TH,2025 TO FEBRUARY 15TH,2025

**MENTOR NAME**:NEELA SANTHOSH

#  DESCRIPTION OF TASK PERFORMED IS:
   
**File Integrity Checker:-**
The File Integrity Checker is a simple Python tool that helps detect changes in files. It calculates and compares hash values to ensure files remain unchanged, making it useful for security and monitoring.

**Features:-**
Generates unique hash values for files (SHA-256, MD5, etc.)
1. Detects if a file is modified, deleted, or added
2. Works with multiple files and folders
3. Uses a lightweight and efficient approach

**Technologies Used**
1.Python
2.hashlib (for generating hash values)
3.os (for handling files)
4.json (for storing file hashes)

**How It Works**
1.The tool scans files and generates a hash for each one.
2.It saves these hashes in a reference file.
3.On the next run, it checks the current hashes against the stored ones.
4.If a file has changed, is missing, or a new file is added, it reports the difference.
