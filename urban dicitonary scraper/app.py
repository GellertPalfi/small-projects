
from objects.definition_writer import *


def menu():
    while True:
        print("What would you like to do?")
        choice = input("l: list currently stored definitions\n"
                       "c: update definitions(only works if you already parsed them)\n"
                       "w: parse definitions(overrides current one)\n"
                       "q: quit\n")

        if choice == 'l':
            list_definition()
        elif choice == 'z':
            read_json()
        elif choice == 'c':
            check_for_updates()
        elif choice == 'w':
            write_json()
        elif choice == 'q':
            break


if __name__ == '__main__':
    menu()
