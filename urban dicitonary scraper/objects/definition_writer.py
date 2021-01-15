import json

from object_scraper.definiton_scraper import definition_maker


def check_for_updates():
    """
    checking if any new definitions exist and adding them if user requests
    """
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
                update_json(definitions_toadd)
                break
            elif choice == 'b':
                break


def read_json():
    """
    reading the currently stored definitions
    """
    try:
        with open('definitions.json', 'r', encoding='utf8') as file:
            try:
                definitions = json.load(file)
                return definitions
            except json.decoder.JSONDecodeError:
                print("file is empty. Try checking for new definitions first\n")

    except IOError:
        print("file not found. Try checking for new definitions first\n")
        return


def update_json(definitions):
    """
    adding definitions which are not in the .json file
    """
    current = read_json()
    for i in range(len(definitions)):
        current.append(definitions[i].__dict__)

    with open('definitions.json', 'w') as file:
        file.write('[\n' + ',\n'.join(json.dumps(definition) for definition in current) + '\n]\n')

    print("definitions successfully added, returning to main menu\n")


def write_json():
    """
    overwriting the current .json file with the trending definitions
    """
    with open('definitions.json', 'w', encoding='utf8') as file:
        file.write('[\n' + ',\n'.join(json.dumps(definition.__dict__, ensure_ascii=False) for definition in definition_maker()) + '\n]\n')

    print("definitions successfully written into .json file\n")


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
                print(f'{definiton["name"]} \n'
                      f'{definiton["meaning"]}\n'
                      f'{definiton["example"]}\n'
                      f'likes:{definiton["likes"]}|dislikes:{definiton["dislikes"]}\n')
            print("\n")

        elif choice == 'o':
            print(next(index))
            while True:
                try:

                    sublist_choice = input("n: list the next one\n"
                                           "b: go back\n")

                    if sublist_choice == 'n':
                        print(next(index))
                    elif sublist_choice == 'b':
                        break
                except StopIteration:
                    print("No more definitions to print, returning to list menu")
                    break

        elif choice == 'b':
            break
