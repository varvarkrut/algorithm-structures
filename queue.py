class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def maxpush(self, item):
        if self.isEmpty()==True:
            self.items.append([item,item])
        else:
            if self.peek()[1]<item:
                self.items.append([item,item])
            else:
                self.items.append([item,self.peek()[1]])
    def maxpush2(self, item):
        if self.isEmpty()==True:
            self.items.append([item[0],item[0]])
        else:
            if self.peek()[1]<item[0]:
                self.items.append([item[0],item[0]])
            else:
                self.items.append([item[0],self.peek()[1]])



    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

def IsBalanced(c,m):
    if m==1:
        for i in range(len(c)):
            print(c[i],end=" ")
        return
    a = Stack()
    b = Stack()
    d=[]
    for i in range(0,m-1):
        a.maxpush(c[i])
    for i in range(m-1,len(c)):
        if (b.isEmpty()==True):
            for j in range(m-1):
                b.maxpush2(a.pop())
        a.maxpush(c[i])
        d.append(max(a.peek()[1],b.peek()[1]))
        b.pop()
    if len(d)==1:
        print(d[0])
    else:
        for i in d:
            print(i,end=" ")






l=input()
c=input()
c=c.split(' ')
for i in range(len(c)):
    c[i]=int(c[i])
m=int(input())
if m==1:
    for i in range(len(c)):
        print(c[i],end=" ")

else:
    IsBalanced(c,m)
