import random

def generate_code():
    """Generate a 4-digit code with digits from 1 to 6."""
    return [random.randint(1, 6) for _ in range(4)]

def get_feedback(guess, code):
    """Provide feedback in terms of black and white pegs."""
    black_pegs = sum(g == c for g, c in zip(guess, code))
    whites = sum(min(guess.count(j), code.count(j)) for j in set(guess))
    white_pegs = whites - black_pegs
    return black_pegs, white_pegs

def validate_guess(guess):
    """Check if the guess is valid (4 digits, each between 1 and 6)."""
    return len(guess) == 4 and all(1 <= digit <= 6 for digit in guess)

def mastermind():
    """Main function to run the Mastermind game."""
    code = generate_code()
    attempts = 10
    print("Welcome to Mastermind!")
    print("Try to guess the 4-digit code. Each digit is between 1 and 6.")
    print(f"You have {attempts} attempts. Good luck!")

    while attempts > 0:
        guess_str = input(f"Enter your guess ({attempts} attempts remaining): ")
        guess = [int(d) for d in guess_str]
        
        if not validate_guess(guess):
            print("Invalid guess. Please enter 4 digits between 1 and 6.")
            continue
        
        black_pegs, white_pegs = get_feedback(guess, code)
        print(f"Feedback: {black_pegs} black peg(s), {white_pegs} white peg(s)")

        if black_pegs == 4:
            print("Congratulations! You've cracked the code!")
            break

        attempts -= 1

    if attempts == 0:
        print(f"Sorry, you've run out of attempts. The code was: {code}")

if __name__ == "__main__":
    mastermind()