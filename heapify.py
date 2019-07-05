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
            
a=[0,15,21,-3,5,-10,-17]
for i in range(0,len(a)):
    print(a,a[i])
    shuffle(a,i)
