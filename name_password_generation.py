import random
import string

def gen_password(name):
    chars = string.ascii_letters + string.digits + string.punctuation
    return name[:3] + ''.join(random.choice(chars) for _ in range(6))
print(gen_password("Ram"))
