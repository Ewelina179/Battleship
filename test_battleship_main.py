from battleship_main import ShipBoard, Game

def test_initial_board():
    board = ShipBoard(10,10)
    assert board.size_of_board == 100