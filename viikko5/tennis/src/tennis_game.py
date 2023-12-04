class TennisGame:
    CALL = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}
    DELIM = "-"

    def __init__(self, player1: str, player2: str):
        self.player1 = player1
        self.player2 = player2
        self.score1 = 0
        self.score2 = 0

    def won_point(self, player_name: str):
        match (player_name):
            case self.player1:
                self.score1 += 1
            case self.player2:
                self.score2 += 1
            case _:
                raise ValueError(f"No such player as {player_name}")

    def equal_score(self) -> str:
        score = self.score1
        if score > 2:
            return "Deuce"
        else:
            return f"{self.CALL[score]}{self.DELIM}All"

    def above_4_score(self) -> str:
        winner = self.player1 if self.score1 > self.score2 else self.player2
        diff = abs(self.score1 - self.score2)

        if diff == 1:
            return f"Advantage {winner}"
        elif diff > 1:
            return f"Win for {winner}"

    def under_4_score(self) -> str:
        return f"{self.CALL[self.score1]}{self.DELIM}{self.CALL[self.score2]}"

    def get_score(self) -> str:
        if self.score1 == self.score2:
            return self.equal_score()
        elif self.score1 >= 4 or self.score2 >= 4:
            return self.above_4_score()
        else:
            return self.under_4_score()
