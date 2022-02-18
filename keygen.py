
import random
import json

#creating a secret key for the program. The key is a random string of 35 digits.


def keygen():
    ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    chars = [random.choice(ALPHABET) for _ in range(35)]
    sk = "".join(chars)
#the key is saved in a key.json file.
    with open('key.json', 'w') as f:
        json.dump(sk, f)
              
keygen()
