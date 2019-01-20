import pytest
from scripts.CleanStrike import *
from scripts.CleanStrike import main

#testing Player class
def test_player():
    print("\n Player Class test")
    t=Player("test",0)
    assert t.name == "test"
    assert t.points == 0

#testing Board class

#testing game_end function for draw game

def test_game_end_draw():
    test_board = Board(0,1,1,0)
    test_player1 = Player("1",2)
    test_player2 = Player("2",3)
    print("\n Game end test for printing draw_game & game end")
    assert False == game_end(test_player1,test_player2,test_board)
#testing game_end function for player1 win with 5-1
def test_game_end_player1_win():
    test_board = Board(7,1,1,0)
    test_player1 = Player("1",5)
    test_player2 = Player("2",1)
    print("\n Game end test for player1 win with 5-1 & game end")
    assert False == game_end(test_player1,test_player2,test_board)





