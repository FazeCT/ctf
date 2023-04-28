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

f = open('E:/Downloads/flag.enc', 'rb').read()

seed = int.from_bytes(f[:4], 'little')

rol = lambda val, r_bits, max_bits: \
    (val << r_bits%max_bits) & (2**max_bits-1) | \
    ((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))

rand = [2014390344, 1469870660, 1982650619, 1625766133, 692418227, 51836669, 1207566194, 29148633, 1814471238, 927732162, 1046980137, 565814735, 422047055, 1517221094, 1814698569, 753299776, 2030934960, 1040711614, 1195375342, 920661508, 574642855, 351439671, 1713504022, 1635586270, 1468557073, 920046345, 1005726139, 1081414708, 653914299, 1269692214, 1744271893, 520820995, 592079226, 1579438864, 2146587128, 1284497453, 1631275533, 1206669674, 1313646087, 1298263123, 2134401837, 213142576, 1864077858, 408965244, 1730363670, 1531292779, 1162265020, 1613814982, 424520745, 210156714, 386992843, 999163600, 561596385, 2100496865, 487266223, 2030153458, 873059562, 1492992362, 964084519, 1526973861, 615200929, 560872764, 2047794857, 1207280155, 2140311628, 2046898337, 344293961, 1624103513, 1106084364, 1657940048, 774882988, 1093002553, 1871082624, 491477198, 1501967797, 1453962647, 2022769977, 516749169, 920293981, 299807074, 726905883, 1307286824, 1298970674, 1288502269, 1260300041, 1786236897, 1171172079, 2133359603, 1131745612, 2135256598, 1512849817, 1746946541, 548645714, 1413161026, 806743048, 541473694, 1312575715, 1151037009, 18093559, 271176431]
idx = 0

for i in f[4:]:
    rand_1 = rand[idx]
    rand_2 = rand[idx + 1]
    idx += 2
    for c in range(256):
        k = (c ^ rand_1) & 0xFF
        v3 = rand_2
        f = rol(k, v3 & 7, 8)
        if f == i:
            print(chr(c), end='')
            break



