def InsertionSort(a):
    n=len(a)
    for i in range(0,n):
        j=i
        while j>0 and a[j]<a[j-1]:
            a[j],a[j-1]=a[j-1],a[j]
            j=j-1
            print(a)
    return(a)

a=[3,2,1,5]
a=InsertionSort(a)
print(a)
