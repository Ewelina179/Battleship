
def create_board(col, row):
    board=[["e" for col in range(col)] for row in range(row)]
    return board

#ta tablica to musza być puste elementy, nie cyfry

x=create_board(5,5)

class ShipBoard:
    def __init__(self, board):
        self.board=board
        self.value_of_one=0 #to keep track of 1-ship czy w klasie ship? raczej ship

    def create_board(self):
        [[col for col in range(self.col)] for row in range(self.row)]

    def is_empty(self, row, col):
        try:
            return self.board[row][col]=="e"
        except IndexError:
            return False

    def last_shot(self, row, col):
        pass

    def which_next(self):
        pass

    def change_to_miss(self, row, col):
        self.board[row][col]="0"

    def change_to_traiony(self, row, col):
        self.board[row][col]="?"
        #czy to powinien być string czy coś innego?

    def change_to_zatopiony(self, row, col):
        #zmienic tablice i licznik, że jest obiekt
        self.board[row][col]="X"

    def __repr__(self):
        return str(self.board)

class Ship:
    def __init__(self, row, col):
        self.row=row
        self.col=col
        #zliczanie obiektów tworzonych?

    def first_move(self,row, col):
        row=row+1
        col=col



class DoubleShip:
    def __init__(self, row, col, form, board):
        #form - pełny, niepełny (i jak) - to podaję po strzale #unfully, fully
        self.row=row
        self.col=col
        self.form=form
        self.board=board#ale tylko po to, by śledzić, jak wygląda tablica
        #zliczanie obiektów tworzonych?
    def changing_form(self):
        #to będzie subtabela - np. statek podwójny ?? to pełna pozycja obu kostek. zmiana parametru obiektu
        pass

    def first_move(self):
            dict={"row":"x", "col":"y"}
            dict["row"]=self.row+1
            dict["col"]=self.col
            return dict
        #!!!!!!!!!!!!tu musi zwrócić liczbę z cyfr ;pppppppppp
    #next?????? bo ma brać kolejny ruch np. w górę, bok, itd.
    #ifowanie na poziomie funkcji? że np jak krawędź, albo za mały odstęp od innego statku
    def second_move(self):
        dict={"row":"x", "col":"y"}
        dict["row"]=self.row
        dict["col"]=self.col+1
        return dict

    def third_move(self):
        dict={"row":"x", "col":"y"}
        dict["row"]=self.row-1
        dict["col"]=self.col
        return dict

    def fourth_move(self):
        dict={"row":"x", "col":"y"}
        dict["row"]=self.row
        dict["col"]=self.col-1
        return dict
        


#głównym celem klas(y)Ship jest generowanie kolejnego ruchu
#tu classmethod, że tworzy obiekt. ale po co? jak zmienię tu tablicę?tu nie zmieniam tablicy, tylko planuję ruch na podstawie tablicy. tablicę zmieniam w klasie Board

board=ShipBoard(x)
print(board)


ship1=DoubleShip(4,4,"unfully",board)
x,y=ship1.row, ship1.col
board.change_to_traiony(x,y)
print(board)
###
#będzie niżej rekurencja? 
while ship1.form=="unfully":
    #pewno zamnkąć to w funkcji
    lst_of_methods=[ship1.first_move(), ship1.second_move(), ship1.third_move(), ship1.fourth_move()]
    #q=ship1.first_move()
    for q in lst_of_methods:
        if board.is_empty(q["row"], q["col"]):
            print(q)
            board.change_to_zatopiony(q["row"], q["col"])
            board.change_to_zatopiony(ship1.row, ship1.col)
            """
            działa przy podwójnym statku. przy 3 i 4 nie
            board.change_to_trafiony i dodaj do listy:
            lst_of_tra_niezat=[]
            lst_of_tra_niezat.append(q)
            potem, kiedy zatopiony to wszystkie elementy z q zamien na "X" z "?"

            """
            break
    
    print(board)
    ship1.form="fully"
"""
###
x=ship1.first_move()
print(x)
#### to jest rozgraniczone odpowiedzią od serwera i tak byc musi
board.change_to_miss(x["row"], x["col"])
print(board)
#po odpowiedzi od serwera robie na obiekcie board change_to metodę
#krok zero i potrafionym to funckja po prostu? może statimethod.
x=ship1.second_move()
board.change_to_miss(x["row"], x["col"])
print(board)

x=ship1.third_move()
board.change_to_miss(x["row"], x["col"])
print(board)

x=ship1.fourth_move()
board.change_to_miss(x["row"], x["col"])
print(board)
"""