# Password Cracker - MD5 Dictionary Attack Tool

Educational password cracking tool built to understand dictionary attack methodology and hash comparison algorithms.

## Overview

This project demonstrates how password cracking works by implementing an MD5 dictionary attack from scratch. Built as part of cybersecurity learning journey to understand both offensive and defensive security concepts.

## Features

- MD5 hash cracking using dictionary attacks
- Command-line interface for professional usage
- Performance timing and speed analysis
- Comprehensive error handling and input validation
- Educational documentation for cybersecurity learning

## Usage

### Command Line Mode
```bash
python password_cracker.py <target_hash> <wordlist_file>
```

## Example Usage
```bash
python password_cracker.py 482c811da5d5b4bc6d497ffa98491e38 common_passwords.txt
```

## Test Mode (Run Built-in Tests)
```bash
python password_cracker.py
```

## Technical Specifications
- Hash Algorithm: MD5 (128-bit)
- Attack Method: Dictionary-based password testing
- Performance: 1000+ attempts per second
- Input Format: 32-character hexadecimal MD5 hashes
- Wordlist Format: Plain text, one password per line

## Project Structure
```
password-cracker-md5/
├── password_cracker.py          # Main cracking script
├── common_passwords.txt         # Sample wordlist (15 passwords)
├── target_hashes.txt           # Test target hashes (5 MD5 hashes)
├── docs/
│   ├── development-log.md      # Development progress documentation
│   ├── technical-analysis.md   # Code architecture analysis  
│   └── security-implications.md # Ethical considerations
└── README.md                   # This file
```

## Sample Results
```
Password Cracker v1.0
Target: 482c811da5d5b4bc6d497ffa98491e38
Wordlist: common_passwords.txt
--------------------------------------------------
SUCCESS!
Password: password123
Attempts: 1
Duration: 0.010 seconds
Speed: 98 attempts/second
```

## Educational Objectives
- Understand password vulnerability assessment techniques
- Learn dictionary attack implementation and methodology
- Analyze hash comparison algorithms and performance
- Practice ethical hacking tool development
- Explore cybersecurity defensive strategies

## Security Considerations
This tool is developed for educational and authorized testing purposes only.
- Never use against systems without explicit written permission
- Understand legal implications of password cracking tools
- Practice responsible disclosure for discovered vulnerabilities
- Use knowledge to improve defensive security measures

## Installation
1. Ensure Python 3.x is installed
2. Clone this repository
3. No additional dependencies required(uses built-in libraries)

## License
This project is for educational purposes. Use responsibly and ethically
