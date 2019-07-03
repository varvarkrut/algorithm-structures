def MergeSort(a):
    n=len(a)
    if n<2:
        return(a)
        print('hi')
    m=len(a)//2
    return Merge(MergeSort(a[0:m]),MergeSort(a[m:]))

def Merge(l,r):
    res=[]
    i=0
    j=0
    while i<len(l) or j<len(r):
        if  i == len(l):
            res.append(r[j])
            j += 1
        elif j == len(r):
            res.append(l[i])
            i += 1
        elif l[i]>r[j]:
            res.append(r[j])
            j=j+1
        elif r[j]>l[i]:
            res.append(l[i])
            i=i+1
    return(res)


a=[-5,3,1,4,8,5,0,-3]
a=MergeSort(a)
print(a)
