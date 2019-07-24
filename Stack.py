class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)



def IsBalanced(b):
    a = Stack()
    for char in range(len(b)):
        if b[char] == '[' or b[char] == '(' or b[char] == '{':
            a.push(char)
        elif b[char] == ']' or b[char] == ')' or b[char] == '}':
            if a.isEmpty():
                return(char+1)
            top = b[a.pop()]
            if (top == '[' and b[char] != ']') or (top == '(' and b[char] != ')') or (top == '{' and b[char] != '}'):
                return(char+1)
    if a.isEmpty() == True:
        return('Success')
    else:
        return(a.pop()+1)

b=str(input())

print(IsBalanced(b))
