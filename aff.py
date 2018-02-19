from sage.all_cmdline import *   # import sage library
import random as rand
# returns a two-tuple containing alpha and beta, legal and randomly generated
# affine keys
def key_gen_aff():
    alpha_size = 26

    #print inverse_mod(3,59)
    x = gen_key()
    b = rand.randint(0,100)
    return (x,b)

#Generates an x value that is co prime to m
def gen_key():
    num = 0
    while(True):
        num = rand.randint(2,26)
        if(gcd(num,26) == 1):
            return num

# reads and encrypts plain_txt using the affine cipher and key. writes the
# output to the file cipher_txt
def enc_aff(key, plain_txt, cipher_txt):
    with open(plain_txt,'r') as f:
        plain_txt = f.read()

    #plain_txt = tokenize(plain_txt)
    ci = ""
    for char in plain_txt:
        if(char.isdigit() or char.isalpha()):
            ci += char
    plain_txt = ci
    x = key[0]
    b = key[1]
    alpha_size = 26
    plain_txt = plain_txt.replace(" ","")
    total_string = ""
    for char in plain_txt:
        if(char.isalpha()):
            base_char = ord(char) - 65
        elif(char.isdigit()):
            #assumes integer
            base_char = ord(char) - 48
        else:
            break

        enc_char = ((base_char * x) +b) % alpha_size
        total_string += chr(int(enc_char)+65)
    encfile = open(cipher_txt,"w")
    encfile.write(total_string)
    return total_string

# reads and decrypts cipher_txt using the affine cipher and key. writes the
# output to the file plain_txt
def dec_aff(key, cipher_txt, plain_txt):
    with open(cipher_txt,'r') as f:
        cipher_txt = f.read()
    ci = ""

    for char in cipher_txt:
        if(char.isdigit() or char.isalpha()):
            ci += char

    cipher_txt = ci
    print cipher_txt
    mult_i = inverse_mod(key[0],26)
    b = key[1]
    alpha_size = 26
    cipher_txt = cipher_txt.replace(" ","")
    total_string = ""
    for char in cipher_txt:
        if(char.isalpha()):
            base_char = ord(char) - 65
        else:
            #assumes integer
            base_char = ord(char) - 48
        enc_char = (mult_i*(base_char-b)) % alpha_size
        total_string += chr(int(enc_char)+65)
    encfile = open(plain_txt,"w")
    encfile.write(total_string)
    return total_string
