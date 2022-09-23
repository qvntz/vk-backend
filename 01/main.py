import os
from typing import Union


class CrossZeros:
    win_coord = (
        (1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7),
        (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)
    )

    user = 'x'
    board = {i: str(i) for i in range(1, 10)}
    count = 0

    def show_board(self):
        for k, v in self.board.items():
            if k != 0 and k % 3 == 0:
                print(f'| {v} |')
            else:
                print(f'| {v}', end=' ')

    def validate_input(self) -> Union[int, None]:
        os.system('cls||clear')
        print()
        self.show_board()

        try:
            coord = int(input(f'Ход {self.user}, введите число от 1 до 9: '))
        except ValueError:
            print("Некорректный ввод")
            return None
        if 0 < coord < 10 and self.board[coord]:
            self.count += 1
            return coord
        return None

    def start_game(self) -> None:
        while (winner := self.check_winner()) is None:
            if self.count == 9:
                print('Ничья')
                return None
            if x := self.validate_input():
                self.board[x] = self.user
                if self.user == 'o':
                    self.user = 'x'
                else:
                    self.user = 'o'
        print(f'Победил {winner}!!')
        return winner

    def check_winner(self) -> Union[None, str]:
        for i in self.win_coord:
            x, y, z = i
            if self.board[x] == self.board[y] == self.board[z]:
                return self.board[x]
        return None


if __name__ == "__main__":
    game = CrossZeros()
    game.start_game()
