from functools import reduce
def accounting():
    orders = [["34587", "Learning Python, Mark Lutz", 4, 40.95], ["98762", "Programming Python, Mark Lutz", 5, 56.80], ["77226", "Head First Python, Paul Barry", 3, 32.95] ,["88112", "Einführung in Python3, Bernd Klein", 3, 24.99]]
    return list(map(lambda x: x if x[1] >= 100 else (x[0], x[1] + 10), map(lambda x: (x[0],int(x[2] * x[3])), orders)))







def accountingv2():
    orders = [["34587", ("Learning Python, Mark Lutz", 4, 40.95)], ["98762", ("Programming Python, Mark Lutz", 5, 56.80)], ["77226", ("Head First Python, Paul Barry", 3, 32.95)] ,["88112", ("Einführung in Python3, Bernd Klein", 3, 24.99)]]
    total = list(map(lambda x: [x[0]] + list(map(lambda y: int(y[1]*y[2]), x[1:])), orders))
    total = list(map(lambda x: [x[0]] + [reduce(lambda a,b: a + b, x[1:])], total))
    return list(map(lambda x: x if x[1] >= 100 else (x[0], int(x[1] + 10)), total))

