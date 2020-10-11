from sympy import *


def task_1():
    x = symbols('λ')
    formula = list()
    matrix = list()
    order_table = [0, 2, 1, 3]
    print("If there is no such argument, type 0 instead")
    while len(formula) < 4:
        number = input()
        try:
            val = int(number)
            formula.append(val)
        except ValueError:
            print("That is not an integer")
    for index in order_table:
        matrix.append(formula[index])

    exp1 = matrix[0] * matrix[3]
    exp2 = matrix[0] * -x
    exp3 = -x * matrix[3]
    exp4 = -x * -x
    ans = exp1 + exp2 + exp3 + exp4
    print(ans)


def task_2():
    vector = list()
    matrix = list()
    ans = list()
    print("first enter your matrix, then your vector")
    for i in range(6):
        if i < 4:
            number = input()
            try:
                val = int(number)
                matrix.append(val)
            except ValueError:
                print("That is not an integer")
        else:
            number = input()
            try:
                val = int(number)
                vector.append(val)
            except ValueError:
                print("That is not an integer")

    if vector[0] == 0 and vector[1] == 0:
        return true

    exp1 = (vector[0] * matrix[0]) + (vector[1] * matrix[2])
    exp2 = (vector[0] * matrix[1]) + (vector[1] * matrix[3])
    ans.append(exp1)
    ans.append(exp2)

    if ans[0] == 0 and ans[1] == 0:
        return true

    i = 0
    while i < 50:
        if i * ans[0] == vector[0] and i * ans[1] == vector[1]:
            return true
        i += 1

    return false


print(task_2())
