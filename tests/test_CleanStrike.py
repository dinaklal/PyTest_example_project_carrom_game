import pytest

import scripts.CleanStrike
from scripts.CleanStrike import *


#functional and unit tests

#testing Player class
def test_player():
    print("\n Player Class test")
    t=Player("test",0)
    assert t.name == "test"
    assert t.points == 0

#testing Board class

def test_Board():
    print("\n Player Class test")
    t=Board(9,1,0)
    assert t.coins == 9
    assert t.red == 1
    assert t.turns == 0

#testing game_end function for draw game

def test_game_end_draw():
    test_board = Board(0,1,0)
    test_player1 = Player("1",2)
    test_player2 = Player("2",3)
    print("\n Game end test for printing draw_game & game end")
    assert False == app.game_end(test_player1,test_player2,test_board)

#testing game_end function for player1 win with 5-1
def test_game_end_player1_win():
    test_board = Board(7,1,0)
    test_player1 = Player("1",5)
    test_player2 = Player("2",1)
    print("\n Game end test for player1 win with 5-1 & game end")
    assert False == app.game_end(test_player1,test_player2,test_board)

#testing input hgher than 6 - expecting systemexit
def test_higher_input_exiting() :
    input_values = ['9']
    output = []

    def mock_input():

        return   input_values.pop(0)

    scripts.CleanStrike.input = mock_input
    scripts.CleanStrike.print = lambda s: output.append(s)
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        scripts.CleanStrike.app.main()
    assert pytest_wrapped_e.type == SystemExit
    assert output[1] == 'Invalid Input'
#testing two times red strike input
def test_two_times_red_input() :
    input_values = [2,3,3]
    out=[]
    def mock_input():
        return input_values.pop(0)

    scripts.CleanStrike.input = mock_input
    scripts.CleanStrike.print = lambda s: out.append(s)
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        scripts.CleanStrike.app.main()

    assert  out[3] ==  "Invalid input, Already Red has been removed from the Board__exiting"
#testing coin epmty draw
def test_coin_empty_draw() :
    input_values = [2,2,2,2,1]
    out=[]
    def mock_input():
        return input_values.pop(0)

    scripts.CleanStrike.input = mock_input
    scripts.CleanStrike.print = lambda s: out.append(s)
    scripts.CleanStrike.app.main()

    assert  out[5] ==  "Draw Game"

#testing input is higher than number of coins in board
def test_input_is_higherhan_board_coins() :
    input_values = [2,2,2,2,2]
    out=[]
    def mock_input():
        return input_values.pop(0)

    scripts.CleanStrike.input = mock_input
    scripts.CleanStrike.print = lambda s: out.append(s)
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        scripts.CleanStrike.app.main()

    assert  out[5] ==  "Invalid input, Insufficent coins in board"

#testing 3 fouls from a player
def test_3fouls_from_player() :
    input_values = [1,3,1,4,1,5,1,4,1]
    out=[]
    def mock_input():
        return input_values.pop(0)

    scripts.CleanStrike.input = mock_input
    scripts.CleanStrike.print = lambda s: out.append(s)
    scripts.CleanStrike.app.main()

    assert  out[9] ==  "Player 1 won the game.Final Score: 5--3"

#testing 3 non srikes from a player
def test_3fouls_from_player() :
    input_values = [1,2,1,6,1,6,1,6,1]
    out=[]
    def mock_input():
        return input_values.pop(0)

    scripts.CleanStrike.input = mock_input
    scripts.CleanStrike.print = lambda s: out.append(s)
    scripts.CleanStrike.app.main()

    assert  out[9] ==  "Player 1 won the game.Final Score: 5-1"















