import random

def main():
    # Welcome and rules
    print(
        'Welcome to Number Guessing Game!!\n'
        'I will think in a number between 1 and 100\n'
        'Select the difficult to determine the number of guessings you will have\n'
    )
    print(
        '1. Easy (12 attempts)\n'
        '2. Medium (8 attempts)\n'
        '3. Hard (5 attempts)\n'
    )
    
    difficulty = input('Select one of the above: ')
    
    # Handling invalid input
    while True:
        try:
            difficulty = int(difficulty)
            if difficulty > 3 or difficulty < 1:
                difficulty = int(input('Option not allowed, try again: '))
            else:
                if difficulty == 1:
                    print('Selected easy difficult. You have 12 attempts')
                    break
                elif difficulty == 2:
                    print('Selected medium difficult. You have 8 attempts')
                    break
                else:
                    print('Selected hard difficult. You have 5 attempts')
                    break
        except ValueError:
            difficulty = input('Please enter a number: ')
    
    print('\nStarting the game!')
    
if __name__ == '__main__':
    main()