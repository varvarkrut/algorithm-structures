import math
import bisect


def initialization():
    results = []
    n = int(input())
    results.append(n)
    a = input()
    a = a.split(' ')
    for i in range(n):
        a[i] = int(a[i])
    results.append(a)
    return results


def maxlen(b, lenb):
    ans = 0
    for i in range(lenb):
        if i + 1 < lenb - 1:
            if b[i + 1] != math.inf:
                ans += 1
    return ans


def sequence_recovery(a, len_of_subs, prev, prevA):
    print(a[prev[len_of_subs]], end=" ")
    initin = prevA[prev[len_of_subs]]
    while initin != math.inf:
        print(a[initin], end=" ")
        initin = prevA[initin]


def main():
    prev = []
    prevA = []
    aftinit = initialization()
    a = aftinit[1]
    n = aftinit[0]
    b = [math.inf] * (n + 1)
    prev = [math.inf] * (n + 1)
    prevA = [math.inf] * n
    b[0] = -1
    for i in range(n):
        j = bisect.bisect_right(b, a[i])
        if (b[j - 1]) < a[i] and a[i] < b[j]:
            b[j] = a[i]
            prev[j] = i
            prevA[i] = prev[j - 1]
    sublen = (maxlen(b, n))
    sequence_recovery(a,sublen,prev,prevA)


main()
