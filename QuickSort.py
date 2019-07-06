def QuickSort(a, l, r):
    if l >= r:
        return 
    m = Partition(a, l, r)
    QuickSort(a, l, m)
    QuickSort(a, m+1, r)


def Partition(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r):
        '''print('x=',x,'a=',a,'a[i]=',a[i])'''
        if a[i] <= x:
            j = j + 1
            a[j], a[i] = a[i], a[j]
    a[l], a[j] = a[j], a[l]
    '''print('a=',a)'''
    return j


a = [0, -5, -3, -2, 1, 10, -30, -2, 7, 11, -23,-5]
QuickSort(a, 0, len(a))
print(a)
