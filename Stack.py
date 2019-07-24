



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
