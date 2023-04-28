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

encrypted = [0x29, 0x38, 0x2B, 0x1E, 0x06, 0x42, 0x05, 0x5D, 0x07, 0x02,
  0x31, 0x10, 0x51, 0x08, 0x5A, 0x16, 0x31, 0x42, 0x0F, 0x33,
  0x0A, 0x55, 0x00, 0x00, 0x15, 0x1E, 0x1C, 0x06, 0x1A, 0x43,
  0x13, 0x59, 0x14]

print(xor(encrypted, 'aliens'))
