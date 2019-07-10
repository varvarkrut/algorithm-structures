a = [7, 2, 1, 3, 8, 4, 9, 1, 2, 6, 5, 9, 3, 8, 1]
b = a.copy()
prev = a.copy()
for i in range(0, len(a)):
    b[i] = 1
    prev[i] = -1
    for j in range(0, i):
        try:
            if a[j] < a[i] and b[j] + 1 > b[i]:
                b[i] = b[j] + 1
                prev[i] = j
        except:
            pass
ans = 0
for i in range(0, len(a)):
    if ans < b[i]:
        ans = b[i]

    elif ans >= b[i]:
        ans = ans

l = []
j = 0
for i in range(len(b)):
    if b[i] == ans:
        j = i
        '''break'''
l.append(a[j])
for i in reversed(range(len(b))):
    if a[i] < a[j] and b[i] + 1 == b[j]:
        l.append(a[i])
        j=i
print(l)
