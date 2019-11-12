def MergeSort(a):
    n = len(a)
    if n < 2:
        return(a)
    m = len(a) // 2
    return Merge(MergeSort(a[0:m]), MergeSort(a[m:]))


def Merge(l, r):
    res = []
    i = 0
    j = 0
    while (i < len(l) and j < len(r)):
        if (l[i] > r[j]):
            res.append(r[j])
            j += 1
            continue
        if (l[i] == r[j]):
            res.append(l[i])
            res.append(r[j])
            j += 1
            i += 1
            continue
        else:
            res.append(l[i])
            i += 1
            continue
    if (i == len(l)):
        for j in range(j, len(r), 1): #один из массивов закончился, циклом забираем оставшийся.
            res.append(r[j])
    else:
        for i in range(i, len(l), 1):
            res.append(l[i])
    return(res)


a = [10,8,6,2,4,5]
a = MergeSort(a)
print(a)
