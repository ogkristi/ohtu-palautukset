class Player:
    def __init__(self, dict):
        self.__dict__.update(dict)

    @property
    def points(self):
        return self.goals + self.assists

    def __str__(self):
        return (
            f"{self.name:20} {self.team:5}"
            f"{self.goals} + {self.assists} = {self.points}"
        )