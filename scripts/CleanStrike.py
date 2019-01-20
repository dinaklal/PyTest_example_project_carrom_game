class Board:
    def __init__(self,coins,red,striker,turns):
        self.coins=coins
        self.red = red
        self.striker = striker
        self.turns=turns
class Player:
    def __init__(self,name,points):
        self.name=name
        self.points=points
        self.last_point = 1
        self.second_last_point = 1

def game_end(playerA,playerB,current_board):
    if  playerA.points > playerB.points and playerA.points - playerB.points >= 3 and playerA.points >= 5:
         print("Player "+playerA.name + " won the game.Final Score: "+ str(playerA.points) + "-"+ str(playerB.points))
         return False
    elif playerB.points > playerA.points and playerB.points - playerA.points >= 3 and playerB.points >= 5:
         print("Player " + playerB.name + " won the game.Final Score: "+str(playerB.points) + "-" + str(playerA.points))
         return False
    elif current_board.coins <= 0 :
        print("Draw Game")
        return False
    else :
            return True

def calcuate_points(strike) :
         if strike == 1:
            return 1,True,True,1
         elif strike == 2:
            return 2,True,True,2

         elif strike == 3:
             return 3,False,True,0
         elif strike == 4:
             return -1,True,True,0

         elif strike == 5:
             return -2,True,True,1
         elif strike == 6:
             return 0,True,True,0
         else:
             exit(0)

def main():
        current_board = Board(9,1,1,0)
        playerA = Player("1",0)
        playerB = Player("2",0)

        while game_end(playerA,playerB,current_board) :
            if current_board.turns % 2 == 0 :
                   print("Player "+playerA.name+": Choose an outcome from the list below \n \
                   1. Strike\n \
                   2. Multistrike\n \
                   3. Red strike\n \
                   4. Striker strike\n \
                   5. Defunct coin\n \
                   6. None\n" )
                   playera_in= int(input())
                   points,red,striker,coins_fell = calcuate_points(playera_in)
                   if playerA.last_point < 1 and playerA.second_last_point < 1 and points < 1 :
                       if playerA.last_point < 0 and playerA.second_last_point < 0 and points < 0 :
                           points = points - 2
                       else :
                           points = points -1
                   playerA.second_last_point = playerA.last_point
                   playerA.last_point = points

                   playerA.points = playerA.points+points
                   current_board.coins = current_board.coins-coins_fell
                   if not red:
                       current_board.red =0

            else:
                   print("Player " + playerB.name + ": Choose an outcome from the list below \n \
                   1. Strike\n \
                   2. Multistrike\n \
                   3. Red strike\n \
                   4. Striker strike\n \
                   5. Defunct coin\n \
                   6. None\n")
                   playerb_in = int(input())
                   points, red, striker, coins_fell = calcuate_points(playerb_in)

                   if playerB.last_point < 1 and playerB.second_last_point < 1 and points < 1 :
                       if playerB.last_point < 0 and playerB.second_last_point < 0 and points < 0 :
                           points = points - 2
                       else :
                           points = points -1
                   playerB.second_last_point = playerB.last_point
                   playerB.last_point = points

                   playerB.points = playerB.points + points
                   current_board.coins = current_board.coins - coins_fell
                   if red == False:
                       current_board.red = 0

            current_board.turns = current_board.turns + 1



