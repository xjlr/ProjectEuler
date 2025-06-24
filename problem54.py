from collections import Counter

CARD_ORDER = "23456789TJQKA"
SUITS = "CDHS"

class Card:
    def __init__(self, code):
        self.rank = code[0]
        self.suit = code[1]
        self.value = CARD_ORDER.index(self.rank)
    
    def __repr__(self):
        return f"{self.rank}{self.suit}"
    
class Hand:
    def __init__(self, cards):
        self.cards = sorted([Card(c) for c in cards], key=lambda c: c.value, reverse=True)
        self.rank_counts = Counter(c.value for c in self.cards)
        self.sorted_counts = sorted(self.rank_counts.items(), key=lambda item: (-item[1], -item[0]))
        self.values = [c.value for c in self.cards]
        self.score = self.evaluate()
    
    def is_straight(self):
        values = sorted(set(self.values), reverse=True)
        # Case 1: Normal straight
        if len(values) == 5 and values[0] - values[4] == 4:
            return True, values[0]  # high card
        # Case 2: Wheel straight (A-2-3-4-5)
        if values == [12, 3, 2, 1, 0]:  # A=12, 2=0
            return True, 3  # treat 5 as high card
        return False, None

    def is_flush(self):
        return len(set(c.suit for c in self.cards)) == 1

    def evaluate(self):
        flush = self.is_flush()
        straight, high_card = self.is_straight()
        counts = [count for val, count in self.sorted_counts]

        if flush and straight:
            return (8,high_card)               # Straight flush
        if counts == [4, 1]:
            return (7, self.sorted_counts[0][0])       # Four of a kind
        if counts == [3, 2]:
            return (6, self.sorted_counts[0][0])       # Full house
        if flush:
            return (5, self.values)                    # Flush
        if straight:
            return (4, high_card)                      # Straight
        if counts == [3, 1, 1]:
            return (3, self.sorted_counts[0][0])       # Three of a kind
        if counts == [2, 2, 1]:
            return (2, self.sorted_counts[0][0], self.sorted_counts[1][0]) # Two pairs
        if counts == [2, 1, 1, 1]:
            return (1, self.sorted_counts[0][0])       # One pair
        return (0, self.values)                        # High card

    def __gt__(self, other):
        return self.score > other.score

    def __eq__(self, other):
        return self.score == other.score
  

def parse_line(line):
    cards = line.strip().split()
    return Hand(cards[:5]), Hand(cards[5:])

def count_player1_wins(filename):
    count = 0
    with open(filename) as f:
        for line in f:
            p1, p2 = parse_line(line)
            if p1 > p2:
                count += 1
    return count

filename = 'problem54.txt'
print("Result: ", count_player1_wins(filename))


