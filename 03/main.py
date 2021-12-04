import datetime
a = input()
a = datetime.datetime(int(a.split('/')[2]), int(a.split('/')[1]), int(a.split('/')[0]))
b = input()
b = datetime.datetime(int(b.split('/')[2]), int(b.split('/')[1]), int(b.split('/')[0]))
delta = a - b
print("Il y a :", int(abs(delta.seconds + delta.days*24*3600)), "secondes entre ces deux dates")