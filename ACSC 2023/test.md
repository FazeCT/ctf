# ACSC 2023
## ngo

## Information
**Category** | **Points** | **Writeup Author**
--- | --- | ---
Reverse Engineering | 120 | Onirique

**Description:** 

https://www.youtube.com/watch?v=R0JWMtr7oDw

## Solution

I tried to run ngo.exe, but it just gave me 7 first characters of the flag.

Load this in IDA, looking for the function that print out the flag.

```c
__int64 sub_14000161F()
{
  unsigned __int64 j; // [rsp+28h] [rbp-18h]
  char v2; // [rsp+33h] [rbp-Dh]
  int i; // [rsp+34h] [rbp-Ch]
  unsigned __int64 v4; // [rsp+38h] [rbp-8h]

  sub_140001780();
  sub_1400015E2("The flag is \"ACSC{");
  v4 = 1i64;
  for ( i = 0; i <= 11; ++i )
  {
    for ( j = 0i64; j < v4; ++j )
      v2 = sub_140001550();
    sub_14000159C((unsigned int)(char)(v2 ^ byte_140008010[i]));
    v4 *= 42i64;
  }
  sub_1400015E2("}\".\n");
  return 0i64;
}
```

I then re-wrote in Python like so:

```python
key = 0x3D2964F0
for j in range(round):
    key = (key >> 1) ^ (-(key & 1) & 0x80200003)
print(key)
```

This is not impossible to run through, because until the last character is printed out, the for loop will have to run for approximately 10 ** 16 times. But then i found out this:

https://github.com/MBorrageiro/Yoda/blob/master/YODA_Project%20(1).pdf 

After some researching, i got to know that every state of the key (from 0x00000000 to 0xFFFFFFFF) has a cycle of 2 ** 32. After modifying the previous Python script, i got the flag.

```python
data = [0x01, 0x19, 0xEF, 0x5A, 0xFA, 0xC8, 0x2E, 0x69, 0x31, 0xD7,
  0x81, 0x21]
key = 0x3D2964F0
cnt = 0
total = 0
print('ACSC{', end='')
for i in data:
    total = pow(42,cnt)
    rnd = total % 0xFFFFFFFF
    for j in range(rnd):
        key = (key >> 1) ^ (-(key & 1) & 0x80200003)
    print(chr((key ^ data[cnt]) & 0xFF),end='')
    cnt += 1
print('}')
```

> Flag is: ACSC{yUhFgRvQ2Afi}
