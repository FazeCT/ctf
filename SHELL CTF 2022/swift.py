# Made by FazeCT

def func(a1):
    v3 = 1.0
    v4 = 0.0
    v5 = 1.0
    v2 = 1
    while (v3 != v4):
        v4 = v3
        v5 = a1 / v2 * v5
        v3 = v3 + v5
        v2 += 1
    return round(v3,6)

key = ""
data = [0.135335,0.367879,2.718282,7.389056,0.049787,1.000000,148.413159,0.367879,0.367879,2.718282,20.085537,148.413159]
str = "GVKCUSIVNABM"
enc = "wbppcugz{F4zp0i5_w3l1p5_sW_4_xHhO7j0r}"
for i in range(0,12):
    for a1 in range(0,200):
        tmp = func(i + a1 - ord(str[i]))
        if tmp == data[i]:
            key += chr(a1 + i)
print(key)

#Use Vigenere Cipher to decrypt the encoded flag and get: shellctf{t4yl0r5_s3r1e5_of_4_func7i0n}.
