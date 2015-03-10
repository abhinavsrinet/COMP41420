from unittest import TestCase
from ChessBoard import ChessBoard
from ChessBoard import FEN

__author__ = 'Megha'


class TestFEN(TestCase):
    def test_setFEN(self):
        chessboard_obj1 = ChessBoard()
        chessboard_obj2 = ChessBoard()
        fen_obj = FEN()
        fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
        fen_obj.setFEN(chessboard_obj1, fen)
        expected_board = [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p'] * 8,
            ['.'] * 8,
            ['.'] * 8,
            ['.'] * 8,
            ['.'] * 8,
            ['P'] * 8,
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]
        self.assertEqual(chessboard_obj1._board, expected_board, "For the starting position")

        fen = "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1"
        fen_obj.setFEN(chessboard_obj1, fen)
        chessboard_obj2.addTextMove('e2e4')
        self.assertEqual(chessboard_obj1._board, chessboard_obj2._board, "For the move e2 to e4")

    def test_getFEN(self):
        chessboard_obj1 = ChessBoard()
        fen_obj = FEN()
        fen1 = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
        self.assertEqual(fen_obj.getFEN(chessboard_obj1), fen1, "For the starting position")
