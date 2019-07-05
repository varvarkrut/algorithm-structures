from heapq import heappop,heappush



def HeapSort(a):
    n=len(a)
    h=[]
    a1=[]
    for i in range(0,n):
        heappush(h,a[i])
    for i in range(0,n):
        a1.append(heappop(h))
    return(a1)
a=[0,3,5,1,-10,-20]

a=HeapSort(a)

print(a)
