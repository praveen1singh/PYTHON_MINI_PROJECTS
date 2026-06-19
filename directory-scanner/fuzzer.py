import requests
import sys

    
def loop():
    for word in sys.stdin:
        res = requests.get(url=f"https://facebook.com/{word}")
        if res.status_code == 404:
            loop()
        else:
             data = res.text
             print(data)
             print(res.status_code)
             print(word)
loop()
