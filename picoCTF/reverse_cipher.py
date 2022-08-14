#Made by FazeCT

data = 'picoCTF{w1{1wq84fb<1>49}'
print(data[:7], end = '')
print('{', end = '')
for i in range(8,23):
    if i & 1 != 0:
        print(chr(ord(data[i]) + 2), end = '')
    else:
        print(chr(ord(data[i]) - 5), end = '')
print('}', end = '')
