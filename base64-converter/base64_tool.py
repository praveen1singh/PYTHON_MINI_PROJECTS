#Create a password encoding program

import base64
# import getpass
import maskpass

def encode_pass(password):
    # convert strings into byptes password.encode() => "hello" => b'hello'
    encoded_bytes = base64.b64encode(password.encode())
    print(encoded_bytes)
    return

# hide the input password
# user_pass = getpass.getpass("Enter your password :")
user_pass = maskpass.askpass("Enter your password :")

encode_pass(user_pass)



# password decoding program :

def decode_pass(password):
    decoded_bytes=base64.b64decode(password)
    decoded_data = decoded_bytes.decode()
    print(f"decoded password : {decoded_data}")

encode_string = input("Enter the base64 string :")
decode_pass(encode_string)
