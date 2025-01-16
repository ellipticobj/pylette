from randomorg_api import Generator

random = Generator("440f3a98-eacd-478e-9a52-d3f3504f49fc")

numbers = ['00'] + list(range(37)) # generates 00 to 36

def getnumber():
    return random.choice(numbers)


