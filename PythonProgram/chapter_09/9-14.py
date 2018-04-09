from random import randint


class Die():
    def __init__(self, side=6):
        self.side = side

    def roll_die(self):
        x = randint(1, self.side)
        print(x)


die = Die()
for i in range(10):
    die.roll_die()
print("-" * 50)

die10 = Die(side=10)
for i in range(10):
    die10.roll_die()
print("-" * 50)


die20 = Die(side=20)
for i in range(10):
    die20.roll_die()
