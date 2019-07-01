a=[1,10,15,20,13,16,19]
x=0
def shuffle(i):
	print(a[i//2]>a[i])
	while (i>1) and (a[i//2]>a[i]):
		print(i)
		print(a[i],a[i//2])
		x=a[i]
		a[i]=a[i//2]
		a[i//2]=x
		print(a[i],a[i//2])
		i=i//2
def insert(a,n):
	a.append(n)
	print(a)
	print(a[len(a)-1])
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



ex_min()
print(a)