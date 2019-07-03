print('Введите изначальный массив через пробел, затем массив ключей. \nЕсли ключ есть- вернется его индекс в массиве\nЕсли ключа нет- вернется -1')
a = input()
b = input()
a = a.split()
b = b.split()
for i in range(len(a)):
    a[i] = int(a[i])
a.sort()


for i in range(len(b)):
    b[i] = int(b[i])


def sort1(a,k):
    z=True
    l=0
    r=len(a)-1
    while l<=r:
        m=(r+l)//2
        if a[m]==k:
            print(m+1,end=" ")
            z=False
            break
        if a[m]>k:
            r=m-1
        else:
            l=m+1
    if z==True:
        print(-1,end=" ")
for i in range(len(b)):
    sort1(a,b[i])
