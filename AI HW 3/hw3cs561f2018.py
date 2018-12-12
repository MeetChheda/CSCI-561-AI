import numpy as np
import copy
import math
from collections import defaultdict
def input1():
    global fin
    fin = open("input0.txt", "r")
    files = fin.readlines()
    loc_of_obstacle_x, loc_of_obstacle_y, loc_of_obstacle = [], [], []
    start_loc_car = []
    end_loc_car = []
    grid_size = int(files[0].strip())
    grid = np.zeros((grid_size,grid_size), dtype=int)
    for i in range (0, grid_size):
        for j in range (0, grid_size):
            grid[i][j] = -1
    no_of_cars = int(files[1].strip())
    no_of_obstacles = int(files[2].strip())
    for i, line in enumerate(files):
        if(i>2 and i<(3+no_of_obstacles)):
            loc_of_obstacle.append(list((line[0].rstrip()+line[2].rstrip())))
            loc_of_obstacle_x.append(line[0].rstrip())
            loc_of_obstacle_y.append(line[2].rstrip())
        a = 3+no_of_obstacles
        if(i>=a and i<(a+no_of_cars)):
            start_loc_car.append(list((line[2].rstrip()+line[0].rstrip())))
        b = a+no_of_cars
        if(i>=b and i<(b+no_of_cars)):
            end_loc_car.append(list((line[2].rstrip()+line[0].rstrip())))
        c = b+no_of_cars
    for i in range (0,len(loc_of_obstacle_x)):
        grid[int(loc_of_obstacle_y[i])][int(loc_of_obstacle_x[i])] -= 100
    return grid_size, no_of_cars, no_of_obstacles,grid, loc_of_obstacle, start_loc_car, end_loc_car



def utility(grid, end_loc_car, grid_size):
    util, utildash = [], []
    Rs = [[0.0 for j in range (grid_size)]for i in range (grid_size)]
    for i in range(0, len(grid)):
        for j in range (0, len(grid)):
            Rs[i][j] = grid[i][j]
    util = copy.deepcopy(Rs)
    utildash = copy.deepcopy(Rs)
    a = [0, 0]
    policy = defaultdict()
    while (True):
        delt = 0
        util = copy.deepcopy(utildash)
        for i in range (0, len(Rs)):
            for j in range (0, len(Rs)):
                if ((i is int(end_loc_car[0])) and (j is int(end_loc_car[1]))):
                    continue
                elif (i == 0 and j == 0):
                    u = float((0.7*util[i][j])+(0.1*util[i+1][j])+(0.1*util[i][j])+(0.1*util[i][j+1]))
                    d = float((0.1*util[i][j])+(0.7*util[i+1][j])+(0.1*util[i][j])+(0.1*util[i][j+1]))
                    l = float((0.1*util[i][j])+(0.1*util[i+1][j])+(0.7*util[i][j])+(0.1*util[i][j+1]))
                    r = float((0.1*util[i][j])+(0.1*util[i+1][j])+(0.1*util[i][j])+(0.7*util[i][j+1]))
                elif(i == 0 and j == len(Rs)-1):
                    u = float((0.7*util[i][j])+(0.1*util[i+1][j])+(0.1*util[i][j-1])+(0.1*util[i][j]))
                    d = float((0.1*util[i][j])+(0.7*util[i+1][j])+(0.1*util[i][j-1])+(0.1*util[i][j]))
                    l = float((0.1*util[i][j])+(0.1*util[i+1][j])+(0.7*util[i][j-1])+(0.1*util[i][j]))
                    r = float((0.1*util[i][j])+(0.1*util[i+1][j])+(0.1*util[i][j-1])+(0.7*util[i][j]))
                elif(i == len(Rs)-1 and j == 0):
                    u = float((0.7*util[i-1][j])+(0.1*util[i][j])+(0.1*util[i][j])+(0.1*util[i][j+1]))
                    d = float((0.1*util[i-1][j])+(0.7*util[i][j])+(0.1*util[i][j])+(0.1*util[i][j+1]))
                    l = float((0.1*util[i-1][j])+(0.1*util[i][j])+(0.7*util[i][j])+(0.1*util[i][j+1]))
                    r = float((0.1*util[i-1][j])+(0.1*util[i][j])+(0.1*util[i][j])+(0.7*util[i][j+1]))
                elif(i == len(Rs)-1 and j == len(Rs)-1):
                    u = float((0.7*util[i-1][j])+(0.1*util[i][j])+(0.1*util[i][j-1])+(0.1*util[i][j]))
                    d = float((0.1*util[i-1][j])+(0.7*util[i][j])+(0.1*util[i][j-1])+(0.1*util[i][j]))
                    l = float((0.1*util[i-1][j])+(0.1*util[i][j])+(0.7*util[i][j-1])+(0.1*util[i][j]))
                    r = float((0.1*util[i-1][j])+(0.1*util[i][j])+(0.1*util[i][j-1])+(0.7*util[i][j]))
                elif(i == 0):
                    u = float((0.7*util[i][j])+(0.1*util[i+1][j])+(0.1*util[i][j-1])+(0.1*util[i][j+1]))
                    d = float((0.1*util[i][j])+(0.7*util[i+1][j])+(0.1*util[i][j-1])+(0.1*util[i][j+1]))
                    l = float((0.1*util[i][j])+(0.1*util[i+1][j])+(0.7*util[i][j-1])+(0.1*util[i][j+1]))
                    r = float((0.1*util[i][j])+(0.1*util[i+1][j])+(0.1*util[i][j-1])+(0.7*util[i][j+1]))
                elif(j == 0):
                    u = float((0.7*util[i-1][j])+(0.1*util[i+1][j])+(0.1*util[i][j])+(0.1*util[i][j+1]))
                    d = float((0.1*util[i-1][j])+(0.7*util[i+1][j])+(0.1*util[i][j])+(0.1*util[i][j+1]))
                    l = float((0.1*util[i-1][j])+(0.1*util[i+1][j])+(0.7*util[i][j])+(0.1*util[i][j+1]))
                    r = float((0.1*util[i-1][j])+(0.1*util[i+1][j])+(0.1*util[i][j])+(0.7*util[i][j+1]))
                elif(i == len(Rs)-1):
                    u = float((0.7*util[i-1][j])+(0.1*util[i][j])+(0.1*util[i][j-1])+(0.1*util[i][j+1]))
                    d = float((0.1*util[i-1][j])+(0.7*util[i][j])+(0.1*util[i][j-1])+(0.1*util[i][j+1]))
                    l = float((0.1*util[i-1][j])+(0.1*util[i][j])+(0.7*util[i][j-1])+(0.1*util[i][j+1]))
                    r = float((0.1*util[i-1][j])+(0.1*util[i][j])+(0.1*util[i][j-1])+(0.7*util[i][j+1]))
                elif(j == len(Rs)-1):
                    u = float((0.7*util[i-1][j])+(0.1*util[i+1][j])+(0.1*util[i][j-1])+(0.1*util[i][j]))
                    d = float((0.1*util[i-1][j])+(0.7*util[i+1][j])+(0.1*util[i][j-1])+(0.1*util[i][j]))
                    l = float((0.1*util[i-1][j])+(0.1*util[i+1][j])+(0.7*util[i][j-1])+(0.1*util[i][j]))
                    r = float((0.1*util[i-1][j])+(0.1*util[i+1][j])+(0.1*util[i][j-1])+(0.7*util[i][j]))
                else:
                    u = float((0.7*util[i-1][j])+(0.1*util[i+1][j])+(0.1*util[i][j-1])+(0.1*util[i][j+1]))
                    d = float((0.1*util[i-1][j])+(0.7*util[i+1][j])+(0.1*util[i][j-1])+(0.1*util[i][j+1]))
                    l = float((0.1*util[i-1][j])+(0.1*util[i+1][j])+(0.7*util[i][j-1])+(0.1*util[i][j+1]))
                    r = float((0.1*util[i-1][j])+(0.1*util[i+1][j])+(0.1*util[i][j-1])+(0.7*util[i][j+1]))
                best = max(u,d,l,r)
                if (best == r):
                    a[0] = best
                    a[1] = 'right'
                if(best == l):
                    a[0] = best
                    a[1] = 'left'
                if(best == d):
                    a[0] = best
                    a[1] = 'down'
                if(best == u):
                    a[0] = best
                    a[1] = 'up'
                utildash[i][j] = float(Rs[i][j] + 0.9*a[0])
                policy[i,j] = a[1]
                if (abs(utildash[i][j]- util[i][j]) > delt):
                    delt = abs(utildash[i][j]- util[i][j])
        if delt < 0.1 * (0.1) / 0.9:
            return (util,policy)
        
