from db.database import Database
from ui.prints import *
from ui.input_entity import *
from fill_db import RandomFillDB

db = Database('localhost', 'lab1')


def get_entity():
    while 1:
        print_choose_entity()
        i = choose_command()
        entities = {
            '1': 1,
            '2': 2,
            '3': 3
        }
        if i is 'q':
            break

        if i in entities:
            return entities[i]
        else:
            print("____________________")
            print("No such option, try again...")


def add_entity(entity_type, db):
    entities = {
        1: input_player,
        2: input_club,
        3: input_agent
    }

    if entity_type in entities:
        entities[entity_type](db)


def add_random(entity_type, db):
    random_fill = RandomFillDB(db)
    entities = {
        1: random_fill.add_n_players,
        2: random_fill.add_n_clubs,
        3: random_fill.add_n_agents
    }

    if entity_type in entities:
        entities[entity_type](check_input(input_num, "Please input number of entities to add: "))


def get_all(entity_type, db):
    entities = {
        1: db.get_players,
        2: db.get_clubs,
        3: db.get_agents
    }

    print_entities = {
        1: print_player_and_club,
        2: print_club,
        3: print_agent
    }

    if entity_type in entities:
        for entity in entities[entity_type]():
            print_entities[entity_type](entity)


def get_one(entity_type, db):
    entities = {
        1: db.get_player_id,
        2: db.get_club_id,
        3: db.get_agent_id
    }

    print_entity = {
        1: print_player_and_club,
        2: print_club,
        3: print_agent
    }
    if entity_type in entities:
        while True:
            try:
                id = int(input("Please input entity's id: "))
                entity = entities[entity_type](id)
                if entity is not None:
                    print_entity[entity_type](entity)
                    break
                raise ValueError
            except ValueError:
                print("Wrong id. Try again...")
                # continue


def update(entity_type, db):
    update_func = {
        1: update_player,
        2: update_club,
        3: update_agent
    }

    entities = {
        1: db.get_player_id,
        2: db.get_club_id,
        3: db.get_agent_id
    }

    if entity_type in update_func:
        while True:
            try:
                id = int(input("Please input entity's id: "))
                entity = entities[entity_type](id)
                if entity is None:
                    raise ValueError
                update_func[entity_type](db, id)
                break
            except ValueError:
                print("Wrong id. Try again...")


def delete(entity_type, db):
    delete_func = {
        1: db.delete_player,
        2: db.delete_club,
        3: db.delete_agent
    }

    entities = {
        1: db.get_player_id,
        2: db.get_club_id,
        3: db.get_agent_id
    }

    if entity_type in delete_func:
        while True:
            try:
                id = int(input("Please input entity's id: "))
                entity = entities[entity_type](id)
                if entity is None:
                    raise ValueError
                delete_func[entity_type](id)
                break
            except ValueError:
                print("Wrong id. Try again...")


def search(db):
    command = search_type()

    commands = {
        1: search_bool,
        2: search_range,
        3: search_text
    }

    if command in commands:
        commands[command](db)


def search_bool(db):
    condition = input("Is club plays at euro cups (True or False): ") == "True"
    for club in db.search_clubs_euro(condition):
        print_club(club)


def search_range(db):
    n1 = check_input(input_num, "Please input 1st number: ")
    n2 = check_input(input_num, "Please input 2nd number: ")
    print("  PlAYERS")
    for player in db.search_range_players(n1, n2):
        print_player_and_club(player)

    print("  AGENTS")
    for agent in db.search_range_agents(n1, n2):
        print_agent(agent)


def search_text(db):
    text = input("Please input smth that u need to find: ")
    if " " in text:
        text = text.replace(" ", " <-> ")
    for player in db.search(text):
        print_player(player)


def search_type():
    while 1:
        print_search()
        i = choose_command()
        entities = {
            '1': 1,
            '2': 2,
            '3': 3
        }
        if i is 'q':
            break

        if i in entities:
            return entities[i]
        else:
            print("____________________")
            print("No such option, try again...")
            continue


while True:
    print_main()
    command = choose_command()
    commands = {
        '1': add_entity,
        '2': add_random,
        '3': get_all,
        '4': get_one,
        '5': update,
        '6': delete
    }

    if command is 'q':
        break

    if command is '7':
        search(db)
        continue

    if command in commands:
        commands[command](get_entity(), db)
    else:
        print("____________________")
        print("No such option, try again...")
