from sage.all_cmdline import *   # import sage library
from vig import *
from aff import *

#tokenize is shared by all functions
#raw_file is a file with the message to be encrypted
#plain_txt is raw_file with alpha chars transformed to uppercase, white space
#removed, and eol inserted every fifty characters.
def tokenize(raw_file, plain_txt):
    return

x = key_gen_aff()
e = enc_aff(x, "plain.txt",'cipher.txt')
d = dec_aff(x,"cipher.txt","plain.txt")
print d
