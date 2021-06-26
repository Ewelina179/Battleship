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
    lst2=[]
    lst2.append([a for a in range(col-1, -1, -1)])
    lst2.append([b for b in range(row-1, -1, -1)])
    lstt=[]
    for i in zip(lst2[0],lst2[1]):
        k=list(i)
        lstt.append(k)
    return lstt

x=diagonal1(2,2)
y=diagonal2(2,2)
diagonals=x+y
#print(diagonals)
#losowe współrzędne:
col=6
row=6
def rand_coord(x,y):
    rand_row=random.randint(0, x-1)
    rand_col=random.randint(0, y-1)
    lst=[rand_row, rand_col]
    return lst
print(rand_coord(col, row))
mylist=iter([x for x in diagonals])
x=next(mylist, rand_coord(col, row))
print(x)


