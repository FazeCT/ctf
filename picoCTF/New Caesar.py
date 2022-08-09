#Made by FazeCT

import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

def unshift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t2+10*len(ALPHABET)-t1) % len(ALPHABET)]

data = "mlnklfnknljflfjljnjijjmmjkmljnjhmhjgjnjjjmmkjjmijhmkjhjpmkmkmljkjijnjpmhmjjgjj"

for j in range(len(ALPHABET)):
    key = ALPHABET[j]
    flag = ""
    for i in range(len(data)):
        flag += unshift(key[i%len(key)],data[i])
    realflag=""
    for i in range(0,len(flag),2):
        n1 = ord(flag[i]) - LOWERCASE_OFFSET
        n2 = ord(flag[i+1]) - LOWERCASE_OFFSET
        binary = bin(n1)[2:].zfill(4) + bin(n2)[2:].zfill(4)
        realflag += chr(int(binary, 2))
    print(realflag)

