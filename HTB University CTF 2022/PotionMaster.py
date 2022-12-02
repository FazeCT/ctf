from pwn import *
import datetime
import time
import math
from Crypto.Util.number import bytes_to_long, long_to_bytes,getPrime, inverse
import base64
import subprocess
import angr
import claripy
from z3 import *
from Crypto.Cipher import AES

ordHelperCounter = 0
def OrdAt(inp, i):
    return StrToCode(SubString(inp, i, 1))

a = [-43, 61, 58, 5, -4, -11, 64, -40, -43, 61, 62, -51, 46, 15, -49, -44, 47, 4, 6, -7, 47, 7, -59, 52, -15, 11, 7, 61, 0]
b = [6, 106, 10, 0, 119, 52, 51, 101, 0, 0, 15, 48, 116, 22, 10, 58, 125, 100, 102, 33]
c = [304, 357, 303, 320, 304, 307, 349, 305, 257, 337, 340, 309, 428, 270, 66]
d = [52, 52, 95, 95, 110, 49, 51, 51, 95, 110, 110, 53]

s = Solver()
x = [BitVec('x{}'.format(i), 8) for i in range(58)]
for i in range(len(x)):
    s.add(And(x[i] <= 125,  x[i] >= 32))
tmp = 0
tmp2 = 1
for i in a:
    s.add(x[tmp] - x[tmp2] == i)
    tmp += 2
    tmp2 += 2
tmp = 0
tmp2 = 1
tmp3 = 2
for i in b:
    t = 0
    if tmp < 58: t ^= x[tmp]
    if tmp2 < 58: t ^= x[tmp2]
    if tmp3 < 58: t ^= x[tmp3]
    s.add(t == i)
    tmp += 3
    tmp2 += 3
    tmp3 += 3
tmp = 0
tmp2 = 1
tmp3 = 2
tmp4 = 3
for i in c:
    t = 0
    if tmp < 58: t += x[tmp]
    if tmp2 < 58: t += x[tmp2]
    if tmp3 < 58: t += x[tmp3]
    if tmp4 < 58: t += x[tmp4]
    s.add(t == i)
    tmp += 4
    tmp2 += 4
    tmp3 += 4
    tmp4 += 4
tmp = 0
for i in d:
    if tmp < 58: s.add(x[tmp] == i)
    tmp += 5
if s.check() == sat:
    result = s.model()
    string = [result[x[i]].as_long() for i in range(58)]
    s = ''.join(map(chr, string))
    print(s)


