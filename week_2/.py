import random

def flip_coin():
    return 'Heads' if random.randint(0, 1) == 0 else 'Tails'

print(flip_coin())