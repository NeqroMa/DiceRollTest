import random


# pick a random number from 0 to n-1
n = 10
my_rand = random.randrange(n)
print(my_rand)

a = 2
b = 5
my_rand2 = random.randint(a,b)
my_rand3 = random.randrange(a,b)
print( f'{my_rand2} vs {my_rand3}')

my_rand4 = random.randrange(10) + 1
print(my_rand4)

# TODO: figure out the difference between rand2 and rand3


# TODO: how is rand4 different from my_rand?
