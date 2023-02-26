# ACSC 2023
## serverless

## Information
**Category** | **Points** | **Writeup Author**
--- | --- | ---
Reverse Engineering | 80 | Onirique

**Description:** 

I made a serverless encryption service. It is so serverless that you should host it yourself.

I encrypted the flag with "acscpass" as the password, but have not finished implementing the decryption feature. Help me decrypt the flag!

MTE3LDk2LDk4LDEwNyw3LDQzLDIyMCwyMzMsMTI2LDEzMSwyMDEsMTUsMjQ0LDEwNSwyNTIsMTI1LDEwLDE2NiwyMTksMjMwLDI1MCw4MiwyMTEsMTAxLDE5NSwzOSwyNDAsMTU4LDE3NCw1OSwxMDMsMTUzLDEyMiwzNiw2NywxNzksMjI0LDEwOCw5LDg4LDE5MSw5MSwxNCwyMjQsMTkzLDUyLDE4MywyMTUsMTEsMjYsMzAsMTgzLDEzMywxNjEsMTY5LDkxLDQ4LDIyOSw5OSwxOTksMTY1LDEwMCwyMTgsMCwxNjUsNDEsNTUsMTE4LDIyNywyMzYsODAsMTE2LDEyMCwxMjUsMTAsMTIzLDEyNSwxMzEsMTA2LDEyOCwxNTQsMTMzLDU1LDUsNjMsMjM2LDY5LDI3LDIwMSwxMTgsMTgwLDc0LDIxMywxMzEsNDcsMjAwLDExNiw1Miw0OSwxMjAsODYsMTI0LDE3OCw5MiwyNDYsMTE5LDk4LDk1LDg2LDEwNCw2NCwzMCw1NCwyMCwxMDksMTMzLDE1NSwxMjIsMTEsODcsMTYsMjIzLDE2MiwxNjAsMjE1LDIwOSwxMzYsMjQ5LDIyMSwxMzYsMjMy

## Solution

The **encrypt.js** holds all of the logic of the whole encrypting system. After changing some of the number obfuscation, I immediately realized that the flow of the function 'b(d,f)' was like so:

- First, it receives our message as d and our password 'acscpass' as f.

- Randomly chooses a hex number from each of the array g, h, then assigns the multiplication of them into variable r.

- Variable t would be one of these numbers: 3 5 17 257 65537.

At this point, I knew that this 'encoding system' is using **RSA encryption**.

- Function 'u(A)' is used to concatenate a list of numbers into a single big number, using shift left logical of 8.

- Funtion 'w(A, B, C)' is used to calculate A ** B, modulo C.

- Array 'y' contains parts of x using shift right logical of 8.

- Variable s, k, j are appended to the end of the array 'y'. (This is very crucial for solving this challenge).

- Last part is just a simple XOR encryption with key = 'acscpass', then the string is reversed and base-64 encoded before being printed out as ciphertext.

I reversed everything using Python and the ciphertext given in the description, and we get the flag:

```python
from Crypto.Util.number import *
data = [117,96,98,107,7,43,220,233,126,131,201,15,244,105,252,125,10,166,219,230,250,82,211,101,195,39,240,158,174,59,103,153,122,36,67,179,224,108,9,88,191,91,14,224,193,52,183,215,11,26,30,183,133,161,169,91,48,229,99,199,165,100,218,0,165,41,55,118,227,236,80,116,120,125,10,123,125,131,106,128,154,133,55,5,63,236,69,27,201,118,180,74,213,131,47,200,116,52,49,120,86,124,178,92,246,119,98,95,86,104,64,30,54,20,109,133,155,122,11,87,16,223,162,160,215,209,136,249,221,136,232][::-1]
key = "acscpass"
for i in range(len(data)):
    data[i] ^= ord(key[i % 8])
# j = 6
# k = 3
# s = 3
data = data[:-3]
x = 0
j = 0
for i in data:
    x += i * pow(2, j * 8)
    j += 1

t = pow(2,pow(2, 3)) + 1
n = 0x96e2cefe4c1441bec265963da4d10ceb46b7d814d5bc15cc44f17886a09390999b8635c8ffc7a943865ac67f9043f21ca8d5e4b4362c34e150a40af49b8a1699 * 0xf79dd7feae09ae73f55ea8aa40c49a7bc022c754db41f56466698881f265507144089af47d02665d31bba99b89e2f70dbafeba5e42bdac6ef7c2f22efa680a67

phi = (0x96e2cefe4c1441bec265963da4d10ceb46b7d814d5bc15cc44f17886a09390999b8635c8ffc7a943865ac67f9043f21ca8d5e4b4362c34e150a40af49b8a1699 - 1)*(0xf79dd7feae09ae73f55ea8aa40c49a7bc022c754db41f56466698881f265507144089af47d02665d31bba99b89e2f70dbafeba5e42bdac6ef7c2f22efa680a67 - 1)
d = inverse(t,phi)
v = pow(x,d,n)
flag = ''
while v > 0:
    flag += chr(v & 0xFF)
    v >>= 8
print(flag[::-1])
```

> Flag is: ACSC{warmup_challenge_so_easy}
