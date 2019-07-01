def invert_a(a):
	for i in range(len(a)):
		a[i]=a[i]*-1



def shake_up(i):
	while (i>0) and (a[i//2]>a[i]):
		x=a[i]
		a[i]=a[i//2]
		a[i//2]=x
		i=i//2
def insert(a,n):
	n*=-1
	a.append(n)

	shake_up(len(a)-1)
def peek_max(a):
	print('max',abs(a[0]))

def shake_down(i):
	j=0
	n=len(a)-1
	while (2*i<=n):
		j=i
		if (a[2*i])<a[j]:
			j=2*i
		if (2*i+1<=n) and (a[(2*i)+1]<a[j]):
			j=(2*i)+1
		if i==j:
			break


		x=a[i]
		a[i]=a[j]
		a[j]=x
		i=j
		
def ex_max():
	print('remove max.element')
	a[0]=a[len(a)-1]
	a.pop(len(a)-1)
	shake_down(0)




if __name__=='__main__':
	a=[]
	insert(a,200)
	insert(a,10)
	peek_max(a)
	insert(a,5)
	insert(a,500)
	insert(a,-3)
	insert(a,100000)
	invert_a(a)
	print(a)
	peek_max(a)
