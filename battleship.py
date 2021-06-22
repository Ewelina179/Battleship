def create_board(col, row):
    board=[["0" for col in range(col)] for row in range(row)]
    return board

#ta tablica to musza być puste elementy, nie cyfry
board_of='global'
board_of=create_board(5,5)

class ShipBoard:
    def __init__(self, board):
        self.board=board
        self.value_of_one=0 #to keep track of 1-ship czy w klasie ship? raczej ship

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
        self.board[row][col]="0"

    def change_to_trafiony(self, row, col):
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
        #to będzie subtabela - np. statek podwójny ?? to pełna pozycja obu kostek. zmiana parametru obiektu
        pass

    def first_move(self, current_row, current_col):
            dict={"row":"x", "col":"y"}
            dict["row"]=current_row
            dict["col"]=current_col+1
            return dict
        #!!!!!!!!!!!!tu musi zwrócić liczbę z cyfr ;pppppppppp
    #next?????? bo ma brać kolejny ruch np. w górę, bok, itd.
    #ifowanie na poziomie funkcji? że np jak krawędź, albo za mały odstęp od innego statku
    def second_move(self, current_row, current_col):
        dict={"row":"x", "col":"y"}
        dict["row"]=current_row+1
        dict["col"]=current_col
        return dict

    def third_move(self, current_row, current_col):
        dict={"row":"x", "col":"y"}
        dict["row"]=current_row
        dict["col"]=current_col-1
        return dict

    def fourth_move(self, current_row, current_col):
        dict={"row":"x", "col":"y"}
        dict["row"]=current_row-1
        dict["col"]=current_col
        return dict
        


#głównym celem klas(y)Ship jest generowanie kolejnego ruchu
#tu classmethod, że tworzy obiekt. ale po co? jak zmienię tu tablicę?tu nie zmieniam tablicy, tylko planuję ruch na podstawie tablicy. tablicę zmieniam w klasie Board

board=ShipBoard(board_of)
print(board)
board.show_board(board_of)



#board.change_to_traiony(x,y)
#print(board)
###
ship1=DoubleShip(4,4,"unfully",board, 3)


while ship1.form=="unfully":
    a,b=ship1.row, ship1.col
    board.change_to_trafiony(a,b)
    print(board)
    x,y=ship1.row, ship1.col#info={"info1":"trafiony niezatopiony", "info2":"trafiony zatopiony", "info3":"nietrafio
    #pewno zamnkąć to w funkcji
    last=[x,y]
    print(last) #pierwszy po sygnale "trafiony niezatopiony"
    #q=ship1.first_move()
    ###muszę wstawić jako argument do kolejnej metody bieżący, ostatni wykonany ruch
    #lst_of_methods=[ship1.first_move(), ship1.second_move(), ship1.third_move(), ship1.fourth_move()]
    #print(lst_of_methods[0])
    #print(lst_of_methods[0]["row"])
    a=ship1.length
    print(a)
    num=0
    searching=True
    while searching:
        for w in range(3):#zależnie od długości statku
            last=[x,y] 
            for q in range(0,4): #bo tyle metod w lst of meth
                #last=[ship1.row, ship1.col]
                lst_of_methods=[ship1.first_move(last[0], last[1]), ship1.second_move(last[0],last[1]), ship1.third_move(last[0], last[1]), ship1.fourth_move(last[0], last[1])]
                x=int(lst_of_methods[q]["row"]) 
                y=int(lst_of_methods[q]["col"])
                print(q)
                #print(y)
                if board.is_empty(x,y)==False:
                    print("unavailable move")
                    continue
                elif board.is_empty(x,y):
                    #print(lst_of_methods[q])
                    z=input("Podaj stan statku: ")
            #komunikat, że trafiony
                    if z=="nietrafiony":
                        board.change_to_miss(x,y)
                    elif z=="zatopiony":
                        board.change_to_zatopiony(x,y)
                        ship1.form="fully"
                
                #print(board)
                        #print(ship1.form)
                        break
                        searching=False
            #na razie pomijam, że trzeba wszystkie zmienić na X z tej pętli
                    elif z=="trafiony":
                        board.change_to_trafiony(x,y)
                        print(board)
                        board.show_board(board_of)
                        new_last=[x,y]

            last=new_last
            print(last)
            print(board)
            board.show_board(board_of)
            

            #board.change_to_zatopiony(ship1.row, ship1.col) #ta linijka, żeby ze ? zrobić X
"""
            działa przy podwójnym statku. przy 3 i 4 nie
            board.change_to_trafiony i dodaj do listy:
            lst_of_tra_niezat=[]
            lst_of_tra_niezat.append(q)
            potem, kiedy zatopiony to wszystkie elementy z q zamien na "X" z "?"
            """
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