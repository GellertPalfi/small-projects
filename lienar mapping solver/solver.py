from sympy import *

from calculations import *


def task_1():
    for i in range(3):  # every task has 3 subtasks
        formula = []
        matrix = []
        # used for getting values to the right spot, because we read x y x y, but we need x x y y order
        order_table = [0, 2, 1, 3]

        print("Enter your formula, if there is no such index, type 0 instead")
        while len(formula) < 4:
            number = input()
            try:
                val = int(number)
                formula.append(val)
            except ValueError:
                print("That is not an integer")

        for index in order_table:
            matrix.append(formula[index])

        task1_calculator(matrix)


def task_2():
    for i in range(3):  # every task has 3 subtasks
        vector = []
        matrix = []
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

        task2_calculator(matrix, vector)


def task_3():
    for i in range(3):
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

        task3_calculator(matrix, coefficient)


while true:
    print("which task would you like to do?(press q to exit)")
    choice = input()
    if choice == '1':
        task_1()
    elif choice == '2':
        task_2()
    elif choice == '3':
        task_3()
    elif choice == 'q':
        break
