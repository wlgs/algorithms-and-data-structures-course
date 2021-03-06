from collections import deque


# normalnie o(n^3)

def cycle4(G):
    n = len(G)
    A = [[0] * n for _ in range(n)]
    neigh = [deque() for _ in range(n)]
    vertex = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if G[i][j] == 1:
                neigh[i].append(j)

    for i in range(n):
        # print("entering with:", i)
        while len(neigh[i]) >= 2:  # normalnie sprawdz wszystkie pary, tu jest źle
            j = neigh[i].pop()
            k = neigh[i].pop()
            # print(j, k)
            if A[j][k] == 0:
                A[j][k] = 1
                vertex[j][k] = i
            else:
                # print(i, j, k)
                # for e in A:
                #     print(e)
                print("the cycle is:", k, i, j, vertex[j][k])
        # for e in A:
        #     print(e)


G1 = [[0, 1, 0, 0, 0],
      [1, 0, 1, 0, 1],
      [0, 1, 0, 1, 0],
      [0, 0, 1, 0, 1],
      [0, 1, 0, 1, 0]]
#      0  1  2  3  4  5  6
G2 = [[0, 1, 1, 0, 0, 0, 0],
      [1, 0, 1, 0, 0, 0, 0],
      [1, 1, 0, 0, 0, 0, 0],
      [0, 0, 1, 0, 1, 1, 1],
      [0, 0, 0, 1, 0, 1, 0],
      [0, 0, 0, 0, 1, 0, 1],
      [0, 0, 0, 1, 0, 1, 0]]

#      0  1  2  3  4  5  6
G3 = [[0, 1, 1, 0, 0, 0, 0],
      [1, 0, 1, 0, 0, 0, 0],
      [1, 1, 0, 0, 0, 0, 0],
      [0, 0, 1, 0, 1, 1, 0],
      [0, 0, 0, 1, 0, 1, 0],
      [0, 0, 0, 0, 1, 0, 1],
      [0, 0, 0, 0, 0, 1, 0]]

#      0  1  2  3  4  5  6
G4 = [[0, 1, 1, 0, 0, 0, 0],
      [1, 0, 1, 1, 0, 0, 0],
      [1, 1, 0, 0, 0, 0, 0],
      [0, 1, 1, 0, 1, 1, 0],
      [0, 0, 0, 1, 0, 1, 0],
      [0, 0, 0, 0, 1, 0, 1],
      [0, 0, 0, 0, 0, 1, 0]]
#      0  1  2  3  4
G5 = [[0, 0, 0, 0, 0],
      [0, 0, 1, 0, 1],
      [0, 1, 0, 1, 0],
      [0, 0, 1, 0, 1],
      [0, 1, 0, 1, 0]]

G6 = [[0, 1, 0, 0, 0, 0, 1, 1],
      [1, 0, 0, 1, 0, 1, 0, 0],
      [0, 0, 0, 0, 0, 0, 1, 0],
      [0, 1, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 1, 0, 0],
      [1, 0, 0, 0, 0, 0, 0, 0], ]

cycle4(G6)
