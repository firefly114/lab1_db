import datetime


class Player:
    fullname = ''
    birth = None
    value = 0
    position = ''
    club_id = 0
    agent_id = 0

    def __init__(self, fullname='', birth=datetime.datetime.now(), value=0, position='NG', club_id=0, agent_id=0):
        self.fullname = fullname
        self.value = value
        self.position = position
        self.birth = birth
        self.club_id = club_id
        self.agent_id = agent_id
