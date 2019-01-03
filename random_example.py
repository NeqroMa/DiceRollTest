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


"""

randint enables a result to be the biggest value while randrange can output only max-1 biggest value





"""


print(random.randrange(0,2)+1)
