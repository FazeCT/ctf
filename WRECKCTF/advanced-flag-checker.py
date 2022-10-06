d = ""

d += bytes.fromhex(hex(89703644 ^ 1647945914)[2:]).decode('utf-8')[::-1]
d += bytes.fromhex(hex(1896877211 ^ 25126112)[2:]).decode('utf-8')[::-1]
d += bytes.fromhex(hex(3460111838 ^ -1589361989 & (2**32-1))[2:]).decode('utf-8')[::-1]
d += bytes.fromhex(hex(841570556 ^ 1096550281)[2:]).decode('utf-8')[::-1]
d += bytes.fromhex(hex(2361298766 ^ -152966357 & (2**32-1))[2:]).decode('utf-8')[::-1]
d += bytes.fromhex(hex(2974431051 ^ -567515016 & (2**32-1))[2:]).decode('utf-8')[::-1]
d += bytes.fromhex(hex(250179706 ^ 1721577224)[2:]).decode('utf-8')[::-1]
d += bytes.fromhex(hex(4186823992 ^ -925716911 & (2**32-1))[2:]).decode('utf-8')[::-1]
d += bytes.fromhex(hex(1567711053 ^ 1813145471)[2:]).decode('utf-8')[::-1]
d += bytes.fromhex(hex(1091280784 ^ 1010629539)[2:]).decode('utf-8')[::-1]

print(d)
