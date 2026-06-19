Password Encoder & Decoder :
A simple Python program that encodes and decodes passwords using Base64 encoding.
The program also hides password input while typing using the maskpass library.

Features :
Encode a password into Base64 format
Decode a Base64 string back to original text
Hide password input while entering
Simple command-line based tool

Requirements :
Python 3.x
maskpass library

Installation :
Install the required library:
pip install maskpass
Usage

Run the program:
python3 password_encoder.py

How It Works
Encoding :
User enters a password. maskpass hides the password input.
password.encode() converts the string into bytes.
base64.b64encode() converts bytes into Base64 format.

Decoding : 
base64.b64decode() converts it back into bytes.
.decode() converts bytes back into readable text.

Note :
Base64 is an encoding method, not encryption. It can be easily decoded, so it should not be used for storing real passwords securely.
For secure password storage, use password hashing algorithms like bcrypt or Argon2.
