def shuffle(a,i):
    if i%2==1:
        while (i>0) and (a[i//2]>a[i]):
            print('chet')
            print(a[i//2],a[i])
            a[i],a[i//2]=a[i//2],a[i]
            i=i//2
    elif i%2==0:
        print('here')
        print(a[i-1//2],a[i],i)
        while (i>0) and (a[(i-1)//2]>a[i]):
            print('nechet')
            a[i],a[(i-1)//2]=a[(i-1)//2],a[i]
            i=(i-1)//2




def insert(a,n):
    a.append(n)
    shuffle(len(a)-1)
def peek_min(a):
    print(a[0])

def shuffle_down(i):
    j=0
    n=len(a)-1
    while (2*i<=n):
        j=i
        if (a[2*i]<a[j]):
            j=2*i
        if (2*i+1<=n) and (a[(2*i)+1]<a[j]):
            j=(2*i)+1
        if i==j:
            break
        x=a[i]
        a[i]=a[j]
        a[j]=x
        i=j
        
def ex_min():
    print(a[0])
    a[0]=a[len(a)-1]
    a.pop(len(a)-1)
    shuffle_down(0)
