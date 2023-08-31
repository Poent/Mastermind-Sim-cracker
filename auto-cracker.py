import random
from itertools import product

# Game Functions

def generate_code():
    return [random.randint(0, 9) for _ in range(4)]

def evaluate_guess(code, guess):
    correct_digits = 0
    correct_positions = 0
    
    for i in range(4):
        if guess[i] == code[i]:
            correct_positions += 1
    
    for g in set(guess):
        correct_digits += min(code.count(g), guess.count(g))
            
    return correct_digits, correct_positions


# Solver Functions

def feedback(code, guess):
    correct_chars = 0
    correct_positions = 0
    
    for i in range(len(code)):
        if code[i] == guess[i]:
            correct_positions += 1
    
    for g in set(guess):
        correct_chars += min(code.count(g), guess.count(g))
    
    return correct_chars, correct_positions

def filter_codes(possible_codes, guess, correct_chars, correct_positions):
    return [code for code in possible_codes if feedback(code, guess) == (correct_chars, correct_positions)]


# single game loop
def run_single_game(game_number):
    code = generate_code()
    code_str = ''.join(map(str, code))

    possible_codes = [''.join(map(str, p)) for p in product(range(10), repeat=4)]
    guess = possible_codes[0]  # Initial guess
    
    attempts = 0

    print(f"--- Starting game {game_number + 1} ---")
    print(f"Generated code is {code_str}")

    while True:
        attempts += 1
        print(f"Current guess: {guess}")  # Output current guess

        correct_chars, correct_positions = feedback(code_str, guess)
        
        if correct_positions == 4:
            print(f"Code {code_str} is solved with guess {guess}!")
            return attempts  # Return the number of guesses taken

        possible_codes = filter_codes(possible_codes, guess, correct_chars, correct_positions)

        print(f"Number of possible codes left: {len(possible_codes)}")  # Output number of possible codes left
        
        if not possible_codes:
            print("Something went wrong. No possible codes left.")
            return -1  # Something went wrong
        
        # For simplicity, just take the first option as our next guess
        guess = possible_codes[0]


# Main Loop for 100 Iterations

def main():
    total_guesses = 0
    total_games = 10

    for i in range(total_games):
        guesses = run_single_game(i)
        if guesses == -1:
            print("Something went wrong in one of the games.")
            return
        total_guesses += guesses

    average_guesses = total_guesses / total_games
    print(f"\nAverage number of guesses needed over {total_games} games: {average_guesses}")

if __name__ == "__main__":
    main()
