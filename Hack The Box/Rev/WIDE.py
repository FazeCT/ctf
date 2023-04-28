data = 'HOt*\x1f\xe8\xcf\x8e\x87\x80{Xt\x0e\x1c\xa3\xee\xf8\x950ANe\x0b\xb9\xd8'
print(''.join(chr(ord(data[i]) ^ (27 * i % 255)) for i in range(len(data))))
