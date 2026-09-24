# Cryptography and Network Security Toolkit
**Institution:** ULK Polytechnic Institute  
**Module Code:** ETTCS801  
**Assessment:** Integrated Situation Evaluation Portfolio  

## Project Deployment Architecture
* `toolkit.py`: Custom zero-dependency cryptography tool (XOR Cipher & SHA-256 hashing).
* `risk_assessment.md`: Core infrastructure vulnerability audit report matrix.
* `filter_tests.md`: Netfilter kernel isolation tables and test diagnostics.
* `report.tex`: Academic LaTeX documentation production source.

## Execution Framework Manual

### 1. Integrity Verification Checks
To generate a secure validation fingerprint of any file item:
```bash
python toolkit.py hash risk_assessment.md
```

### 2. Confidentiality File Enciphering
To encrypt a source record artifact securely to disk:
```bash
python toolkit.py encrypt risk_assessment.md encrypted_data.enc
```

### 3. File Deciphering Verification
To restore an encrypted payload back into human-readable plaintext state:
```bash
python toolkit.py decrypt encrypted_data.enc restored_doc.txt
```
