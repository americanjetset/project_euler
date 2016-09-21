f = open('matrix1.txt')
M = []
for row in f:
    M += [row.strip().split(',')]
f.close()
for r in range(0,len(M[0])):
    for c in range(0,len(M[0])):
        M[r][c] = int(M[r][c])

i
