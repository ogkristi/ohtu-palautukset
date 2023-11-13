import requests
from operator import attrgetter
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    response = requests.get(url).json()

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    finns = filter(lambda e: e.nationality == "FIN", players)
    finns = sorted(finns, key=attrgetter('points'), reverse=True)

    print("Players from FIN\n")

    for player in finns:
        print(player)

if __name__ == "__main__":
    main()