#TASK 03, TEST FILE 04!


import hashlib
import random
import base64

# Weak MD5 hashing (B303, B324)
password = "admin123"
hashed = hashlib.md5(password.encode()).hexdigest()
print("MD5:", hashed)

# Insecure randomness (B311)
token = random.randint(1, 999999)
print("Random token:", token)

# Weak base64 "encoding instead of encryption"
encoded = base64.b64encode(password.encode())
print("Encoded:", encoded)
