import random
import datetime
import names


def rnd_fullname():
    return names.get_full_name(gender='male')


def rnd_date():
    return datetime.datetime(random.randint(1990, 2018), random.randint(1, 12), random.randint(1, 30))


def rnd_value():
    return random.randint(5, 300)


def rnd_salary():
    return random.randint(1, 30)


def rnd_club():
    file = open("clubs.txt", "r")
    clubs = file.readlines()
    return clubs[random.randint(0, len(clubs)-1)].strip()


def rnd_league():
    file = open("leagues.txt", "r")
    leagues = file.readlines()
    return leagues[random.randint(0, len(leagues)-1)].strip()


def rnd_pos():
    file = open("positions.txt", "r")
    positions = file.readlines()
    return positions[random.randint(0, len(positions)-1)].strip()


def rnd_bool():
    return random.randint(0, 1) == 0