def turn_left(move):
    if(move == 'left'):
        move = 'down'
    elif(move == 'up'):
        move = 'left'
    elif(move == 'down'):
        move = 'right'
    else:
        move = 'up'
    return move

def turn_right(move):
    if(move == 'left'):
        move = 'up'
    elif(move == 'up'):
        move = 'right'
    elif(move == 'down'):
        move = 'left'
    else:
        move = 'down'
    return move

def simulation(p, start_loc_car, end_loc_car, grid):
    endx = int(end_loc_car[0])
    endy = int(end_loc_car[1])
    total = 0
    for j in range (10):
        posx = int(start_loc_car[0])
        posy = int(start_loc_car[1])
        points = 0
        np.random.seed(j)
        swerve = np.random.random_sample(1000000)
        k = 0
        while(posx!=endx or posy!=endy):
            move = p[posx,posy]
            if (swerve[k] > 0.7):
                if (swerve[k] > 0.8):
                    if (swerve[k] > 0.9):
                        move = turn_left(turn_left(move))
                    else:
                        move = turn_right(move)
                else:
                    move = turn_left(move)
            if (move == 'left'):
                if(posy != 0):
                    posy -= 1
            if (move == 'right'):
                if (posy != len(grid)-1):
                    posy += 1
            if (move == 'up'):
                if (posx != 0):
                    posx -= 1
            if (move == 'down'):
                if (posx != len(grid)-1):
                    posx += 1
            k+=1
            points+=grid[posx][posy]
        total += points
    total = math.floor(float(total/10))
    total = int(total)
    return (total)

def city(grid, end_loc_car, start_loc_car, grid_size):
    fout = open("output.txt", "w")
    for i in range (0, len(end_loc_car)):
        grid[int(end_loc_car[i][0])][int(end_loc_car[i][1])] +=100
        util, p = utility(grid, end_loc_car[i], grid_size)
        total = simulation(p,start_loc_car[i],end_loc_car[i], grid)
        fout.write(str(total))
        #print(total)
        fout.write('\n')
        grid[int(end_loc_car[i][0])][int(end_loc_car[i][1])] -=100
    fout.close()
def main():
    grid_size, no_of_cars, no_of_obstacles,grid, loc_of_obstacle, start_loc_car, end_loc_car = input1()
    city(grid,end_loc_car, start_loc_car, grid_size)
main()


