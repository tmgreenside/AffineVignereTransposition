from sage.all_cmdline import *   # import sage library

#tokenize is shared by all functions
#raw_file is a file with the message to be encrypted
#plain_txt is raw_file with alpha chars transformed to uppercase, white space
#removed, and eol inserted every fifty characters.
def tokenize(raw_file, plain_txt):
    return

# returns a two-tuple containing alpha and beta, legal and randomly generated
# affine keys
def key_gen_aff():
    return

# reads and encrypts plain_txt using the affine cipher and key. writes the
# output to the file cipher_txt
def enc_aff(key, plain_txt, cipher_txt):
    return

# reads and decrypts cipher_txt using the affine cipher and key. writes the
# output to the file plain_txt
def dec_aff(key, cipher_txt, plain_txt):
    return

# returns a randomly generated vigenere key of length, "key_length".
def key_gen_vig(key_length):
    return

# reads and encrypts plain_txt using the vigenere cipher and key. writes the
# output to the file cipher_txt
def enc_vig(key, plain_txt, cipher_txt):
    return

# reads and decrypts cipher_txt using the vigenere cipher and key. writes
# the output to the file plain_txt
def dec_vig(key, cipher_txt, plain_txt):
    return

# returns a randomly generated upper-case alphabet
def key_gen_trans():
    alphabet = ""
    for letter in range(26):

    return

# reads and encrypts plain_txt using the alphabetic transposition cipher and
# key and writes the output to the file cipher_txt.  A dictionary will be
# useful.
def enc_trans(key, plain_txt, cipher_txt):
    return

# reads and decrypts cipher_txt using the alphabetic transpositon cipher and
# key and writes the output to the file plain_txt
def dec_trans(key, cipher_txt, plain_txt):
    return
