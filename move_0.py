import random

def diagonal1(col, row):
    lst1=[]
    lst1.append([a for a in range(col-1,-1,-1)])
    lst1.append([b for b in range(0, row)])
    lst=[]
    for i in zip(lst1[0], lst1[1]):
        k=list(i)
        lst.append(k)
    return lst

def diagonal2(col, row):
    lst1=[]
    lst1.append([a for a in range(col-1, -1, -1)])
    lst1.append([b for b in range(row-1, -1, -1)])
    lst=[]
    for i in zip(lst1[0],lst1[1]):
        k=list(i)
        lst.append(k)
    return lst

def rand_coord(x,y):
    rand_row=random.randint(0, x-1)
    rand_col=random.randint(0, y-1)
    lst=[rand_row, rand_col]
    return lst



