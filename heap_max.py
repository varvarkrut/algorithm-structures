#the main idea of this code- you must  add element to a heap  with "-".


a=[-5,-4,-3,-2,-1]

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
def peek_max(a):
	print(abs(a[0]))

def shuffle_down(i):
	print('heap',i,a[i])
	j=0
	n=len(a)-1
	while (2*i<=n):
		print('heap2',a[i])
		j=i
		if abs((a[2*i])<abs(a[j])):
			j=2*i
		if abs((2*i+1<=n)) and abs((a[(2*i)+1]<a[j])):
			j=(2*i)+1
		if i==j:
			break


		x=a[i]
		a[i]=a[j]
		a[j]=x
		i=j
		
def ex_min():
	a[0]=a[len(a)-1]
	a.pop(len(a)-1)
	shuffle_down(0)


peek_max(a)
ex_min()
print(a)
peek_max(a)
