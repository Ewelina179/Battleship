from abc import ABC, abstractmethod
import random

class Board(ABC):

    @abstractmethod
    def create_board():
        pass

    @abstractmethod
    def show_board():
        pass

class ShipBoard(Board):

    def __init__(self, col, row):
        self.col = col
        self.row = row
        self.board = self.create_board()
        self.first_diagonal = self.diagonal1()
        self.second_diagonal = self.diagonal2()

    def create_board(self):
        return [["0" for col in range(self.col)] for row in range(self.row)]

    def show_board(self):
        for row in self.board:
            print((" ").join(row))

    def is_empty(self, row, col):
        try:
            return self.board[row][col]=="e"
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

    def diagonal1(self):
        lst1=[]
        lst1.append([a for a in range(self.col-1,-1,-1)])
        lst1.append([b for b in range(0, self.row)])
        lst=[]
        for i in zip(lst1[0], lst1[1]):
            k=list(i)
            lst.append(k)
        return lst

    def diagonal2(self):
        lst1=[]
        lst1.append([a for a in range(self.col-1, -1, -1)])
        lst1.append([b for b in range(self.row-1, -1, -1)])
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

    def __repr__(self):
        return str(self.board)

class Game(ABC):

    @abstractmethod
    def __init__(self, board: Board):
        pass

    @abstractmethod
    def start_game(self):
        pass
    
    @abstractmethod
    def first_move(self):
        pass

    @abstractmethod
    def play_game(self):
        pass

class Battleship(Game):

    def __init__(self, board: ShipBoard):
        self.board = board

    def start_game(self):
        pass

    def first_move(self):
        pass

    def next_move(self):
        pass

    def hunt_for_ship(self):
        pass

    def play_game(self):
        pass

def main():
    col = int(input("Podaj długość tablicy: "))
    row = int(input("Podaj szerokość tablicy: "))
    shipboard = ShipBoard(col, row)
    print(shipboard.show_board())
    game = Battleship(shipboard)
    

if __name__ == '__main__':
    main()