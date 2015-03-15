import unittest
import ChessBoard


class ChessBoardTest(unittest.TestCase):
    def setUp(self):
        self.chess_board = ChessBoard.ChessBoard()

    def test_isFree(self):
        self.assertTrue(self.chess_board.isFree(1,2))
        self.assertTrue(self.chess_board.isFree(5,2))
        self.assertTrue(self.chess_board.isFree(4,2))
        self.assertFalse(self.chess_board.isFree(1,1))
        self.assertFalse(self.chess_board.isFree(2,0))

    def test_traceValidMoves(self):
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        self.assertEqual(self.chess_board.traceValidMoves([3,3], dirs), [(4, 3), (5, 3), (6, 3), (7, 3), (2, 3), (1, 3), (0, 3), (3, 4), (3, 5), (3, 2), (3, 1)])
        self.assertEqual(self.chess_board.traceValidMoves([1,1], dirs), [(2, 1), (0, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 0)])
        self.assertEqual(self.chess_board.traceValidMoves([0,0], dirs), [(1, 0), (0, 1)])
        self.assertEqual(self.chess_board.traceValidMoves([7,7], dirs), [])
        self.assertEqual(self.chess_board.traceValidMoves([8,8], dirs), [])

if __name__ == '__main__':
    unittest.main()
