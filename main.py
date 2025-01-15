from logic import *

print("roulette game!!! yippee gambling!!!!")

# TODO: difficulties? (starting cash + payouts + chances)
# TODO: different versions of roulette

balance = 1000

while True:
    # get user bet
    choice = input(
'''place bets
1. even/odd
2. red/black
3. low/high
4. dozens
5. single number (0-36, 00)
[1-4/q/?] > '''
    ).lower()
    
    if choice == 'q':
        print(f"you will be quitting the game with ${balance}")
        suretoquit = input("are you sure you want to quit [y/N]? ")
        print()
        if suretoquit == 'y':
            print('quitting...')
            break
        else:
            print("continuing the game...")
            continue
    
    if choice not in {'1', '2', '3', '4', '5', 'q', '?'}:
        print("please input a valid choice.")
        print()
        continue
    
    print()
    # get user bet amount
    while True:
        bet = input('amount to bet (no decimals!!)\n> ')
        if not bet.isdigit():
            print("please input an integer.")
            continue
        bet = int(bet)
        break
    
    # TODO: balanced gets checked in the if chain based on payout
    
    if bet > balance:
        pass
    
    if choice == '1':
        pass

    elif choice == '2':
        pass

    elif choice == '3':
        pass

    elif choice == '4':
        pass

    elif choice == '5':
        pass

    elif choice == "?":
        pass