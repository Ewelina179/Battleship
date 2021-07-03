import random
from move_0 import diagonal1, diagonal2, rand_coord
from ships import ShipBoard, Ship

def create_board(col, row):
    board=[["0" for col in range(col)] for row in range(row)]
    return board


col=int(input("Podaj szerokość tablicy: "))
row=int(input("Podaj wysokość tablicy: "))

global board_of
board_of=create_board(col,row)

size_of_board=col*row


board=ShipBoard(board_of)

board.show_board(board_of)
#kolejna propozycja ruchu z listy. odczyt z pliku, zakodować i wysłać. o ile już nie padł ruch!!!! uwzględnij to!
      
def find_rest_of_ship(ship):
    ship.form="unfull"
    while True:
        q,w=ship.row, ship.col    
        board.change_to_hit(q,w)
        board.show_board(board_of)
        global LAST_HIT
        LAST_HIT=[]
        LAST_HIT.append([q,w])
        LAST_HIT=[[q,w]]    
        for el in LAST_HIT: 
            for method in range(0,4):
                print("Lista trafionych współrzędnych" + str(LAST_HIT))
                lst_of_methods=[ship.south_move(el[0], el[1]), ship.east_move(el[0], el[1]), ship.north_move(el[0], el[1]), ship.west_move(el[0], el[1])]
            
                x=int(lst_of_methods[method][0]) 
                y=int(lst_of_methods[method][1])

                if board.is_empty(x,y)==False:
                    print("unavailable move")    
                    continue
                elif board.is_empty(x,y):
                    print("Kolejne proponowane współrzędne: " + str(x) + "," + str(y))
                    z=input("Podaj stan współrzędnych, jak poprzednio - trafiony, nietrafiony, zatopiony: ")
                    
                    if z=="nietrafiony":
                        board.change_to_miss(x,y)
                        board.show_board(board_of)
                        continue
                    if z=="zatopiony":
                        LAST_HIT.append([x,y])
                        for el in LAST_HIT:
                            board.change_to_sunken(el[0],el[1])
                        board.show_board(board_of)
                        ship.form="full"
                        return False
                    if z=="trafiony":
                        board.change_to_hit(x,y)
                        print(board)
                        board.show_board(board_of)
                        LAST_HIT.append([x,y])
            

random_coord=rand_coord(col, row)


game_on=True
while game_on:
    x=diagonal1(col, row)
    y=diagonal2(col, row)
#diagonals to lista współrzędnych wszystkich punktów na przekątnych
    diagonals=x+y
    #print(diagonals)
    mylist=iter([x for x in diagonals])
    coord=next(mylist, rand_coord(col, row))
    print("Proponowane współrzędne do sprawdzenia na tablicy przeciwnika: " + str(coord))
    for el in range(size_of_board+1):
#przychodzące - raise Exception na wszelki wypadek?    
        if board.is_empty(coord[0], coord[1]):
            c=input("Wpisz trafiony, nietrafiony lub zatopiony: ")#informacja otrzymana - funkcje - przyjmij, przerób na swoje
            if c=="trafiony":
                ship=Ship(coord[0],coord[1],"unfully",board, 3)
                find_rest_of_ship(ship)
            elif c=="nietrafiony":
                board.change_to_miss(coord[0], coord[1])
                board.show_board(board_of)
                coord=next(mylist, rand_coord(col, row))#odeślij te współrzędne 
                print("Kolejne proponowane współrzędne do sprawdzenia:" + str(coord))  
            elif c=="zatopiony":
                board.change_to_sunken(coord[0], coord[1]) #zliczać te pojedyncze zatopione?
                board.show_board(board_of)
                coord=next(mylist, rand_coord(col, row))#odeślij te współrzędne
                print("Kolejne proponowane współrzędne do sprawdzenia:" + str(coord))
        else:
            coord=next(mylist, rand_coord(col, row))
            print("Kolejne proponowane współrzędne do sprawdzenia:" + str(coord))

#nie uwzględniłam jednej istotnej kwestii. Czy statki mogą się stykać???!!! 