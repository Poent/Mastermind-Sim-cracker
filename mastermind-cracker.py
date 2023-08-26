from itertools import product

# Generate all possible codes (from 0000 to 9999)
possible_codes = [''.join(map(str, p)) for p in product(range(10), repeat=4)]

def feedback(code, guess):
    """
    Given the actual code and a guess, returns the number of correct characters
    and the number of characters in the correct positions.
    """
    correct_chars = 0
    correct_positions = 0
    
    for i in range(len(code)):
        if code[i] == guess[i]:
            correct_positions += 1
    
    for g in set(guess):
        correct_chars += min(code.count(g), guess.count(g))
    
    return correct_chars, correct_positions

def filter_codes(possible_codes, guess, correct_chars, correct_positions):
    """
    Filters out codes from possible_codes that would not produce
    the same feedback if they were the actual code.
    """
    return [code for code in possible_codes if feedback(code, guess) == (correct_chars, correct_positions)]

# Get the initial guess from the user
initial_guess = input("Enter your initial guess: ")

# Get feedback for the initial guess
correct_chars = int(input("How many correct characters for the initial guess? "))
correct_positions = int(input("How many correct positions for the initial guess? "))

# Filter the list of possible codes based on the feedback for the initial guess
possible_codes = filter_codes(possible_codes, initial_guess, correct_chars, correct_positions)

# Main loop
while True:
    # For simplicity, just take the first option as our next guess
    guess = possible_codes[0]
    print(f"Next guess: {guess}")

    # Get feedback for the guess
    correct_chars = int(input("How many correct characters? "))
    correct_positions = int(input("How many correct positions? "))

    if correct_positions == 4:
        print("Code is solved!")
        break

    # Filter the list of possible codes based on feedback
    possible_codes = filter_codes(possible_codes, guess, correct_chars, correct_positions)

    if not possible_codes:
        print("Something went wrong. No possible codes left.")
        break
