# 1

random = [1, 'one', 1.1]
print(random)


# 2 you index into the list and then index again

random = [1,1,[1,2]]
print(random[2][1])

# 3 it returns everything at and after index 1

random = ['a','b','c']
print(random[1:])

# 4

weekdays = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4}

# 5 you will get the number 2 back

# 6

random = [1,[2,3]]
random = (tuple(random))
print(random)

# 7

new = (set('Mississippi'))
print(new)

# 8 yes you can

new.add('X')
print(new)


# 9 output would be {1,2,3}


# Question
def test(a,b):
    answer = ''
    for number in range(a,b):
        if number % 7 == 0 and number % 5 != 0:
            answer += f'{number},'
    print(answer[:-1])

test(2000,3200)



# Question 2

def facto(number):
    answer = 1
    for i in range(1,number + 1):
        answer = answer*i

    return answer


# x = int(input('Please enter a number to check its factorial: '))
print("#-------------------------------------#")
print(facto(8))
print("#-------------------------------------#")


# question 3

def math(number):
    answer = {}
    for i in range(1,number+1):
        answer[i] = i*i
    return answer


# x = int(input('Enter a number to get a cool Dictionary '))
print(math(8))

#question 4

def lt(numbers):
    l = numbers.split(',')
    t = tuple(l)
    print(l)
    print(t)

lt("34,67,55,33,12,98")