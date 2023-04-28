from Crypto.Util.number import *
from Crypto.Cipher import AES
from Crypto.Cipher import DES
from Crypto.Hash import MD5
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

s = Solver()
v3 = [BitVec('x{}'.format(i), 8) for i in range(32)]

for i in range(len(v3)):
    s.add(And(v3[i] <= 125, v3[i] >= 32))

form = b'HTB{'
for i in range(len(form)):
    s.add(v3[i] == form[i])

s.add(v3[29] == v3[5] - v3[3] + 70)
s.add(v3[22] + v3[2] == v3[13] + 123)
s.add(v3[4] + v3[12] == v3[5] + 28)
s.add(v3[23] * v3[25] == v3[17] + v3[0] + 23)
s.add(v3[1] * v3[27] == v3[22] + v3[5] - 21)
s.add(v3[13] * v3[9] == v3[3] * v3[28] - 9)
s.add(v3[9] == 112)
s.add(v3[21] + v3[19] == v3[6] + 0x80)
s.add(v3[16] == v3[15] - v3[11] + 48)
s.add(v3[27] * v3[7] == v3[13] * v3[1] + 45)
s.add(v3[13] == v3[13] + v3[18] - 101)
s.add(v3[20] - v3[8] == v3[9] + 124)
s.add(v3[31] == v3[8] - v3[31] - 121)
s.add(v3[31] * v3[20] == v3[20] + 4)
s.add(v3[24] - v3[17] == v3[8] + v3[21] - 23)
s.add(v3[5] + v3[7] == v3[29] + v3[5] + 44)
s.add(v3[10] * v3[12] == v3[1] - v3[11] - 36)
s.add(v3[0] * v3[31] == v3[26] - 27)
s.add(v3[20] + v3[1] == v3[10] - 125)
s.add(v3[18] == v3[14] + v3[27] + 2)
s.add(v3[11] * v3[30] == v3[21] + 68)
s.add(v3[19] * v3[5] == v3[1] - 44)
s.add(v3[13] - v3[26] == v3[21] - 127)
s.add(v3[23] == v3[29] - v3[0] + 88)
s.add(v3[19] == v3[13] * v3[8] - 23)
s.add(v3[22] + v3[6] == v3[3] + 83)
s.add(v3[12] == v3[7] + v3[26] - 114)
s.add(v3[16] == v3[18] - v3[5] + 51)
s.add(v3[30] - v3[8] == v3[29] - 77)
s.add(v3[20] - v3[11] == v3[3] - 76)
s.add(v3[16] - v3[7] == v3[17] + 102)
s.add(v3[21] + v3[1] == v3[18] + v3[11] + 43)

if s.check() == sat:
    result = s.model()

    string = [result[v3[i]].as_long() for i in range(32)]
    s2 = ''.join(map(chr, string))
    print(s2)
