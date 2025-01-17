import logic
import utils

print("roulette game!!! yippee gambling!!!!")

# TODO: difficulties? (starting cash + payouts + chances)
# TODO: different versions of roulette

balance = 1000

while True:
    number = 0
    payout = 0

    # Get user bet
    betkind = input(
        '''place bets
1. even/odd
2. red/black
3. low/high
4. dozens
5. single number (0-36, 00)
[1-4/q/?] > '''
    ).lower()

    if betkind == 'q':  # quit
        print(f"you will be quitting the game with ${balance}")
        suretoquit = input("are you sure you want to quit [y/N]? ")
        print()
        if suretoquit == 'y':
            print("quitting...")
            break
        else:
            print("continuing the game...")
            continue

    if betkind == "?":  # help
        utils.help()
        input("ENTER to continue ")
        continue

    if betkind not in {'1', '2', '3', '4', '5', 'q', '?'}:
        print("please input a valid betkind.")
        print()
        continue

    print()

    # get user bet amount
    while True:
        bet = input("amount to bet (no decimals!!)\n> ")
        if not bet.isdigit():
            print("please input an integer.")
            print()
            continue
        bet = int(bet)
        break

    # check if balance is sufficient
    if bet > balance:
        print("if you lose this, you will end up in debt.")
        continuedebtrisk = input("are you sure you want to continue [y/N]: ").lower()
        if continuedebtrisk != 'y':
            print()
            continue

    # handle specific bet kinds
    if betkind == '1':  # even/odd
        while True:
            choice = input("[even] or [odd]?\n> ").lower()
            if choice not in {'even', 'odd'}:
                print("please input a valid choice.")
                print()
                continue
            break

        print(f"you bet ${bet} on {choice}")
        print()

        number = utils.spin()
        print()

        if utils.checkeven(number) == choice:
            payout = bet * 2

    elif betkind == '2':  # red/black
        while True:
            choice = input("[red] or [black]?\n> ").lower()
            if choice not in {'red', 'black'}:
                print("please input a valid choice.")
                print()
                continue
            break

        print(f"you bet ${bet} on {choice}")
        print()

        number = utils.spin()
        print()

        if utils.checkcolor(number) == choice:
            payout = bet * 2

    elif betkind == '3':  # low/high
        while True:
            choice = input("[low] or [high]?\n> ").lower()
            if choice not in {'low', 'high'}:
                print("please input a valid choice.")
                print()
                continue
            break

        number = utils.spin()
        print()

        if utils.checklow(number) == choice:
            payout = bet * 2

    elif betkind == '4':  # dozens
        while True:
            choice = input(
                '''choose:
1. 1-12
2. 13-24
3. 25-36
> '''
            ).lower()
            if choice not in {'1', '2', '3'}:
                print("please input a valid choice.")
                print()
                continue
            break

        number = utils.spin()
        print()

        if utils.checkdozens(number) == choice:
            payout = bet * 3

    elif betkind == '5':  # single number
        while True:
            choice = input("choose a number [00, 0-36]: ").lower().strip()
            if not choice.isdigit() or not (choice in logic.numbers or choice == '00'):
                print("please input a valid choice")
                print()
                continue
            break

        number = utils.spin()
        print()

        if number == int(choice):
            payout = bet * 36

    # update balance and display results
    if payout > 0:
        print(f"you won ${payout}!!!!!")
        balance += payout - bet
    else:
        print("you lost this bet...")
        balance -= bet
        print(f"${bet} deducted from your balance")
        print()

    print(f"your balance is ${balance}")
    print()
    input("ENTER to continue")
    print()
    print()

# final
print(f"your balance is ${balance}")
if balance > 1000:
    print(f"you won ${balance - 1000}!!")
elif balance < 1000:
    print(f"you lost ${1000 - balance}...")
else:
    print("you won nothing")
