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

    def __init__(self, col):
        self.col = col
        self.board = self.create_board()
        self.first_diagonal = self.diagonal1()
        self.second_diagonal = self.diagonal2()
        self.rand_coord = self.rand_coordinates()
        self.size_of_board = self.col ** 2

    def create_board(self):
        return [["0" for x in range(self.col)] for y in range(self.col)]

    def show_board(self):
        for row in self.board:
            print((" ").join(row))

    def is_empty(self, x, y):
        try:
            self.board[x][y]=="e"
            return True
        except IndexError:
            return False

    def change_to_miss(self, row, col):
        self.board[row][col]=" "

    def change_to_hit(self, row, col):
        self.board[row][col]="?"

    def change_to_sunken(self, row, col):
        self.board[row][col]="X"

    def diagonal1(self):
        lst1=[]
        lst1.append([a for a in range(self.col-1,-1,-1)])
        lst1.append([b for b in range(0, self.col)])
        lst=[]
        for i in zip(lst1[0], lst1[1]):
            k=list(i)
            lst.append(k)
        return lst

    def diagonal2(self):
        lst1=[]
        lst1.append([a for a in range(self.col-1, -1, -1)])
        lst1.append([b for b in range(self.col-1, -1, -1)])
        lst=[]
        for i in zip(lst1[0],lst1[1]):
            k=list(i)
            lst.append(k)
        return lst

    def rand_coordinates(self):
        rand_row=random.randint(0, self.col-1)
        rand_col=random.randint(0, self.col-1)
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
    
    #@abstractmethod
    #def first_move(self):
    #    pass

    @abstractmethod
    def play_game(self):
        pass

class Battleship(Game):

    def __init__(self, board: ShipBoard):
        self.board = board
        self.first_moves = board.first_diagonal + board.second_diagonal
        self.rand_coord = board.rand_coordinates()

    def start_game(self):
        print("Proponowane współrzędne do sprawdzenia na tablicy przeciwnika (wiersz 0-9, kolumna 0-9): " + str(self.first_moves_when_not_hunting()))

    def first_moves_when_not_hunting(self):
        mylist=iter(self.first_moves)
        coord=next(mylist, self.board.rand_coordinates())
        return coord

    def hunt_for_ship(self, col, row):
        self.board.show_board()
        last_hit = []
        last_hit.append([col, row])
        for el in last_hit: 
            for method in range(0,4):
                print("Lista trafionych współrzędnych" + str(last_hit))
                lst_of_methods=[self.south_move(el[0], el[1]), self.east_move(el[0], el[1]), self.north_move(el[0], el[1]), self.west_move(el[0], el[1])]
            
                x=int(lst_of_methods[method][0])
                y=int(lst_of_methods[method][1])

                if self.board.is_empty(x,y)==False:
                    print("unavailable move")    
                    continue
                elif self.board.is_empty(x,y):
                    print("Kolejne proponowane współrzędne (wiersz 0-9, kolumna 0-9): " + str(x) + "," + str(y))
                    z=input("Podaj stan współrzędnych, jak poprzednio - trafiony, nietrafiony, zatopiony: ")
                    
                    if z=="nietrafiony":
                        self.board.change_to_miss(x,y)
                        self.board.show_board()
                        continue
                    if z=="zatopiony":
                        last_hit.append([x,y])
                        for el in last_hit:
                            self.board.change_to_sunken(el[0],el[1])
                        self.board.show_board()
                        return False
                    if z=="trafiony":
                        self.board.change_to_hit(x,y)
                        print(self.board)
                        self.board.show_board()
                        last_hit.append([x,y])

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

    def play_game(self):
        game_on=True
        while game_on:
            self.start_game()
            print("Proponowane współrzędne do sprawdzenia na tablicy przeciwnika (wiersz 0-9, kolumna 0-9): " + str(self.first_moves_when_not_hunting()))
            coordinates=iter([x for x in self.first_moves])
            print(self.first_moves)
            coord=next(coordinates, self.board.rand_coordinates())
            for _ in range(self.board.size_of_board+1):
                if self.board.is_empty(coord[0], coord[1]):
                    c=input("Wpisz trafiony, nietrafiony lub zatopiony: ")
                    if c=="trafiony":
                        self.board.change_to_hit(coord[0], coord[1])
                        self.hunt_for_ship(coord[0], coord[1])
                    elif c=="nietrafiony":
                        self.board.change_to_miss(coord[0], coord[1])
                        self.board.show_board()
                        coord=next(coordinates, self.board.rand_coordinates())
                        print("Kolejne proponowane współrzędne do sprawdzenia:" + str(coord))  
                    elif c=="zatopiony":
                        self.board.change_to_sunken(coord[0], coord[1])
                        self.board.show_board()
                        coord=next(coordinates, self.board.rand_coordinates())
                        print("Kolejne proponowane współrzędne do sprawdzenia:" + str(coord))
                else:
                    coord=next(coordinates, self.board.rand_coordinates())
                    print("Kolejne proponowane współrzędne do sprawdzenia:" + str(coord))


def main():
    col = int(input("Podaj długość boku tablicy: "))
    shipboard = ShipBoard(col)
    game = Battleship(shipboard)
    game.play_game()
    

if __name__ == '__main__':
    main()