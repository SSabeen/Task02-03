#TEST FILE 01 

import subprocess
import hashlib
import random
import yaml

# Hardcoded credentials (B105, B106)
USERNAME = "admin"
PASSWORD = "12345"   # insecure hardcoded password

# Insecure random (B311)
otp = random.random()
print("Generated OTP:", otp)

# Insecure hashing (B303)
md5_hash = hashlib.md5(b"hello").hexdigest()
print("MD5 Hash:", md5_hash)

# Dangerous eval usage (B307)
user_input = "5 + 5"
result = eval(user_input)
print("Eval Result:", result)

# Unsafe YAML Load (B506)
with open("config.yaml", "r") as f:
    data = yaml.load(f, Loader=yaml.Loader)
    print(data)

# Command injection risk with shell=True (B602, B607)
filename = "test.txt"
subprocess.run(f"cat {filename}", shell=True)
