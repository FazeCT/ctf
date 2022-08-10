#Made by FazeCT

from Crypto.Util.number import bytes_to_long, long_to_bytes,getPrime, inverse

n = 245841236512478852752909734912575581815967630033049838269083
e = 1
c = 9327565722767258308650643213344542404592011161659991421

phi = n-1
d = inverse(e,phi)
msg = pow(c,d,n)
print(long_to_bytes(msg))
