def QuickSort(a, l, r):
    if l >= r:
        return
    z = Partition(a, l, r)
    m = z[0]
    d = z[1]
    QuickSort(a, l, m)
    l=d


def Partition(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r):
        if a[i] < x:
            j = j + 1
            a[j], a[i] = a[i], a[j]
    a[l], a[j] = a[j], a[l]
    '''print('a before',a,'j=',j)'''

    if j < r:
        k = j
        for i in range(j + 1, r):
            if a[i] == a[j]:
                k = k + 1
                a[k], a[i] = a[i], a[k]
        '''print(a)
        print('j=',j,'k=',k)'''
        return (j, k + 1)



import time
start_time = time.time()
a = [5,0,2,4,6,5,5,-100,-500,500,3000,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
QuickSort(a, 0, len(a))
print(a)
print("--- %s seconds ---" % (time.time() - start_time))
