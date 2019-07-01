from operator import itemgetter

# создаю список из букв и частоты их вхождения
s = input()
l = []
d={}
d2={}
for i in s:
    if [i, s.count(i)] not in l:
        l.append([i, s.count(i)])
if len(l) > 1: # если слово состоит не из одной буквы
        # делаю копию списка и сортирую по частоте
    l.sort(key=itemgetter(1))
    l1 = l.copy()
    i=1
    while len(l1)>1:
        d[l1[0][0]]=[0,i]
        d[l1[1][0]]=[1,i]
        l1.append([i,l1[0][1]+l1[1][1]])
        for j in range(2): l1.pop(0)
        l1.sort(key=itemgetter(1))
        i=i+1
    par=0
    for i in range(len(l)):
        val=l[i][0]
        par=d[val][1]
        answer=str(d[val][0])
        while par in d:
            answer=str(d[par][0])+answer
            par=d[par][1]
        d2[val]=answer
else:
    d2[l[0][0]]='0'
a=''
for i in s:
    a=a+(d2[i])
print(len(l),len(a))
for i in list(reversed(l)):
    a=i[0]
    b=d2[a]
    print(a,b)
for i in s:
    i=d2[i]
    print(i,end='')