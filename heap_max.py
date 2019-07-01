#the main idea of this code- you must  add element to a heap  with "-".For that i wrote a function 'invert_list'
def invert_list(a):
	for i in range(len(a)):
		a[i]=a[i]*-1


def shuffle(i):
	while (i>1) and (a[i//2]>a[i]):
		x=a[i]
		a[i]=a[i//2]
		a[i//2]=x
		i=i//2
def insert(a,n):
	a.append(n)
	shuffle(len(a)-1)
def peek_max(a):
	print('max',abs(a[0]))

def shuffle_down(i):
	j=0
	n=len(a)-1
	while (2*i<=n):
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
		
def ex_max():
	print('remove max.element')
	a[0]=a[len(a)-1]
	a.pop(len(a)-1)
	shuffle_down(0)




if __name__=='__main__':
	a=[5,4,3,2,1]
	print(a)
	invert_list(a)
	peek_max(a)
	ex_max()
	peek_max(a)
