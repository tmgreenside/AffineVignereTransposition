#transposition cipher

from sage.all_cmdline import *   # import sage library
import random


# returns a randomly generated upper-case alphabet
def key_gen_trans():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #create permutation of alphabet
	perm = [ord(x)-64 for x in alphabet]

    return perm

#takes a string and turns it into a numeric list
def str21st(s):
	return [ord(x)-65 for x in s]

#takes a list and turns it back into a string
def lst2str(lst):
	return join([chr(int(x)+65) for x in lst],'')


# reads and encrypts plain_txt using the alphabetic transposition cipher and
# key and writes the output to the file cipher_txt.  A dictionary will be
# useful.
#take list and turns back to string
def enc_trans(perm, plain_txt, cipher_txt):
    #open plain_txt to read
	plain = open(plain_txt, "r")
    #open cipher_txt to write
    cipher = open(cipher_txt, "w")

    '''
     #turns string into numeric list
    pln = str21st(plain)
    plr = [perm[pln[i]]-1 for i in range(len(pl))]

    #take list and turns back to string
    lst2str(plr)

    #need to save plr to cipher_txt
    cipher.write(plr)
    '''

    while True:
        currLine = plain.readline()
        #make string currLine into a list
        #pass through str21st()

        pln = str21st(currLine) #turns string into numeric list
        plr = [perm[pln[i]]-1 for i in range(len(currLine))]

        #take list and turns back to string
        lst2str(plr)

        #need to save plr to cipher_txt
        cipher.write(plr)



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

    while True:
        currLine = plain.readline()

        #inverse permutation
        #Sage has this functionality
        inverseKey = Permutation(key).inverse()

        pls = [inverseKey[currLine[i]]-1 for i in range((currLine))]

        lst2str(pls)

        plain.write(pls)

    plain.close()
    cipher.close()

    return
