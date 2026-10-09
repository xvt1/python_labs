import random
from math import sqrt
from math import *
import statistics as st

from random import *

from datetime import datetime, date

import demo

a = 81
print(sqrt(a))

grades = [7,2,4,6,2,4,8,11,12,4,6,7]

print(f'Середній бал: {st.mean(grades)}')

radius = 5
print(f'Площа круга: {round((pi * pow(radius, 2)),2)}')


b = 2.456435632216146323

print(ceil(b))
print(floor(b))


balls = 25
items = 6

print(f'{floor(balls/items)}')
print(f'{ceil(balls / items)}')

numbers = []

for i in range(10):
    numbers.append(randint(1,100))

print(numbers)

print(choice(numbers))


print(f'Сьогодні: {datetime.today()}')
print(f'Сьогодні: {datetime.now()}')

new_year = date.today().year

print(demo.sqaure(5))
print(demo.average(numbers))