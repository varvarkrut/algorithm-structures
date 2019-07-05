def heapify(a):
    def sift_down(a, i):
        n = len(a) - 1
        j = 0
        while ((2 * i) + 1 <= n):
            j = i
            if (a[(2 * i) + 1] > a[j]):
                j = (2 * i) + 1
            if ((2 * i) + 2 <= n) and (a[(2 * i) + 2] > a[j]):
                j = (2 * i) + 2
            if i == j:
                break
            a[i], a[j] = a[j], a[i]
            i = j
    for i in reversed(range(0, len(a))):
        sift_down(a, i)


def HeapSort(a):
    def sift_down(a, i, size):
        n = size
        j = 0
        while ((2 * i) + 1 <= n):
            j = i
            if (a[(2 * i) + 1] > a[j]):
                j = (2 * i) + 1
            if ((2 * i) + 2 <= n) and (a[(2 * i) + 2] > a[j]):
                j = (2 * i) + 2
            if i == j:
                break
            a[i], a[j] = a[j], a[i]
            i = j
    print(a)
    n = len(a) - 1
    size = n
    for i in reversed(range(0, n)):
        a[size], a[0] = a[0], a[size]
        size = size - 1
        sift_down(a, 0, size)


a = [0, 15, 21, -3, 5, -10, -17, -12, -25, -100]
heapify(a)
HeapSort(a)
print(a)
