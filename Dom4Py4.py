# 4) Определить позицию второго вхождения строки в списке либо сообщить, что её нет.

s = ["ee", "dh", "rt", "dh"]
try:
    ind = s.index("dh")
except ValueError:
    ind = -1
    print(ind)
else:
    del s[:ind + 1]
    ind2 = s.index("dh")
    print(ind2 + 1)
