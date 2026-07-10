import random

def main():
    # Welcome and rules
    print(
        'Welcome to Number Guessing Game!!\n'
        'I will think in a number between 1 and 100\n'
        'Select the difficult to determine the number of guessings you will have\n'
    )
    
    # First play
    game()
    
    while True:
        # Asking the user if wants to play another time
        keep_playing = input('Do you want to play again?\n Enter "yes" for keep playing: ')
        if keep_playing.lower() == 'yes':
            game()
        else:
            print('Thanks for playing!')
            break


def game():
    print(
        '1. Easy (12 attempts)\n'
        '2. Medium (8 attempts)\n'
        '3. Hard (5 attempts)\n'
    )
    
    # Variables
    difficulty = input('Select one of the above: ')
    rand_num = random.randint(1, 100)
    attempts_left = 0
    attempts = 0
    
    # Handling invalid input and selecting difficulty
    while True:
        try:
            difficulty = int(difficulty)
            if difficulty > 3 or difficulty < 1:
                difficulty = int(input('Option not allowed, try again: '))
            else:
                if difficulty == 1:
                    print('Selected easy difficult. You have 12 attempts')
                    attempts_left = 12
                    break
                elif difficulty == 2:
                    print('Selected medium difficult. You have 8 attempts')
                    attempts_left = 8
                    break
                else:
                    print('Selected hard difficult. You have 5 attempts')
                    attempts_left = 5
                    break
        except ValueError:
            difficulty = input('Please enter a number: ')
    
    print('\nStarting the game!')

    while attempts_left > 0:
        # Re-read a valid guess in case of invalid input
        while True:
            guess_input = input('Enter your guess: ')
            try:
                guess = int(guess_input)
                if guess < 1 or guess > 100:
                    print('Please enter a number between 1 and 100.\n')
                    continue
                break
            except ValueError:
                print('Please, enter a valid integer between 1 and 100.\n')
                continue

        # Valid guess: consume an attempt
        attempts_left -= 1
        attempts += 1

        if guess == rand_num:
            print(f'Congratulations! You have guessed the number in {attempts} attempts')
            break
        elif guess > rand_num:
            print(f'Incorrect! The number is lower than {guess}')
            print(f'You have {attempts_left} attempts left\n')
        else:
            print(f'Incorrect! The number is greater than {guess}')
            print(f'You have {attempts_left} attempts left\n')

    if attempts_left == 0 and guess != rand_num:
        print(f'Game over! The number was {rand_num}\n')


if __name__ == '__main__':
    main()