from datetime import datetime


def input_club_id(str, db):
    id = int(input(str))
    if db.get_club_id(id) is not None:
        return id
    raise ValueError


def input_agent_id(str, db):
    id = int(input(str))
    if db.get_agent_id(id) is not None:
        return id
    raise ValueError


def input_player_id(str, db):
    id = int(input(str))
    if db.get_player_id(id) is not None:
        return id
    raise ValueError


def choose_command():
    return input("Choose command: \n")


def input_num(str):
    return int(input(str))


def input_date(str):
    return datetime.strptime(input(str), '%d-%m-%Y')


def input_range():
    n1 = input("Input first number: ")
    n2 = input("Input last number: ")
    # check numbers
    arr = {n1, n2}
    return arr
