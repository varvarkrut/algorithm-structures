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
        print('item=',item)
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

def IsBalanced(c):
    a = Stack()
    b = Stack()
    d=[]
    m=12
    for i in range(0,m-1):
        a.maxpush(c[i])
    print(a.items)
    for i in range(m-1,len(c)):
        if (b.isEmpty()==True):
            for j in range(m-1):
                b.maxpush2(a.pop())
            print(b.items)
        a.maxpush(c[i])
        print('a[items]=',a.items)
        print('b[items]=',b.items)
        d.append(max(a.peek()[1],b.peek()[1]))
        print('d=',d)
        b.pop()
    if len(d)==1:
        print(d[0])






c=[28,7,64,40,68,86,80,93,4,53,32,56,68,18,59]
IsBalanced(c)
