import random, math
# 1

def find(a,b):
    print([i for i in range(a,b+1) if i % 7 == 0 and i % 5 ==0])

find(1500,2700)

# 2


def fctocf(c,f):
    celsius = (f-32)*5/9
    print(f"{c}C is {int((c * 9 / 5) + 32)} in Farenheit")
    print(f"{f}F is {int((f-32)*5/9)} in Celsius")





# 3

def guess():
    number = random.randint(1,9)
    guessed = False
    while not guessed:
        guess = int(input('Take a guess as to what number it is? '))
        if guess == number:
            print("Congratulations you guessed correctly!")
            guessed = True
        else:
            print("Good try but you didnt get it try again!")

# 4 and 5

def build(columns):
    while columns != 0:
        for i in range(1,int(columns/2 + 1)):
            print('*' * i)
        columns = int(columns/2 +1)
        for i in reversed(range(1,columns+1)):
            print('*' *i)
        columns = 0

# 6

def rev():
    word = input('Hey give me a word and I will reverse it! ')
    print(word[::-1])

# 7

def counting(numbers):
    even = [num for num in numbers if num % 2 == 0]
    odd = [num for num in numbers if num % 2 != 0]
    print(f"Number of even numbers: {len(even)}")
    print(f"Number of odd numbers: {len(odd)}")


# 8

datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

for item in datalist:
    print(f" {item}  is a {type(item)}")


# 9

for i in range(0,7):
    if i == 3 or i == 6:
        continue
    print(i)