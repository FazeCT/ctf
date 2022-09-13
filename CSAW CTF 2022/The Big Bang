from pwn import *
import random
import binascii

p = remote("rev.chal.csaw.io", 5004)
MAGIC = 73

def gen_iv(tmp):
    iv_a = tmp
    return iv_a, [b"\xff" * MAGIC if iv_a[i] == '1' else b"\x00" * MAGIC for i in range(MAGIC)]

p.recvline()
tmp = p.recvline()[25:-1].decode()

iv_a, iv_b = gen_iv(tmp)
p.sendline(binascii.hexlify(b''.join(iv_b)))
p.interactive()
