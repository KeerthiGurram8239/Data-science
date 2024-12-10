"""
File: Keerthi-Gurram-Program2.py
Name: Keerthi Gurram
Course: DSA 230/CIS 492/CIS 593 Intro to Data Science I
Date: 09/22/2024

"""

import random

def rollDice() -> list:
    """Simulates a dice poker roll by returning a list of 5 random ints, where each is between 1 and 6"""
    return [random.randint(1, 6) for _ in range(5)]

def countFrequencies(dice: list) -> dict:
    """Counts the frequency of each dice value in the roll"""
    frequency = {}
    for die in dice:
        if die in frequency:
            frequency[die] += 1
        else:
            frequency[die] = 1
    return frequency

# 3a) isFiveKind function
def isFiveKind(dice: list) -> bool:
    """Returns True if all five dice are the same value"""
    frequencies = countFrequencies(dice)
    return 5 in frequencies.values()

# 3b) isFourKind function
def isFourKind(dice: list) -> bool:
    """Returns True if four dice are the same value"""
    frequencies = countFrequencies(dice)
    return 4 in frequencies.values()

# 3c) isFullHouse function
def isFullHouse(dice: list) -> bool:
    """Returns True if there are three of one value and two of another value"""
    frequencies = countFrequencies(dice)
    return sorted(frequencies.values()) == [2, 3]

# 3d) isStraight function
def isStraight(dice: list) -> bool:
    """Returns True if all dice can be ordered consecutively"""
    dice_sorted = sorted(dice)
    return dice_sorted == list(range(min(dice), min(dice) + 5))

# 3e) isThreeKind function
def isThreeKind(dice: list) -> bool:
    """Returns True if three dice are the same value"""
    frequencies = countFrequencies(dice)
    return 3 in frequencies.values()

# 3f) isTwoPair function
def isTwoPair(dice: list) -> bool:
    """Returns True if there are two pairs of dice with the same value"""
    frequencies = countFrequencies(dice)
    return list(frequencies.values()).count(2) == 2

# 3g) isPair function
def isPair(dice: list) -> bool:
    """Returns True if two dice are the same value"""
    frequencies = countFrequencies(dice)
    return list(frequencies.values()).count(2) == 1

# 3h) playDicePoker function
def playDicePoker(numRolls: int) -> dict:
    """Simulates a dice poker game for a given number of rolls and returns the result of different hands"""
    handsWon = {"fiveKind": 0, "fourKind": 0, "fullHouse": 0, "straight": 0, "threeKind": 0, "twoPair": 0, "pair": 0, "bust": 0}
    
    for _ in range(numRolls):
        dice = rollDice()
        
        if isFiveKind(dice):
            handsWon["fiveKind"] += 1
        elif isFourKind(dice):
            handsWon["fourKind"] += 1
        elif isFullHouse(dice):
            handsWon["fullHouse"] += 1
        elif isStraight(dice):
            handsWon["straight"] += 1
        elif isThreeKind(dice):
            handsWon["threeKind"] += 1
        elif isTwoPair(dice):
            handsWon["twoPair"] += 1
        elif isPair(dice):
            handsWon["pair"] += 1
        else:
            handsWon["bust"] += 1
    
    return handsWon

# 3i) printResults function
def printResults(numRolls: int, handsWon: dict) -> None:
    """Prints the results of the game including total rolls and percentage of each hand"""
    print(f"\nTotal Rolls: {numRolls}")
    for hand, count in handsWon.items():
        percentage = (count / numRolls) * 100
        print(f"{hand.capitalize()}: {count} ({percentage:.2f}%)")

# 3j) Main function to run the game
def main():
    """Main script that asks user for the number of rolls and displays the results"""
    numRolls = int(input("How many times would you like to play dice poker? "))
    results = playDicePoker(numRolls)
    printResults(numRolls, results)

# Use this starting code to test your functions
testRoll = rollDice()
print(f"Test Roll: {testRoll}")

# Testing the other functions on the test roll
print(f"Is Five of a Kind: {isFiveKind(testRoll)}")
print(f"Is Four of a Kind: {isFourKind(testRoll)}")
print(f"Is Full House: {isFullHouse(testRoll)}")
print(f"Is Straight: {isStraight(testRoll)}")
print(f"Is Three of a Kind: {isThreeKind(testRoll)}")
print(f"Is Two Pair: {isTwoPair(testRoll)}")
print(f"Is Pair: {isPair(testRoll)}")

# Main function to run the game
def main():
    """Main script that asks user for the number of rolls and displays the results"""
    numRolls = int(input("How many times would you like to play dice poker? "))
    results = playDicePoker(numRolls)
    printResults(numRolls, results)

# Testing
if __name__ == "__main__":
    main()
