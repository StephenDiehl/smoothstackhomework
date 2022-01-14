def bmi(amount, *args):
    weight_list = [item for item in args]
    final_list = []
    temp = amount
    bmi = 0
    answer = ''
    while temp != 0:
        final_list.append([weight_list[0],weight_list[1]])
        weight_list.pop(0)
        weight_list.pop(0)
        temp -= 1
    for i in range(amount):
        bmi = final_list[i][0]/final_list[i][1]**2
        if bmi >= 30:
            answer += 'obese '
        elif bmi < 30 and bmi >= 25:
            answer += 'over '
        elif bmi < 25 and bmi >= 18.5:
            answer += 'normal '
        else:
            answer += 'under '
    return(answer[:-1])
