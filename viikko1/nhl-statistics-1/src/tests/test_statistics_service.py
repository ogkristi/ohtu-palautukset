from statistics_service import StatisticsService
from player import Player
import unittest

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_exists(self):
        target = Player("Semenko", "EDM", 4, 12)
        result = self.stats.search("Semenko")
        
        self.assertEqual(result, target)

    def test_search_not_exists(self):
        result = self.stats.search("Kariya")
        
        self.assertIs(result, None)

    def test_team_exists(self):
        edm = [
            Player("Semenko", "EDM", 4, 12),
            Player("Kurri",   "EDM", 37, 53),
            Player("Gretzky", "EDM", 35, 89),
            ]
        edm = {str(p) for p in edm}
        
        result = {str(p) for p in self.stats.team("EDM")}
        
        self.assertSetEqual(result, edm)

    def test_team_not_exists(self):
        self.assertEqual(self.stats.team("MED"), [])

    def test_top(self):
        self.assertEqual(self.stats.top(0), [Player("Gretzky", "EDM", 35, 89)])
