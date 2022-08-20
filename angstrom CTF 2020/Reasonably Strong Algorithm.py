#Made by FazeCT

from Crypto.Util.number import bytes_to_long, long_to_bytes,getPrime, inverse

n = 126390312099294739294606157407778835887
e = 65537
c = 13612260682947644362892911986815626931
p = 9336949138571181619
q = 13536574980062068373

phi = (p-1)*(q-1)
d = inverse(e,phi)
msg = pow(c,d,n)
print(long_to_bytes(msg))
