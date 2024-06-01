import random

def roll_dice():
    return random.randint(1, 6)

def simulate_dice_rolls(num_rolls):
    results = [0] * 13  # Індекси від 2 до 12 для суми кидків
    for _ in range(num_rolls):
        dice1 = roll_dice()
        dice2 = roll_dice()
        results[dice1 + dice2] += 1
    return results

def calculate_probabilities(results, num_rolls):
    probabilities = [count / num_rolls for count in results[2:]]
    return probabilities

def print_probabilities(probabilities):
    print("Sum\tProbability")
    for i, prob in enumerate(probabilities, start=2):
        print(f"{i}\t{prob:.4f}")

num_rolls = 1000000
results = simulate_dice_rolls(num_rolls)
probabilities = calculate_probabilities(results, num_rolls)
print_probabilities(probabilities)
