from ui.input import *
from models.club import Club
from models.agent import Agent
from models.player import Player


def check_input(cb, helpstr, db=None):
    while True:
        try:
            if db is not None:
                return cb(helpstr, db)
            return cb(helpstr)
        except ValueError:
            print("Try again...")
            continue


def input_player(db):
    print("Input required values and press enter...")
    p = Player()
    p.fullname = input("Fullname: ")
    p.position = input("Position: ")

    p.birth = check_input(input_date, "Date of birth (dd-mm-yyyy): ")

    p.value = check_input(input_num, "Market value: ")
    # print clubs
    p.club_id = check_input(input_club_id, "Please input club id that exists or 0: ", db)
    # print agents
    p.agent_id = check_input(input_agent_id, "Please input agent id that exists or 0: ", db)
    db.new_player(p)


def input_club(db):
    print("Input required values and press enter...")
    c = Club()
    c.title = input("Title: ")
    c.coach = input("Coach: ")
    c.league = input("League: ")
    c.euro_cups = input("Is club plays at euro cups (True or False): ") == "True"
    db.new_club(c)


def input_agent(db):
    print("Input required values and press enter...")
    a = Agent()
    a.fullname = input("Fullname: ")
    a.salary = check_input(input_num, "Salary: ")
    db.new_agent(a)


def update_player(db, id):
    # select cols to update
    # input(col)
    player = db.get_player_id(id)
    print("Input required values and press enter...")
    new_p = Player()
    inp = input("Position: ")
    new_p.position = inp if inp is not '' else player[4]

    new_p.value = check_input(input_num, "Market value: ")
    # print clubs
    new_p.club_id = check_input(input_club_id, "Please input club id: ", db)
    # print agents
    new_p.agent_id = check_input(input_agent_id, "Please input agent id: ", db)
    db.update_player(new_p, id)


def update_club(db, id):
    club = db.get_club_id(id)

    print("Input required values and press enter...")
    new_c = Club()
    inp = input("Coach: ")
    new_c.coach = inp if inp is not '' else club[2]
    inp = input("League: ")
    new_c.league = inp if inp is not '' else club[3]
    inp = input("Is club plays at euro cups (True or False): ")
    new_c.euro_cups = inp == "True" if inp is not '' else club[4]
    db.update_club(new_c, id)


def update_agent(db, id):
    print("Input required values and press enter...")
    new_a = Agent()
    new_a.salary = check_input(input_num, "Salary: ")
    db.update_agent(new_a, id)
