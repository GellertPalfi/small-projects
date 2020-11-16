from sympy import *


def task_1():
    for k in range(3):  # every task has 3 subtasks
        x = symbols('λ')
        formula = list()
        matrix = list()
        # used for getting values to the right spot, because we read x y x y, but we need x x y y order
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

        exp1 = matrix[0] * matrix[3]  # determinant calculations
        exp2 = matrix[0] * -x
        exp3 = -x * matrix[3]
        exp4 = -x * -x
        exp5 = matrix[1] * matrix[2]
        ans = exp1 + exp2 + exp3 + exp4 - exp5
        print(ans)


def task_2():
    vector = list()
    matrix = list()
    ans = list()
    index = 0

    print("first enter your matrix, then your vector")
    while index < 6:
        if index < 4:
            number = input()
            try:
                val = int(number)
                matrix.append(val)
                index += 1
            except ValueError:
                print("That is not an integer")
        else:
            number = input()
            try:
                val = int(number)
                vector.append(val)
                index += 1
            except ValueError:
                print("That is not an integer")

    if vector[0] == 0 and vector[1] == 0:  # if vector == null vector, the task is always true
        return print(true)

    exp1 = (vector[0] * matrix[0]) + (vector[1] * matrix[2])
    exp2 = (vector[0] * matrix[1]) + (vector[1] * matrix[3])
    ans.append(exp1)
    ans.append(exp2)

    if ans[0] == 0 and ans[1] == 0:  # same principle as above, answer is always true if it is the null vector
        return print(true)

    index = -20  # the task always uses small numbers, hence the [-20,20]
    while index < 20:
        if index * vector[0] == ans[0] and index * vector[1] == ans[1]:
            return print(true)
        index += 1

    return print(false)


def task_3():
    index = 0
    coefficient = 0  # task uses lambda, but i cant because of built in function
    matrix = list()
    unit_matrix = [1, 0, 0, 1]

    print("first enter your matrix, then your lambda")
    while index < 5:
        if index < 4:
            number = input()
            try:
                val = int(number)
                matrix.append(val)
                index += 1
            except ValueError:
                print("That is not an integer")
        else:
            number = input()
            try:
                val = int(number)
                coefficient = val
                index += 1
            except ValueError:
                print("That is not an integer")

    ans_unit_matrix = [i * coefficient for i in unit_matrix]

    ans_matrix = list()
    for index in range(4):
        ans_matrix.append(matrix[index] - ans_unit_matrix[index])

    # calculate determinant
    determinant = (ans_matrix[0] * ans_matrix[3]) - (ans_matrix[1] * ans_matrix[2])

    return print(not determinant)


task_1()
for i in range(3):
    task_2()
for i in range(3):
    task_3()
