from operator import attrgetter

class PlayerStats:
    def __init__(self, reader) -> None:
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        result = filter(lambda e: e.nationality == nationality, self.players)
        result = sorted(result, key=attrgetter('points'), reverse=True)

        return result