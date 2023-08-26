import random

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

def main():
    code = generate_code()
    attempts = 10
    
    print("Welcome to the Code Guessing Game!")
    print("I have generated a 4-digit code. You have 10 attempts to guess it.")
    
    while attempts > 0:
        guess = input(f"You have {attempts} attempts remaining. Enter your 4-digit guess: ")
        
        if len(guess) != 4 or not guess.isdigit():
            print("Invalid input. Make sure to enter exactly 4 digits.")
            continue
        
        guess = [int(digit) for digit in guess]
        correct_digits, correct_positions = evaluate_guess(code, guess)
        
        print(f"Correct digits: {correct_digits}, Correct positions: {correct_positions}")
        
        if correct_positions == 4:
            print("Congratulations! You've guessed the correct code!")
            break
        
        attempts -= 1
    
    if attempts == 0:
        print(f"Sorry, you've run out of attempts. The correct code was {''.join(map(str, code))}.")

if __name__ == "__main__":
    main()
