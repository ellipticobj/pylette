from randomorg_api import Generator

randgen = Generator("440f3a98-eacd-478e-9a52-d3f3504f49fc")

numbers = ['00'] + [str(i) for i in range(37)] # generates 00 to 36

rednumbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
blacknumbers = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

def getnumber():
    return randgen.choice(numbers)