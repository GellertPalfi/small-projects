import json

from object_scraper.definiton_scraper import definition_maker


def check_for_updates():
    try:
        current_definitions = [definition["name"] for definition in read_json()]
    except TypeError:
        return

    new_definitons = [definition for definition in definition_maker()]
    definitions_toadd = []

    for new in new_definitons:
        is_found = False
        for old in current_definitions:
            if new.name == old:
                is_found = True
                break

        if not is_found:
            definitions_toadd.append(new)

    if not definitions_toadd:
        print("no new definitions found, returning to main menu\n")
    else:
        print(f"found {len(definitions_toadd)} new definitions.\n")
        while True:
            choice = input("What would you like to do?\n"
                           "l: list them\n"
                           "u: add them to the .json file\n"
                           "b: go back\n")

            if choice == 'l':
                for index in definitions_toadd:
                    print(index)
            elif choice == 'u':
                update_json()
            elif choice == 'b':
                break


def read_json():
    """
    reading the currently stored definitions
    """
    try:
        with open('definitions.json', 'r') as file:
            definitions = json.load(file)
            return definitions
    except IOError:
        print("file not found. Maybe check for new definitions first?\n")
        return


def update_json():
    """
    adding definitions which are not in the .json file
    """
    pass

def write_json():
    """
    overwriting the current .json file with the trending definitions
    """
    with open('definitions.json', 'w') as file:
        file.write('[\n' + ',\n'.join(json.dumps(definition.__dict__) for definition in definition_maker()) + '\n]\n')

    print("definitions succesfully overwritten\n")


def list_definition():
    definitons = read_json()
    if not definitons:
        return

    def next_item():
        i = 0
        while i < len(definitons):
            yield definitons[i]
            i += 1

    while True:
        index = next_item()
        choice = input("a: list all\n"
                       "o: list the first one\n"
                       "b: go back\n")
        if choice == 'a':
            for definiton in definitons:
                print(definiton)
            print("\n")

        elif choice == 'o':
            print(next(index))
            while True:

                sublist_choice = input("n: list the next one\n"
                                       "b: go back\n")

                if sublist_choice == 'n':
                    print(next(index))
                elif sublist_choice == 'b':
                    break

        elif choice == 'b':
            break
