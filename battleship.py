def create_board(col, row):
    board=[["0" for col in range(col)] for row in range(row)]
    return board

global board_of
board_of=create_board(5,5)

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

    def change_to_trafiony(self, row, col):
        self.board[row][col]="?"
    def change_to_zatopiony(self, row, col):
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

    def first_move(self, x,y):
        lst=[x+1,y]
        return lst

    def second_move(self, x,y):
        lst=[x,y+1]
        return lst

    def third_move(self, x,y):
        lst=[x-1,y]
        return lst

    def fourth_move(self, x,y):
        lst=[x,y-1]
        return lst
        

board=ShipBoard(board_of)
#print(board)
#board.show_board(board_of)

        #if kolejny jest empty to go podaj!
        #kolejna propozycja ruchu z listy. odczyt z pliku, zakodować i wysłać. o ile już nie padł ruch!!!! uwzględnij to!
        
def find_rest_of_ship(ship1):
    ship1.form=="unfully"
    while ship1.form=="unfully":
        q,w=ship1.row, ship1.col    
        board.change_to_trafiony(q,w)
        print(board)
        board.show_board(board_of)
        global LAST_HIT
        LAST_HIT=[]
        LAST_HIT.append([q,w])
        LAST_HIT=[[q,w]]    
        for el in LAST_HIT: 
            for method in range(0,4):
                print(LAST_HIT)
                lst_of_methods=[ship1.first_move(el[0], el[1]), ship1.second_move(el[0], el[1]), ship1.third_move(el[0], el[1]), ship1.fourth_move(el[0], el[1])]
            
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
                            board.change_to_zatopiony(el[0],el[1])
                        board.show_board(board_of)
                        #ship1.form="fully"
                        ship1.form!="unfully"
                        break
                    #nie przerywa głównej pętli while. do poprawki
                    if z=="trafiony":
                        board.change_to_trafiony(x,y)
                        print(board)
                        board.show_board(board_of)
                        LAST_HIT.append([x,y])

#przychodzące - raise Exception na wszelki wypadek?    
coord=[4,4]#przykładowe "kolejne współrzędne" z mojej listy proponowanych ruchów, która jeszcze nie powstała ;p
print(coord)                
c=input("Podaj stan współrzędnych: ")#informacja otrzymana - funkcje - przyjmij, przerób na swoje
if c=="trafiony":
    ship1=Ship(coord[0],coord[1],"unfully",board, 3)
    find_rest_of_ship(ship1)
        #tu powinna być funckja do tego przebiegu
elif c=="nietrafiony":
    a==b
     #if kolejny jest empty to go podaj!
        #kolejna propozycja ruchu z listy. odczyt z pliku, zakodować i wysłać. o ile już nie padł ruch!!!! uwzględnij to!