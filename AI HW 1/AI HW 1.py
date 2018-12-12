import signal
import time
import timeit
import numpy as np
import itertools

def findMax(pol, r):
    if (pol == p):
        current = 0
        global maximise
        Trans = 0
        Lr = 0
        Ud = 0
        for i, j in itertools.product(range(N), range(N)):
            if city[i][j] == 1:
                current += score[i][j]
                Ud += score[N - i - 1][j]
                Lr += score[i][N - j - 1]
                Trans += score[j][i]
        maximise = max(maximise, current, Trans, Lr, Ud)
        return



    if p - pol <= N - r:
        i = 0
        while i < N:
            if checkSafe(r, i):
                city[r][i] = 1
                if (pol!=p):
                    findMax(pol + 1, r + 1)
                    city[r][i] = 0
            i+=1
        findMax(pol, r + 1)


def checkSafe(r, c):
    xi, yi = 0,0
    while yi < N:
        if city[yi][c] == 1 and yi != r:
            return False
        yi+=1
    while xi < N:
        if city[r][xi] == 1 and xi != c:
            return False
        xi+=1
    
    xi, yi = r, c
    while xi < N and yi >= 0:
        if city[xi][yi] == 1 and xi != r and yi != c:
            return False
        xi += 1
        yi -= 1
    xi, yi = r, c
    while xi >= 0 and yi >= 0:
        if city[xi][yi] == 1 and xi != r and yi != c:
            return False
        xi -= 1
        yi -= 1
    xi, yi = r, c
    while xi < N and yi < N:
        if city[xi][yi] == 1 and xi != r and yi != c:
            return False
        xi += 1
        yi += 1
    xi, yi = r, c
    while xi >= 0 and yi < N:
        if city[xi][yi] == 1 and xi != r and yi != c:
            return False
        xi -= 1
        yi += 1
    return True



def handle(signum, frame):
    global fout
    fout.write(str(maximise))
    exit()

start_time = time.time()
signal.signal(signal.SIGALRM, handle)
signal.alarm(178)

fin = open("input.txt", "r")
fout = open("output.txt", "w")
files = fin.readlines()
N = int(files[0].strip())
score = np.zeros((N,N), dtype=int)
x=[]
p = int(files[1].strip())
for i, line in enumerate(files):
    if (i>2):
        x.append(list((line[0].rstrip()+line[2].rstrip())))
for i in range (0,N):
    for j in range (0,N):
        score[i][j] = x.count([str(i),str(j)])
maximise = -999
city = [[0 for x in range(N)] for x in range(N)]
start_time = timeit.default_timer()
findMax(0, 0)
fout.write(str(maximise))
fout.close()