class Player:
    def __init__(self, dict):
        self.__dict__.update(dict)

    def __str__(self):
        return f"{self.name} team {self.team}  goals {self.goals} assists {self.assists}"