def QuickSort(a, l, r):
    if l >= r:
        return
    m = Partition(a, l, r)
    if len(m)==1:
        QuickSort(a, l, m[0])
        QuickSort(a, m[0]+1, r)
    elif len(m)==2:
        QuickSort(a, l, m[0])
        QuickSort(a, m[0]+m[1]+1, r)


def Partition(a, l, r):
    x = a[l]
    j = l
    m=0
    res=[]
    for i in range(l + 1, r):
        if a[i] < x:
            j = j + 1
            a[j], a[i] = a[i], a[j]
        if a[i]==x:
            m=j+1
            a[m],a[i]=a[m],a[i]
    a[l], a[j] = a[j], a[l]
    if m==0:
        res.append(j)
        return res
    else:
        res.append(j)
        res.append(m)
        return res

import time
start_time = time.time()
a = [5]*500
a.append(0)
a.append(-3)
QuickSort(a, 0, len(a))
print(a)
print("--- %s seconds ---" % (time.time() - start_time))
