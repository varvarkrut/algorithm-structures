a=[2,2,1,1,1,3,1]
b=[0,0,0]
a1=[0,0,0,0,0,0,0]
for j in range(0,len(a)):
    b[a[j]-1]=b[a[j]-1]+1
for i in range(1,len(b)):
    b[i]=b[i]+b[i-1]
print(b)
for j in reversed(range(0,len(a))):
    print('a=',a,'j=',j,'a[j]=',a[j],'b=',b,'a1=',a1)
    a1[b[a[j]-1]-1]=a[j]
    b[a[j]-1]=b[a[j]-1]-1

print(a1)
