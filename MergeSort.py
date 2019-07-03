z = 0


def MergeSort(a):
    n = len(a)
    if n < 2:
        return(a)
    m = len(a) // 2
    return Merge(MergeSort(a[0:m]), MergeSort(a[m:]))


def Merge(l, r):
    global z
    res = []
    i = 0
    j = 0
    while i < len(l) or j < len(r):
        if i == len(l):
            res.append(r[j])
            j += 1
        elif j == len(r):
            res.append(l[i])
            i += 1
        elif l[i] >= r[j]:
            if len(l) > 1:
                if l[i] == r[j] and l[i + 1] > r[j]:
                    z += (len(l) - (i + 1))
            if l[i] > r[j]:
                z += len(l) - i
            res.append(r[j])
            j = j + 1
        elif r[j] > l[i]:
            res.append(l[i])
            i = i + 1
    return(res)

print('Ввведите числа массива через пробел')
a = input()
a = a.split()

for i in range(len(a)):
    a[i] = int(a[i])
a = MergeSort(a)
print(a)
print('количество инверсий в заданном массиве:', z)
