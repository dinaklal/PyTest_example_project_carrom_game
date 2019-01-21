import sys

#creating class Board
class Board:
    def __init__(self,coins,red,turns):
        self.coins=coins
        self.red = red
        self.turns=turns
        
#creating class Player
class Player:
    def __init__(self,name,points):
        self.name=name
        self.points=points
        self.last_point = 1
        self.second_last_point = 1

#creating class App
class app:
    
    '''
    function to check if the game has been completed. It will check for point difference of 3.
    Draw condition comes when there is no coins left in the Board including red.
    '''
    def game_end(playerA,playerB,current_board):
        if  playerA.points > playerB.points and playerA.points - playerB.points >= 3 and playerA.points >= 5:
             print("Player "+playerA.name + " won the game.Final Score: "+ str(playerA.points) + "-"+ str(playerB.points))
             return False
        elif playerB.points > playerA.points and playerB.points - playerA.points >= 3 and playerB.points >= 5:
             print("Player " + playerB.name + " won the game.Final Score: "+str(playerB.points) + "-" + str(playerA.points))
             return False
        elif current_board.coins <= 0 and current_board.red == False: #if there is no coins in board including red
            print("Draw Game")
            return False
        else :
                return True
                
    ''' Points are calculated in this function. The function will return points earned ,
       does red is still there ?, and no.of coins fell during the last strike.
    '''
    def calcuate_points(strike) : 
             if strike == 1:
                return 1,True,1
             elif strike == 2:
                return 2,True,2

             elif strike == 3:
                 return 3,False,0
             elif strike == 4:
                 return -1,True,0

             elif strike == 5:
                 return -2,True,1
             elif strike == 6:
                 return 0,True,0
             else:
                 print("Invalid Input")
                 sys.exit()

    def main():
            current_board = Board(9,1,0)
            playerA = Player("1",0)
            playerB = Player("2",0)
            ''' Loop will run indeffinitely untill the game_end() function returns false.
                The turn will decided based on the Turn ( even - Player 1 , odd - Player2)
            '''
            while app.game_end(playerA,playerB,current_board) :
                if current_board.turns % 2 == 0 :
                       print("Player "+playerA.name+": Choose an outcome from the list below \n \
                       1. Strike\n \
                       2. Multistrike\n \
                       3. Red strike\n \
                       4. Striker strike\n \
                       5. Defunct coin\n \
                       6. None\n" )
                       playera_in= int(input())
                       #receiving points from calcuate_points() function
                       points,red,coins_fell = app.calcuate_points(playera_in)
                       
                       #If there is less coins in board than the coins fell down during strike
                       if current_board.coins < coins_fell :
                           print("Invalid input, Insufficent coins in board")
                           sys.exit()
                          
                       '''check if it is a red strike , if yes check for the red is already pocketed then it is an ' invaid input '
                          else red count will make 0 in the board 
                       '''
                       if not red:
                           if current_board.red == 0:
                                print("Invalid input, Already Red has been removed from the Board__exiting")
                                sys.exit()
                           else :
                                current_board.red =0
                                
                       ''' Check for continuous 3 fouls and continuous 3 Non-Strikes
                       '''
                       if playerA.last_point < 1 and playerA.second_last_point < 1 and points < 1 :
                           if playerA.last_point < 0 and playerA.second_last_point < 0 and points < 0 :
                               points = points - 2
                           else :
                               points = points -1
                       playerA.second_last_point = playerA.last_point
                       playerA.last_point = points
        pu
                       playerA.points = playerA.points+points
                       current_board.coins = current_board.coins-coins_fell


                else:
                       print("Player " + playerB.name + ": Choose an outcome from the list below \n \
                       1. Strike\n \
                       2. Multistrike\n \
                       3. Red strike\n \
                       4. Striker strike\n \
                       5. Defunct coin\n \
                       6. None\n")
                       playerb_in = int(input())
                       points, red,coins_fell = app.calcuate_points(playerb_in)
                       if current_board.coins < coins_fell :
                           print("Invalid input, Insufficent coins in board")
                           sys.exit()
                       if not red:
                           if current_board.red == 0:
                                print("Invalid input, Already Red has been removed from the Board__exiting")
                                sys.exit()
                           else :
                                current_board.red =0
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



