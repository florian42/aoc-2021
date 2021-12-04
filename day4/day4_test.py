from day4.day4_2 import BingoBoard, calc_score, play


class TestBingoBoard:
    def test_marks_numbers(self):
        board = BingoBoard([[11, 12, 13], [21, 22, 23]])
        board.mark(12)
        board.mark(23)
        assert board.rows[0][1].isMarked is True
        assert board.rows[1][2].isMarked is True
        assert board.rows[0][0].isMarked is False
        assert board.rows[0][2].isMarked is False
        assert board.rows[1][0].isMarked is False
        assert board.rows[1][1].isMarked is False

    def test_has_won_if_all_numbers_in_row_marked(self):
        board = BingoBoard([[11, 12, 13], [21, 22, 23]])
        board.mark(11)
        board.mark(12)
        board.mark(13)
        assert board.has_won() is True

    def test_has_won_if_all_numbers_in_column_marked(self):
        board = BingoBoard([[11, 12, 13], [21, 22, 23]])
        board.mark(11)
        board.mark(21)
        board.mark(13)
        assert board.has_won() is True

    def test_returns_is_equal(self):
        board = BingoBoard([[11, 12, 13], [21, 22, 23]])
        other = BingoBoard([[11, 12, 13], [21, 22, 23]])

        is_equal = board == other

        assert is_equal


class TestCalculateScore:
    def test_calculates_score(self):
        board = BingoBoard([[11, 12, 13], [21, 22, 23]])
        board.mark(12)
        board.mark(23)
        assert calc_score(board, 23) == sum([11, 13, 21, 22]) * 23


class TestPlay:
    def test_determines_winner_and_looser(self):
        board = BingoBoard([[11, 12, 13], [21, 22, 23]])
        other_board = BingoBoard([[14, 15, 16], [24, 25, 26]])
        looser_board = BingoBoard([[17, 18, 19], [27, 28, 29]])
        numbers = [11, 12, 13, 14, 24, 19, 29]

        winner, looser = play(numbers, [board, other_board, looser_board])

        assert winner[0] == board
        assert winner[1] == 13
        assert looser[0] == looser_board
        assert looser[1] == 29

    def test_determines_winner_and_looser_when_multiple_boards_finish_parallel(self):
        other_board = BingoBoard([[14, 15, 16], [24, 25, 26]])
        other_board2 = BingoBoard([[14, 16, 16], [24, 26, 26]])
        looser_board = BingoBoard([[17, 18, 19], [27, 28, 29]])
        numbers = [14, 24, 19, 29]

        winner, looser = play(numbers, [other_board, other_board2, looser_board])

        assert winner[0] == other_board
        assert winner[1] == 24
        assert looser[0] == looser_board
        assert looser[1] == 29
