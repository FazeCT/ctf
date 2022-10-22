from pwn import *
from geopy.geocoders import Nominatim
import geocoder

p = remote("137.184.215.151", 22606)
geolocator = Nominatim(user_agent="geoapiExercises")

s = p.recvlines(36)
for i in range(50):
    a = p.recvline().decode()
    print(a)
    txt = p.recvline().decode()
    print(txt)
    if txt[0] == 'C':
        x = txt.split()
        x[3] = x[3][0:len(x[3])-1]
        location = geolocator.reverse(x[3] + "," + x[4])
        addr = location.raw['address']
        city = addr.get('city', '')
        print(city)
        p.sendline(city)
    else:
        x = txt.split()
        ip = geocoder.ip(x[1])
        print(ip.city)
        p.sendline(ip.city)
    if i != 49:
        p.recvline()

flag = p.recvlines(2)
print(flag)
