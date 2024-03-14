sliding_puzzle = [[1, 2, 3],
                  [4, 8, 7],
                  [6, 0, 9]]

sliding_puzzle_answer = [[1, 2, 3],
                         [4, 0, 6],
                         [7, 8, 9]]


class SlidingPuzzleGame:

    def __init__(self, board: list[list[int]], answer: list[list[int]]):
        self.board = board
        self.answer = answer
        # the board and the answer are not of the same shape!
        assert len(board) == len(answer)
        for i in range(len(board)):
            assert len(board[i]) == len(answer[i])
        self.hole_idx = self.find_hole()
        # the board has no hole!
        assert self.hole_idx != (-1, -1)

    def find_hole(self) -> tuple[int, int]:
        for r in range(len(self.board)):
            for c, c_value in enumerate(self.board[r]):
                if c_value == 0:
                    return r, c
        return -1, -1

    def is_solved(self) -> bool:
        return self.board == self.answer

    # idx should probably not be a tuple, we don't need it to be hashable, but it is clearer this way :)
    def check_idx(self, idx: tuple[int, int], value: int) -> bool:
        # case when not in bounds
        if idx[0] < 0 or idx[0] >= len(self.board) or idx[1] < 0 or idx[1] >= len(self.board[0]):
            return False
        if self.board[idx[0]][idx[1]] == value:
            return True
        return False

    def move(self, tile: int) -> bool:
        possible_moves = [(-1, 0),
                          (0, -1),
                          (1, 0),
                          (0, 1)]
        for row in possible_moves:
            # trust me it's int, int
            # noinspection PyTypeChecker
            selected_tile: tuple[int, int] = tuple(map(lambda i, j: i + j, row, self.hole_idx))
            if self.check_idx(selected_tile, tile):
                # swap
                self.board[selected_tile[0]][selected_tile[1]] = 0
                self.board[self.hole_idx[0]][self.hole_idx[1]] = tile
                self.hole_idx = selected_tile
                return True
        return False

    def pretty_print(self):
        for row in self.board:
            print(row)

    def play_game(self):
        while not self.is_solved():
            self.pretty_print()
            again = input("Choose what tile to move:")
            while not again.isdigit():
                self.pretty_print()
                again = input("Please enter the number of a valid tile:")
            if not self.move(int(again)):
                print("Invalid tile")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    game = SlidingPuzzleGame(sliding_puzzle, sliding_puzzle_answer)
    game.play_game()
