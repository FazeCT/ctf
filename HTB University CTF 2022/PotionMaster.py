from Crypto.Util.number import *
from Crypto.Cipher import AES
from Crypto.Cipher import DES
from Crypto.Hash import MD5
from Crypto.PublicKey import RSA
from Crypto.Util.Padding import unpad
from Crypto.Cipher import Blowfish
from malduck import xor
from sympy.ntheory.modular import crt
from sympy import *
from z3 import *
from pwn import *
from subprocess import *
from itertools import *
from PIL import Image
from copy import *

import gmpy2
import json
import base64
import hashlib
import requests
import angr
import numpy as np
import binascii
import codecs
import time
import claripy
import sympy
import subprocess
import itertools
import ctypes
import re
import math

a = [-43, 61, 58, 5, -4, -11, 64, -40, -43, 61, 62, -51, 46, 15, -49, -44, 47, 4, 6, -7, 47, 7, -59, 52, 17, 11, -56, 61, -74, 52, 63, -21, 53, -17, 66, -10, -58, 0]
b = [6, 106, 10, 0, 119, 52, 51, 101, 0, 0, 15, 48, 116, 22, 10, 58, 93, 59, 106, 43, 30, 47, 93, 62, 97, 63]
c = [304, 357, 303, 320, 304, 307, 349, 305, 257, 337, 340, 309, 396, 333, 320, 380, 362, 368, 286]
d = [52, 52, 95, 95, 110, 49, 51, 51, 95, 110, 110, 53, 116, 51, 98, 63]

len = 76
s = Solver()
x = [BitVec('x{}'.format(i), 8) for i in range(len)]
for i in range(len):
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
    if tmp < len: 
        t ^= x[tmp]
    if tmp2 < len: 
        t ^= x[tmp2]
    if tmp3 < len: 
        t ^= x[tmp3]
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
    if tmp < len: 
        t += x[tmp]
    if tmp2 < len: 
        t += x[tmp2]
    if tmp3 < len: 
        t += x[tmp3]
    if tmp4 < len: 
        t += x[tmp4]
    s.add(t == i)
    tmp += 4
    tmp2 += 4
    tmp3 += 4
    tmp4 += 4
tmp = 0
for i in d:
    if tmp < len: 
        s.add(x[tmp] == i)
    tmp += 5

if s.check() == sat:
    result = s.model()
    string = [result[x[i]].as_long() for i in range(76)]
    s = ''.join(map(chr, string))
    print('HTB{' + s + '}')
