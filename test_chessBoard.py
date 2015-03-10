from unittest import TestCase
from ChessBoard import ChessBoard

__author__ = 'nikhil'


class TestChessBoard(TestCase):
    def test_getColor(self):
        chess_obj = ChessBoard()
        self.assertEquals(chess_obj.getColor(3, 0), 1)
        self.assertEquals(chess_obj.getColor(2, 2), -1)
        self.assertEquals(chess_obj.getColor(2, 7), 0)

    def test_addMove(self):
        chess_obj = ChessBoard()
        # covers invalid inputs for from position & to position
        self.assertEquals(chess_obj.addMove((-1, 2), (3, 8)), False)
        self.assertEquals(chess_obj.addMove((2, 2), (2, 2)), False)

    def test_isFree(self):
        chess_obj = ChessBoard()
        self.assertEquals(chess_obj.isFree(3, 3), True)
