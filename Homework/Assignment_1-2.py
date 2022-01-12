import math
# Number 1

def add(a,b):
    print(a+b)
def subtract(a,b):
    print(a-b)
add(50,50)
subtract(100,10)

# or

print(50+50)
print(100-10)


# Number 2

# print(30 + *6) doesnt work as *6 isn't valid syntax

print(6^6)
print(6**6)
print(6+6+6+6+6+6)


# Number 3

hello = "Hello World"
print(hello)
print(hello + " : 10")


# Number 4

loan = 800000
interest = .06/12
plus = interest + 1
length = 103
x = interest * (plus**103.0)
y = (plus**103) - 1
z = x / y
print(math.ceil(loan * z))


