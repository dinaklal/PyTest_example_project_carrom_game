class Board:
    def __init__(self,coins,red,striker):
        print("Board created")
        self.coins=coins
        self.red = red
        self.striker = striker
class Player:
    def __init__(self,name,points):
        print("Player  created")
        self.name=name
        self.points=points
class App:
    def main():
            cuerrent_board = Board(9,1,1)
           # print(cuerrent_board.coins)
            playerA = Player("A",0)
           # print(playerA.name)
           # playerB = Player("B",0)



