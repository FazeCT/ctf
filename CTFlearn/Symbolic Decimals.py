#Made by FazeCT

data = "^&,*$,&),!@#,*#,!!^,(&,!!$,(%,$^,(%,*&,(&,!!$,!!%,(%,$^,(%,&),!!!,!!$,(%,$^,(%,&^,!)%,!)@,!)!,!@%"
alphabet = "!@#$%^&*()"

real_data = ""
for i in data:
    if i == ',':
        real_data += ' '
    else:
        real_data += str((alphabet.index(i) + 1) % 10)

list = real_data.split()
for i in list:
    print(chr(int(i)),end='')



