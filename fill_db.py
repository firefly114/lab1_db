from models.club import Club
from models.agent import Agent
from models.player import Player
from db.database import Database
from randomize import *


class RandomFillDB:

    db = None

    def __init__(self, db):
        self.db = db

    def add_n_players(self, n):
        for x in range(0, n):
            self.add_player()

    def add_player(self):
        self.db.new_player(Player(
            rnd_fullname(), rnd_date(),
            rnd_value(), rnd_pos(),
            self.db.get_random_club_id(), self.db.get_random_agent_id()
        ))

    def add_n_clubs(self, n):
        for x in range(0, n):
            self.add_club()

    def add_club(self):
        self.db.new_club(
            Club(rnd_club(), rnd_fullname(), rnd_league(), rnd_bool()))

    def add_n_agents(self, n):
        for x in range(0, n):
            self.add_agent()

    def add_agent(self):
        self.db.new_agent(
            Agent(rnd_fullname(), rnd_salary()))
