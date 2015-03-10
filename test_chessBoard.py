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

    def test__parseTextMove(self):
        chess_obj = ChessBoard()
        print chess_obj._parseTextMove('e2e4')
        #chess_obj.moveKing((0, 4), (1, 4), True)

    def test_addTextMove(self):
        chess_obj = ChessBoard()
        chess_obj.addTextMove('e2e4')
        chess_obj.printBoard()

    def test_moveKing(self):
        chess_obj = ChessBoard()
        self.assertEquals(chess_obj.moveKing((7, 4), (6, 4)), True)
        self.assertEquals(chess_obj.moveKing((7, 4), (4, 4)), True)

    def test_updateKingLocations(self):
        chess_obj = ChessBoard()
        chess_obj.addTextMove('e2e4')
        chess_obj.addTextMove('f7f5')
        chess_obj.printBoard()
        chess_obj.addTextMove('e1e2')
        # Gets the updated location of white king on the chess board.
        print chess_obj._white_king_location
