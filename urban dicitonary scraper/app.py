from object_scraper.definiton_scraper import definition_maker
from objects.definition_writer import *


def menu():
    while True:
        print("What would you like to do?")
        choice = input("l: list currently stored definitions\n"
                       "c: check for new definitions\n"
                       "w: write definitions into .json file(overrides current one)\n"
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


menu()
