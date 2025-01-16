from logic import *

print("roulette game!!! yippee gambling!!!!")

# TODO: difficulties? (starting cash + payouts + chances)
# TODO: different versions of roulette

balance = 1000

while True:
    payout = 0
    # get user bet
    betkind = input(
'''place bets
1. even/odd
2. red/black
3. low/high
4. dozens
5. single number (0-36, 00)
[1-4/q/?] > '''
    ).lower()
    
    if betkind == 'q':
        print(f"you will be quitting the game with ${balance}")
        suretoquit = input("are you sure you want to quit [y/N]? ")
        print()
        if suretoquit == 'y':
            print('quitting...')
            break
        else:
            print("continuing the game...")
            continue
    
    if betkind not in {'1', '2', '3', '4', '5', 'q', '?'}:
        print("please input a valid betkind.")
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
        print(f"if you lose this, you will end up in debt.")
        continuedebtrisk = input("are you sure you want to continue [y/N]: ").lower()
        if continuedebtrisk != 'y':
            print()
            print()
            continue
    
    if betkind == '1': # even/odd
        while True:
            choice = input("[even] or [odd]?\n>").lower()
            if choice not in {'even', 'odd'}:
                print("please input a valid choice.")
                continue
            break
            
        print(f"you bet ${bet} on {choice}")
        print()

    elif betkind == '2': # red/black
        while True:
            choice = input("[red] or [black]?\n>").lower()
            if choice not in {'red', 'black'}:
                print("please input a valid choice.")
                continue
            break
            
        print(f"you bet ${bet} on {choice}")
        print()

    elif betkind == '3': # low/high
        while True:
            choice = input("[low] or [high]?\n>").lower()
            if choice not in {'low', 'high'}:
                print("please input a valid choice.")
                continue
            break

    elif betkind == '4': # dozens
        while True:
            choice = input(
'''choose:
1. 1-12
2. 13-24
3. 25-36
> 
'''
                           ).lower()
            if choice not in {'1', '2', '3'}:
                print("please input a valid choice.")
                continue
            break

    elif betkind == '5': # single number
        pass

    elif betkind == "?": # help
        continue
    

    print("spinning the wheel...")
    number = getnumber()
    print(f"the number is: {number}")
    
    if betkind == '1': # even/odd
        betkind = input("")

    elif betkind == '2': # red/black
        pass

    elif betkind == '3': # low/high
        pass

    elif betkind == '4': # dozens
        pass

    elif betkind == '5': # single number
        pass
    
    
    if payout > 0:
        print(f"you won ${payout}!!!!!")
        balance += payout - bet
    else:
        print("you lost this bet...")
        balance -= bet
        print("${bet} deducted from your balance")
        
    print(f"your balance is now ${balance}")
    print()
    print()