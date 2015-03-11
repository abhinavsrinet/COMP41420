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

    def test_addTextMove(self):
        chess_obj = ChessBoard()
        chess_obj.addTextMove('e2e4')
        chess_obj.printBoard()

    def test_getValidKingMoves(self):
        chess_obj = ChessBoard()
        chess_obj.addTextMove('e2e4')
        chess_obj._turn = 0
        print chess_obj.getValidKingMoves((7, 4))

    def test_updateKingLocations(self):
        chess_obj = ChessBoard()
        chess_obj.addTextMove('e2e4')
        chess_obj.addTextMove('f7f5')
        chess_obj.printBoard()

        # Moving white king one step ahead
        chess_obj.addTextMove('e1e2')

        # Gets the updated location of white king on the chess board.
        chess_obj.updateKingLocations()
        print chess_obj._white_king_location

    def test_printLastTextMove(self):
        chess_obj = ChessBoard()

        # when no moves has been made.
        print chess_obj.getLastTextMove()
        chess_obj.printLastTextMove()

        chess_obj.addTextMove('e2e4')
        chess_obj.addTextMove('f7f5')
        chess_obj.printLastTextMove()

    def test_getMoveCount(self):
        chess_obj = ChessBoard()

        # When there are no moves
        self.assertEquals(chess_obj.getMoveCount(), 0)

        # When there are certain number of moves
        chess_obj.addTextMove('e2e3')
        chess_obj.addTextMove('g7g6')
        chess_obj.addTextMove('Bd3')
        chess_obj.printBoard()
        self.assertEquals(chess_obj.getMoveCount(), 3)

        # When moves are undone. shouldn't it be reflected to the move count?
        chess_obj.undo()
        chess_obj.undo()
        chess_obj.printBoard()
        self.assertEquals(chess_obj.getMoveCount(), 1)  # test case fails here.

        # Shouldn't this be 2 here?
        chess_obj.redo()
        chess_obj.printBoard()
        self.assertEquals(chess_obj.getMoveCount(), 2)  # test case fails here.

    def test_undo(self):
        chess_obj = ChessBoard()
        chess_obj.addTextMove('e2e3')
        chess_obj.addTextMove('g7g6')

        self.assertEquals(chess_obj.undo(), True)
        self.assertEquals(chess_obj.undo(), True)
        self.assertEquals(chess_obj.undo(), False)

        # This should print as if board has been reset
        chess_obj.printBoard()

    def test_redo(self):
        chess_obj = ChessBoard()
        chess_obj.addTextMove('e2e3')
        chess_obj.addTextMove('g7g6')

        chess_obj.undo()
        chess_obj.undo()

        self.assertEquals(chess_obj.redo(), True)

    def test_gotoMove(self):
        chess_obj = ChessBoard()
        chess_obj.addTextMove('e2e3')
        chess_obj.addTextMove('g7g6')
        chess_obj.addTextMove('Bd3')

        # Checking the boundry condition
        self.assertEquals(chess_obj.gotoMove(-1), False)
        self.assertEquals(chess_obj.gotoMove(5), False)

        # Moving to the specific move
        chess_obj.gotoMove(1)
        self.assertEquals(chess_obj.getLastTextMove(), 'e3')

    def test_getAllTextMoves(self):
        chess_obj = ChessBoard()
        chess_obj.addTextMove('e2e3')
        chess_obj.addTextMove('g7g6')
        chess_obj.addTextMove('Bd3')

        self.assertEquals(chess_obj.getAllTextMoves(), ['e3', 'g6', 'Bd3'])

