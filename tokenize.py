#tokenize is shared by all functions
#raw_file is a file with the message to be encrypted
#plain_txt is raw_file with alpha chars transformed to uppercase, white space
#removed, and eol inserted every fifty characters.
def tokenize(raw_file, plain_txt):
    raw = open(raw_file,"r")
    plain = open(plain_txt, "w")
    chars = 0
    writeline = ""
    while True:
        line = raw.readline()
        if not line:
            break
        for char in line:
            if char.isalpha():
                writeline += char.upper()
                chars += 1
            else:
                if char != ' ' and char != '_' and char != '\n' and char != '\t':
                    writeline += char
                    chars += 1
            if chars >= 50:
                writeline += '\n'
                chars = 0
    plain.write(writeline)
    raw.close()
    plain.close()
    return
