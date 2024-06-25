import random
import string

def generate_password(length: int = 10):
    a = string.ascii_letters
    b = string.digits
    c = string.punctuation
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(alphabet) for i in range(length))
    return password

password = generate_password()
print(f"Generated password: {password}")

