from operator import itemgetter

# создаю список из букв и частоты их вхождения
s = input()
sp1 = []
sl2 = {}
for i in s:
    if [i, s.count(i)] not in sp1:
        sp1.append([i, s.count(i)])
if len(sp1) > 1: # если слово состоит не из одной буквы
    # делаю копию списка и сортирую по частоте
    sp = sp1.copy()
    sp.sort(key=itemgetter(1))
    # создаю словарь {буква: код(0 или 1), номер родительского узла}
    # удаляю первые две буквы из списка, добавляю узел с частотой, равной сумме частот этих букв
    # сортирую список заново
    sl = {}
    i = 1
    while len(sp) > 1:
        sl[sp[0][0]] = [0, i]
        sl[sp[1][0]] = [1, i]
        sp.append([i, sp[0][1] + sp[1][1]])
        for j in range(2): sp.pop(0)
        sp.sort(key=itemgetter(1))
        i += 1
    # создаю второй словарь {буква: ее код(напр. 1010)}
    for i in range(len(sp1)):
        ch = sp1[i][0]
        uz = sl[ch][1]
        kod = str(sl[ch][0])
        while uz in sl:
            kod = str(sl[uz][0]) + kod
            uz = sl[uz][1]
        sl2[ch] = kod

elif len(sp1) == 1: # если слово из одной буквы
    sl2[sp1[0][0]] = '0'

# вывод результатов на печать
s2 = ''
for i in s:
    s2 += sl2[i]
print(len(sp1), len(s2))
for ch, kod in sl2.items():
    print("{0}: {1}".format(ch, kod))
print(s2)
