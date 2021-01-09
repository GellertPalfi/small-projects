from sympy import *


def task1_calculator(matrix):
    x = symbols('λ')
    exp1 = matrix[0] * matrix[3]  # determinant calculations
    exp2 = matrix[0] * -x
    exp3 = -x * matrix[3]
    exp4 = -x * -x
    exp5 = matrix[1] * matrix[2]
    print(exp1 + exp2 + exp3 + exp4 - exp5)


def task2_calculator(matrix, vector):
    ans = []

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


def task3_calculator(matrix, coefficient):
    unit_matrix = [1, 0, 0, 1]

    ans_unit_matrix = [index * coefficient for index in unit_matrix]

    ans_matrix = list()
    for index in range(4):
        ans_matrix.append(matrix[index] - ans_unit_matrix[index])

    # calculate determinant
    determinant = (ans_matrix[0] * ans_matrix[3]) - (ans_matrix[1] * ans_matrix[2])

    print(not determinant)

