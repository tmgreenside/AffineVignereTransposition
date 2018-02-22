#transposition cipher

from sage.all_cmdline import *   # import sage library
import random

# returns a randomly generated upper-case alphabet
def key_gen_trans():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #create permutation of alphabet
    enumAlpha = [ord(x)-64 for x in alphabet]
    perm = ""
    shuffle(enumAlpha)
    for i in enumAlpha:
        perm += chr(i + 64)
    return perm

#takes a string and turns it into a numeric list
def str21st(s):
	return [ord(x)-65 for x in s]

#takes a list and turns it back into a string
def lst2str(lst):

    currStr = ""
    for x in lst:
        currStr += str(chr(ord(x) + 65))
    return currStr


# reads and encrypts plain_txt using the alphabetic transposition cipher and
# key and writes the output to the file cipher_txt.  A dictionary will be
# useful.
#take list and turns back to string
def enc_trans(perm, plain_txt, cipher_txt):
    #open plain_txt to read
    plain = open(plain_txt, "r")
    #open cipher_txt to write
    cipher = open(cipher_txt, "w")

    while True:
        currLine = plain.readline()
        if not currLine:
            break
        print currLine
        cipherline = ""
        for char in currLine:
            if char.isalpha():
                #print ord(char) - 65
                cipherline += perm[ord(char) - 65]
        cipherline += "\n"
        cipher.write(cipherline)

    plain.close()
    cipher.close()

    return #plr #returns string of permuted plaintext

# reads and decrypts cipher_txt using the alphabetic transpositon cipher and
# key and writes the output to the file plain_txt
def dec_trans(key, cipher_txt, plain_txt):
    #open cipher_txt to read
    cipher = open(cipher_txt, "r")
    #open plain_txt to write to
    plain = open(plain_txt, "w")

    print "Decrypting"

    while True:
        currLine = cipher.readline()
        if not currLine:
            break
        print currLine
        #inverse permutation
        #Sage has this functionality
        decryptline = ""
        for char in currLine:
            if char.isalpha():
                decryptline += chr(key.find(char) + 65)

        print decryptline
        decryptline += "\n"
        plain.write(decryptline)

    plain.close()
    cipher.close()

    return
