def find_path(vertex, parrents):
    path = ""
    try:
        while True:
            path += parrents[int(vertex)]
            vertex = int(parrents[int(vertex)])
    except:
        return path


def print_results(weight, parrents):
    for i in range(len(weight)):
        print("Стоимость пути до вершины " + str(i + 1) +
              " " + "составляет " + str(weight[i]))
    for i in range(1, len(weight)):
        try:
            path = parrents[i]
        except:
            continue
        print("Как добраться в вершину" + " " + str(i) + ": " + str(path))


def Dijkstra(N, S, matrix):
    validvertex = [True] * N
    weight = [500] * N
    weight[S] = 0
    currentid = 0
    parrents = {}
    for i in range(N):
        weightmin = 500
        for j in range(N):
            if (validvertex[j] and weight[j] < weightmin):
                weightmin = weight[j]
                currentid = j
        for j in range(N):
            if (matrix[currentid][j] + weight[currentid] < weight[j]):
                weight[j] = (matrix[currentid][j] + weight[currentid])
                path = find_path(currentid, parrents)
                parrents[j] = path + "->" + str(currentid)
        validvertex[currentid] = False
    results = []
    results.append(weight)
    results.append(parrents)
    return results


def datainput():
    matrix = [[0, 2, 500, 3, 500, 500], [500, 0, 1, 500, 4, 500], [500, 500, 0, 500, 500, 5], [
        500, 500, 500, 0, 2, 500], [500, 500, 500, 500, 0, 1], [500, 500, 500, 500, 500, 0]]
    buf = []
    print('Введите количество вершин графа')
    sizematrix = int(input())
    '''print('Введите матрицу достижимости')
    for i in range(sizematrix):
        buf = input()
        buf = buf.split()
        matrix.append(list(map(int, buf)))'''
    print('Задайте вершину')
    SVertex = int(input())
    SVertex = SVertex - 1
    results = Dijkstra(sizematrix, SVertex, matrix)
    weight = results[0]
    parrents = results[1]
    print_results(weight, parrents)


datainput()
