import random
from move_0 import diagonal1, diagonal2, rand_coord

def create_board(col, row):
    board=[["0" for col in range(col)] for row in range(row)]
    return board


col=int(input("Podaj szerokość tablicy: "))
row=int(input("Podaj wysokość tablicy: "))

global board_of
board_of=create_board(col,row)

r=col*row

class ShipBoard:
    def __init__(self, board):
        self.board=board

    def create_board(self):
        [[col for col in range(self.col)] for row in range(self.row)]

    def show_board( self, s_board):
        for row in s_board:
            print((" ").join(row))

    def is_empty(self, row, col):
        try:
            return self.board[row][col]=="0"
        except IndexError:
            return False

    def change_to_miss(self, row, col):
        self.board[row][col]=" "

    def change_to_hit(self, row, col):
        self.board[row][col]="?"
    def change_to_sunken(self, row, col):
        self.board[row][col]="X"

    def __repr__(self):
        return str(self.board)



class Ship:
    def __init__(self, row, col, form, board, length):
        #form - pełny, niepełny (i jak) - to podaję po strzale #unfully, fully
        self.row=row
        self.col=col
        self.form=form
        self.board=board#ale tylko po to, by śledzić, jak wygląda tablica
        self.length=length
        #length-1,2,3,4
        #zliczanie obiektów tworzonych?
    def changing_form(self):
        pass

    def south_move(self, x,y):
        lst=[x+1,y]
        return lst

    def east_move(self, x,y):
        lst=[x,y+1]
        return lst

    def north_move(self, x,y):
        lst=[x-1,y]
        return lst

    def west_move(self, x,y):
        lst=[x,y-1]
        return lst
        

board=ShipBoard(board_of)
#board.change_to_sunken(1,3)
board.show_board(board_of)
#print(board)
#board.show_board(board_of)

        #if kolejny jest empty to go podaj!
        #kolejna propozycja ruchu z listy. odczyt z pliku, zakodować i wysłać. o ile już nie padł ruch!!!! uwzględnij to!
      
def find_rest_of_ship(ship):
    ship.form="unfully"
    #global A == True
    while True:
        q,w=ship.row, ship.col    
        board.change_to_hit(q,w)
        print(board)
        board.show_board(board_of)
        global LAST_HIT
        LAST_HIT=[]
        LAST_HIT.append([q,w])
        LAST_HIT=[[q,w]]    
        for el in LAST_HIT: 
            for method in range(0,4):
                print(LAST_HIT)
                lst_of_methods=[ship.south_move(el[0], el[1]), ship.east_move(el[0], el[1]), ship.north_move(el[0], el[1]), ship.west_move(el[0], el[1])]
            
                x=int(lst_of_methods[method][0]) 
                y=int(lst_of_methods[method][1])

                if board.is_empty(x,y)==False:
                    print("unavailable move")    
                    continue
                elif board.is_empty(x,y):
                    print(x,y)
                    z=input("Podaj stan współrzędnych: ")
                    
                    if z=="nietrafiony":
                        board.change_to_miss(x,y)
                        board.show_board(board_of)
                        continue
                    if z=="zatopiony":
                        LAST_HIT.append([x,y])
                        for el in LAST_HIT:
                            board.change_to_sunken(el[0],el[1])
                        board.show_board(board_of)
                        ship.form="fully"
                        return False
                        
                        #A==False
                        #break
                    #nie przerywa głównej pętli while. do poprawki
                    if z=="trafiony":
                        board.change_to_hit(x,y)
                        print(board)
                        board.show_board(board_of)
                        LAST_HIT.append([x,y])
            

random_coord=rand_coord(col, row)
#print(random_coord)
#x i y to przekątne adekwatne do rozmiaru tablicy
x=diagonal1(5,5)
y=diagonal2(5,5)

#diagonals to lista współrzędnych wszystkich punktów na przekątnych
diagonals=x+y
#print(diagonals)
"""""
def move_zero(diagonals):
    mylist=iter([x for x in diagonals])
#kolejny ruch to po kolei punty ze współrzędnych. a gdy braknie, losowe z tablicy (+dodać wyjatki, że punkt zatopiony!!!)
    next_move=next(mylist, rand_coord(col, row))
    return next_move
"""""
###################################################
game_on=True
while game_on:
    x=diagonal1(5,5)
    y=diagonal2(5,5)
#diagonals to lista współrzędnych wszystkich punktów na przekątnych
    diagonals=x+y
    #print(diagonals)
    mylist=iter([x for x in diagonals])
    coord=next(mylist, rand_coord(col, row))
    print(coord)
    for el in range(r+1):
        
#przychodzące - raise Exception na wszelki wypadek?    
#coord=[2,2]#przykładowe "kolejne współrzędne" z mojej listy proponowanych ruchów, która to jeszcze nie powstała ;p
#print(coord)
# najpierw muszę sprawdzić czy już te współrzędne nietrafione lub zatopione - we własnym zakresie i dopiero odesłać i czekać na odpowiedź od serwera/input            
        if board.is_empty(coord[0], coord[1]):
            c=input("Podaj stan współrzędnych: ")#informacja otrzymana - funkcje - przyjmij, przerób na swoje
            if c=="trafiony":
                ship=Ship(coord[0],coord[1],"unfully",board, 3)
                find_rest_of_ship(ship)
        #tu się nie przerywa ta pętla. do poprawki
            elif c=="nietrafiony":
                board.change_to_miss(coord[0], coord[1])
                board.show_board(board_of)
                coord=next(mylist, rand_coord(col, row))#odeślij te współrzędne 
                print(coord)
                
            elif c=="zatopiony":
                board.change_to_sunken(coord[0], coord[1]) #zliczać te pojedyncze zatopione?
                board.show_board(board_of)
                coord=next(mylist, rand_coord(col, row))#odeślij te współrzędne
                print(coord)
                
            #coord=next(mylist, rand_coord(col, row))
     #if kolejny jest empty to go podaj!
        #kolejna propozycja ruchu z listy. odczyt z pliku, zakodować i wysłać. o ile już nie padł ruch!!!! uwzględnij to!
        else:
            coord=next(mylist, rand_coord(col, row))
            print(coord)
            