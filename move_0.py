col=5
row=5


#def creating move 0
lst1=[]
lst1.append([a for a in range(col-1,-1,-1)])
lst1.append([b for b in range(0, row)])
print(lst1)
lst=[]
for i in zip(lst1[0], lst1[1]):
    k=list(i)
    lst.append(k)
print(lst)

lst2=[]
lst2.append([a for a in range(col-1, -1, -1)])
lst2.append([b for b in range(row-1, -1, -1)])
lstt=[]
for i in zip(lst2[0],lst2[1]):
    k=list(i)
    lstt.append(k)
print(lstt)
#for el in LAST_HIT:
#board.change_to_zatopiony(el[0],el[1])
#