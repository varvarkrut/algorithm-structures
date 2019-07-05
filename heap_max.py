def sift_up(a,i):
    if i%2==1:
        while (i>0) and (a[i//2]<a[i]):
            a[i],a[i//2]=a[i//2],a[i]
            i=i//2
    elif i%2==0:
        while (i>0) and (a[(i-1)//2]<a[i]):
            a[i],a[(i-1)//2]=a[(i-1)//2],a[i]
            i=(i-1)//2




def insert(a,n):
    a.append(n)
    sift_up(len(a)-1)
def peek_max(a):
    print(a[0])

def sift_down(a,i):
    j=0
    n=len(a)-1
    while ((2*i)+1<=n):
        j=i
        if (a[(2*i)+1]>a[j]):
            j=(2*i)+1
        if ((2*i)+2<=n) and (a[(2*i)+2]>a[j]):
            j=(2*i)+2
        if i==j:
            break
        a[i],a[j]=a[j],a[i]
        i=j
        
def ex_max():
    print(a[0])
    a[0]=a[len(a)-1]
    a.pop(len(a)-1)
    sift_down(0)

def heapify(a):
    for i in range(0,len(a)):
        sift_up(a,i)


def heapify2(a):
    for i in reversed(range(0,len(a))):
        sift_down(a,i)




a=[0,15,21,-3,5,-10,-17]


heapify2(a)

print(a)
