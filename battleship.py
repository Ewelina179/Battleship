def create_board(col, row):
    board=[["0" for col in range(col)] for row in range(row)]
    return board

board_of='global'
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
        self.board[row][col]="0"

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

    def first_move(self, current_row, current_col):
            dict={"row":"x", "col":"y"}
            dict["row"]=current_row
            dict["col"]=current_col+1
            return dict

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
        

board=ShipBoard(board_of)
print(board)
board.show_board(board_of,5,5)

ship1=Ship(4,4,"unfully",board, 3)


while ship1.form=="unfully":
    a,b=ship1.row, ship1.col
    board.change_to_trafiony(a,b)
    print(board)
    x,y=ship1.row, ship1.col#info={"info1":"trafiony niezatopiony", "info2":"trafiony zatopiony", "info3":"nietrafio
    last=[x,y]
    print(last) #pierwszy po sygnale "trafiony niezatopiony"
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
                if board.is_empty(x,y)==False:
                    print("unavailable move")
                    continue
                elif board.is_empty(x,y):
                    z=input("Podaj stan statku: ")
                    if z=="nietrafiony":
                        board.change_to_miss(x,y)
                    elif z=="zatopiony":
                        board.change_to_zatopiony(x,y)
                        ship1.form="fully"
                        break
                        searching=False
            #na razie pomijam, że trzeba wszystkie zmienić na X z tej pętli
                    elif z=="trafiony":
                        board.change_to_trafiony(x,y)
                        print(board)
                        board.show_board(board_of,5,5)
                        new_last=[x,y]

            last=new_last
            print(last)
            print(board)
            board.show_board(board_of,5,5)
            

            