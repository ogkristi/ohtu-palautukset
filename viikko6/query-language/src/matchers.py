class All:
    def __init__(self) -> None:
        pass

    def test(self, player):
        return True


class QueryBuilder:
    def __init__(self, *matchers) -> None:
        self._matchers = matchers

    def playsIn(self, team):
        return QueryBuilder(*self._matchers, PlaysIn(team))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(*self._matchers, HasAtLeast(value, attr))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(*self._matchers, HasFewerThan(value, attr))

    def oneOf(self, *matchers):
        return QueryBuilder(*self._matchers, Or(*matchers))

    def build(self):
        if len(self._matchers) == 0:
            return All()
        return And(*self._matchers)


class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True


class Or:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if matcher.test(player):
                return True

        return False


class Not:
    def __init__(self, matcher) -> None:
        self._matcher = matcher

    def test(self, player):
        return not self._matcher.test(player)


class HasFewerThan:
    def __init__(self, value, attr) -> None:
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)
        return player_value < self._value


class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value
