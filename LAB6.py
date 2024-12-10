class PlayingCard:
    # Dictionary to map card names to corresponding values
    rank_to_value = {
        "Ace": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5,
        "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10,
        "Jack": 11, "Queen": 12, "King": 13
    }

    # List to establish order of suits alphabetically
    suit_priority = ["Clubs", "Diamonds", "Hearts", "Spades"]

    def __init__(self, rank_name, suit_type):
        # Assign card rank and suit
        self.rank_name = rank_name
        self.suit_type = suit_type
        # Retrieve corresponding value for the rank
        self.rank_value = PlayingCard.rank_to_value[rank_name]

    # Method to compare two cards using the less-than operator
    def __lt__(self, other_card):
        # Compare based on rank values first
        if self.rank_value != other_card.rank_value:
            return self.rank_value < other_card.rank_value
        # If rank values are the same, compare suit based on priority
        return PlayingCard.suit_priority.index(self.suit_type) < PlayingCard.suit_priority.index(other_card.suit_type)

# Testing different card comparisons
first_card = PlayingCard("Seven", "Hearts")
second_card = PlayingCard("Queen", "Spades")
third_card = PlayingCard("Queen", "Diamonds")

print(first_card < second_card)  # Output: True
print(second_card < third_card)  # Output: False
print(third_card < third_card)  # Output: False
