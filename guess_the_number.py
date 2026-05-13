import random
def guess_the_number(x):
    low=1
    high=x
    random_number = random.randint(low, high)
    feedback = ''
    while feedback != 'c':
        if low == high:
            print(f'The computer guessed the number {low}!')
            break
        print(f'The computer guesses {random_number}.')
        feedback = input(f'Does the number low, high, or correct? (l/h/c): ')
        if feedback == 'l':
            low = random_number + 1
        elif feedback == 'h':
            high = random_number - 1
        random_number = random.randint(low, high)    
    print(f'The computer guessed the number {random_number} correctly!')
guess_the_number(100)            