# import random

# coin = random.choice(["heads", "tails"])
# print(coin)

# from random import choice

# coin = choice(["heads", "tails"])
# print(coin)

# import random

# coin = random.randint(1, 10)
# print(coin)

import random

cards = ["Jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)
