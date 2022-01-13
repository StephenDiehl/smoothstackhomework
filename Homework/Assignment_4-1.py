# 1

def func():
    print("Hello World")

# 2

def func1(name):
    print(f"Hi, My name is {name}")


# 3

def func3(x,y,z):
    if z == True:
        return x
    else:
        return y

# 4

def func4(x,y):
    return x*y


# 5

def is_even(number):
    if number % 2 != 0:
        return False
    else:
        return True

# 6

def two(a,b):
    if a > b:
        return True
    else:
        return False

# 7

def sum(*nums):
    answer = 0
    for number in nums:
        answer += number
    return answer


print(sum(1,2,3,4))
# 8

def evens(*nums):
    answer = [num for num in nums if num % 2 == 0]
    return answer

# 9

def case(word):
    new_word = ''
    for i in range(len(word)):
        if i % 2 == 0:
            new_word += word[i].upper()
        else:
            new_word += word[i].lower()

    print(new_word)



# 10

def greater(a,b):
    if a % 2 == 0 and b % 2 == 0 and a > b:
        return b
    elif a % 2 == 0 and b % 2 == 0 and a < b:
        return a
    else:
        if a > b:
            return a
        else:
            return b

# 11

def start(a,b):
    if a[0] == b[0]:
        return True
    else:
        return False

# 12

def square(x):
    return x**2

# 13

def randomcap(word):
    cap = ''
    for i in range(len(word)):
        if i == 0 or i == 3:
            cap += word[i].upper()
        else:
            cap += word[i]

    print(cap)


randomcap('eagle')