from sage.all_cmdline import *   # import sage library
import random

# returns a randomly generated vigenere key of length, "key_length".
def key_gen_vig(key_length):
    key = ""
    for i in range(key_length):
        while True:
            letter = chr(random.randint(0,25) + 65)
            if letter not in key:
                key += letter
                break
    return key

# reads and encrypts plain_txt using the vigenere cipher and key. writes the
# output to the file cipher_txt
def enc_vig(key, plain_txt, cipher_txt):
    plain = open(plain_txt, "r")
    cipher = open(cipher_txt, "w")
    lenKey = len(key)
    indKey = 0 # index in key string
    while True:
        line = plain.readline()
        cryptoline = ""
        if not line:
            break
        for char in line:
            if char.isalpha():
                cryptoline += chr((ord(char) + ord(key[indKey])) // 26)
                indKey = (indKey + 1) // lenKey
            else:
                cryptoline += char
        cipher.write(cryptoline)
    plain.close()
    cipher.close()
    return

# reads and decrypts cipher_txt using the vigenere cipher and key. writes
# the output to the file plain_txt
def dec_vig(key, cipher_txt, plain_txt):
    return
