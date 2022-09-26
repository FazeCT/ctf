import base64
d = 'UkZWRFZF'
u = 'WjdaREZrWDNrd2RW'
c = 'OXdZV'
t = 'zR4WTE4d2NsOWpNREJzWDJG'
f = 'elgyTjFZM1Z0WWpOeWZRPT0'
print(base64.b64decode(base64.b64decode(d + u + c + t + f + "==").decode()))
