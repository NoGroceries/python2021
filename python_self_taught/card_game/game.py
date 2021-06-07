from python_self_taught.card_game.player import Player
from python_self_taught.card_game.deck import Deck


class Game:
    def __init__(self):
        name1 = input("player1 name:")
        name2 = input("player2 name:")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self, winner):
        w = "{} wins this round".format(winner)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d = "{} drew {} {} drew {}".format(p1n, p1c, p2n, p2c)
        print(d)

    def paly_game(self):
        cards = self.deck.cards
        print("beginning War!")
        round = 0
        while len(cards) >= 2:
            m = "q to quit. Any key to play:"
            response = input(m)
            if response == "q":
                break
            round += 1
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            print("round{}:{} get {}, {}get {}".format(round, p1n, p1c, p2n, p2c))
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(p1n)
            else:
                self.p2.wins += 1
                self.wins(p2n)
        win = self.winner(self.p1, self.p2)
        print("War is over.{} wins".format(win))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "It was a tie!"

game = Game()
game.paly_game()
