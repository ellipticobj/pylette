import logic

def help():
    print(
f'''
rules of the game:

you start with a balance of 1000

every round, a number is randomly generated. 

you get to place a bet, shown in the list below:

even or odd: 
you bet whether the number will be even or odd
the payout for this is 2x (you get your bet if you win)

low or high:
you bet whether the number will be in the range 1-12 or 13-36
the payout for this is 2x

red or black:
you bet whether the number will be red or black
the payout for this is 2x

red numbers: {logic.rednumbers}
black numbers: {logic.blacknumbers}

dozens:
you bet whether the number will be in the ranges 1-12, 13-24 or 25-36
the payout is 3x (you win 2x what you bet)

single number:
you bet on a single number
the payout is 36x
'''
        )
    
def spin() -> str:
    print("spinning the wheel...")
    number = logic.getnumber()
    print(f"the number is: {number}")
    
    return int(number)

def checkeven(number: int) -> str:
    if int(number) % 2 == 1 or number in {'0', '00'}:
        return 'odd'
    return 'even'

def checkcolor(number: int) -> str:
    if number in logic.rednumbers:
        return 'red'
    elif number in logic.blacknumbers:
        return 'black'
    else:
        return ''
    
def checklow(number: int) -> str:
    if number in range(start=1, stop=19):
        return 'low'
    elif number in range(start=19, stop=37):
        return 'high'
    
def checkdozens(number: int) -> str:
    # 1: 1-12
    # 2: 13-24
    # 3: 25-36
    if number in range(start=1, stop=13):
        return '1'
    elif number in range(start=13, stop=25):
        return '2'
    elif number in range(start=25, stop=36):
        return '3'