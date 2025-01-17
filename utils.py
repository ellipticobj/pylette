import logic

def help():
    print(
'''
rules of the game:

you start with a balance of 1000

every round, a number is randomly generated. 

you get to place a bet, shown in the list below:

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