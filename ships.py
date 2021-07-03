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
        self.row=row
        self.col=col
        self.form=form #full or unfull
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
        