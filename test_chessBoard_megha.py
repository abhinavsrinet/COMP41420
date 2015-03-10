from unittest import TestCase
from ChessBoard import ChessBoard

__author__ = 'Megha'


class TestChessBoard(TestCase):
    def test_getValidMoves(self):
        chessboard_obj1 = ChessBoard()
        self.assertFalse(chessboard_obj1.getValidMoves([0, 8]), "y position out of range")

        self.assertFalse(chessboard_obj1.getValidMoves([-1, 8]), "x and y position out of range")

        self.assertFalse(chessboard_obj1.getValidMoves([-1, 0]), "x position out of range")

        self.assertEqual(chessboard_obj1.getValidMoves([3, 3]), [], "No piece at this position")

        self.assertEqual(chessboard_obj1.getValidMoves([1, 1]), [], "Not the player's turn")

        self.assertEqual(chessboard_obj1.getValidMoves([6, 6]), [(6, 5), (6, 4)],
                         "Pawn can move one place or two places at the start")