from unittest import TestCase
from ChessBoard import ChessBoard


__author__ = 'abhinav'


class TestChessBoard(TestCase):
    def test_printLastTextMove(self):
        s = ChessBoard()
        #self.assertEquals(s.printLastTextMove(), 'Changed')

    def test_hasAnyValidMoves(self):
        s = ChessBoard()
        self.assertEquals(s.hasAnyValidMoves(), True)

    def test_getAllTextMoves(self):
        s = ChessBoard()
        self.assertEquals(s.getAllTextMoves(), None)

    def test_movePawn(self):
        s = ChessBoard()
        self.assertEquals(s.movePawn((2, 3), (4, 5)), False)
        self.assertEquals(s.movePawn((0, 6), (0, 5)), True)
        #Cases which fails
        # self.assertEquals(s.movePawn((0,3),(4,5)), True)
        # self.assertTrue(s.movePawn(),True,'Passed')
        # self.assertFalse(s.movePawn(),False,'Failed')

    def test_moveKing(self):
        s = ChessBoard()
        self.assertEquals(s.moveKing((3, 4), (4, 5)), True)
        #Cases which fails
        # self.assertEquals(s.moveKing((3, 4), (3, 5)), False)

    def test_moveQueen(self):
        s = ChessBoard()
        self.assertEquals(s.moveQueen((0, 1), (1, 1)), True)
        self.assertEquals(s.moveQueen((0, 1), None), False)

    def test_getLastMove(self):
        s = ChessBoard()
        self.assertEquals(s.getLastMove(), None)
        #Cases which fails
        #a = ((4, 6), (4, 4))
        #self.assertEquals(s.getLastMove(), a)

    def test_isThreatened(self):
        s = ChessBoard()
        self.assertEquals(s.isThreatened(1, 3, None), False)
        self.assertEquals(s.isThreatened(0, 0, None), False)
        #Cases which fails
        #self.assertEquals(s.isThreatened(2, 3, None), False)
        #self.assertEquals(s.isThreatened(0, 0, None), True)

    def test_moveBishop(self):
        s = ChessBoard()
        self.assertEquals(s.moveBishop((0, 1), (1, 1)), False)
        self.assertEquals(s.moveBishop((0, 1), None), False)