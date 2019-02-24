for i in range(10):
    print(i)

for i in range(5):
    print(i)

for f in range(3):
    print(f)

for f in range (-2):
    print(f)

for y in range (1):
    print('blah')

for y in range (0):
    print('possible?')

for x in range (2):
    l = []

l = [4, 5, 6]
for i in l:
    print(i)

l = [2, 20, 7]
for i in l:
    print(i)

l = [2, 20, 7]
for i in l:
    if i < 10:
        print(i)

print('\n')

i = 8
while i > 0:
    print(i)
    i = i - 1

print('\n')

i = 8
while i < 12:
    print(i)
    i = i +1

print('\n')

i = 5
while i > 5:
    if i < 10:
        print(i)
        i = i + 1

print('\n')

i = 8
while True:
    if i <= 0:
        break
    i = i - 1

i = 8
while True:
    if i <=0:
        print(i)
        break
    i = i - 1

print('\n')

i = 8
while True:
    if i >= 10:
        print(i)
        break
    i = i + 1

print('\n')

i = 8
while True:
    if i >= 10 and i <= 15:
        print(i)
    i = i + 1
    if i > 15:
        break

print('\n')

i = 8
if i > 0:
    print("i is greater than zero")
else:
    print("i is less than or equal to zero")

print('\n')

i = 25
if i >= 10 and i <= 15:
    print(i)
else:
    print(i -1)

print('\n')

i = 8
if i > 0:
    print("i is greater than zero")
elif i < 4:
    print("i is between 0 and 4")
else:
    print("i is greater than or equal to four")

print('\n')

i = 8
if i * 5 < 20:
    print(i)
elif i / 5 > 2:
    print(i/5)
else:
    print("easy fix")

print('\n')

i = 9
while True:
    if i * 5 < 40:
        print(i)
    elif i / 3 > 2:
        break
    else:
        print("should have broke")


print('\n')

def my_function():
    i = 8
    if i > 0:
        print("i is greater than zero")
    elif i < 4:
        print("i is between 0 and 4")
    else:
        print("i is greater than or equal to four")

my_function()

def my_function():
    i = 8
    f = 7
    if i < f:
        print("i is less than f")
    elif i > f:
        print("i is greater than f")
    else:
        print("nothing to see here")

my_function()

def add(a, b):
    return a + b

a = 4
b = 7
def add(a, b):
    return 4 + 7


def add(a, b):
    a = 5.6
    b = 0.1
    return 5.6 + 0.1


def add(a, b):
    a = "my"
    b = "oh my"
    return "my" + "oh my"


def add(a, b):
    a = 3
    b = 9
    return a + b

print(add(a, b))

f = 2
g = 1

def subtract(f, g):
    f = f + 12
    g = g + 9
    return f - g

print(subtract(f,g))




