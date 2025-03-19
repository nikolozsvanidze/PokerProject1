from deck import Deck, Card

class PokerHand:
    def __init__(self, deck):

        cards = []
        for i in range(5):
            cards.append(deck.deal())
        self._cards = cards

    @property
    def cards(self):
        return self._cards

    def __str__(self):
        return str(self.cards)

    @property
    def is_flush(self):
        for card in self.cards[1:]:
            if self.cards[0]._suit != card._suit:
                return False
        return True


count = 0
flush = 0
while flush < 100:
    deck = Deck()
    deck.shuffle()
    hand = PokerHand(deck)
    if hand.is_flush:
       flush += 1
    count += 1

print(f"probability of flush is {100*flush/count}")

