URL Fuzzer :
A simple Python-based URL fuzzing tool that checks different paths on a target URL using a wordlist.

Description :
This tool takes paths from standard input, appends them to a target URL, sends HTTP GET requests, and displays the response details.
It is useful for checking which paths return valid responses.

Example:
Wordlist:
admin
login
robots.txt
test

Requests generated:
https://target.com/admin
https://target.com/login
https://target.com/robots.txt
https://target.com/test

Features
Read paths from a wordlist
Send HTTP GET requests
Check HTTP response status codes
Display response content
Display tested path

Requirements
Python 3.x
Install dependency:
pip install requests

Usage
Run the tool with a wordlist:
cat wordlist.txt | python3 fuzzer.py

Example:
cat paths.txt | python3 fuzzer.py

Output example:
200
login

403
admin

404
test
