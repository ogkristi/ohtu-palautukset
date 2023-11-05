class Player:
    def __init__(self, name, team, goals, assists):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists

    @property
    def points(self):
        return self.goals + self.assists

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__
    
    def __str__(self):
        return f"{self.name} {self.team} {self.goals} + {self.assists} = {self.points}"
