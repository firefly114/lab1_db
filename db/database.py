import psycopg2
import sys
import random
from string import punctuation

def print_player(player):
    print('Player №' + str(player[1]) + ': ' + player[0])
    print('     ' + player[2].strftime("%b %d, %Y") + ' | $' + str(player[3]))
    if player[5] is not None:
        print('     Club: ' + player[8] + ' | ' + player[4])


def print_club(row):
    print('Club №' + str(row[0]) + ': ' + row[1])
    print('     ' + row[2] + ' | ' + row[3])
    print('     Euro cups: ' + str(row[4]))


class Database:

    def __init__(self, host, db):
        self.host = host
        self.db = db
        self.conn = None
        self.cur = None

        self.connect('postgres', '1234')

    def connect(self, username, password):
        try:
            self.conn = psycopg2.connect(host=self.host, dbname=self.db, user=username, password=password)
            self.cur = self.conn.cursor()
        except (Exception, psycopg2.DatabaseError) as e:
            print("error")
            sys.exit(1)
        print("ok")

    def close(self):
        self.cur.close()
        self.conn.close()

    def get_players(self):
        self.cur.execute("SELECT * from players INNER JOIN clubs ON players.club_id=clubs.id ORDER BY players.id")
        rows = self.cur.fetchall()
        # for row in rows:
        #     print_player(row)
        return rows

    def get_clubs(self):
        self.cur.execute("SELECT * from clubs Where id > 0 ORDER BY clubs.id")
        rows = self.cur.fetchall()
        # for row in rows:
        #     print_club(row)
        return rows

    def get_agents(self):
        self.cur.execute("SELECT * from agents Where id > 0 ORDER BY agents.id")
        rows = self.cur.fetchall()
        # for row in rows:
        #     print('Agent №' + str(row[0]) + ': ' + row[1] + ' | $' + str(row[2]))
        return rows

    def get_player_id(self, pid):
        self.cur.execute("SELECT * from players INNER JOIN clubs ON players.club_id=clubs.id WHERE players.id = " + str(pid))
        row = self.cur.fetchone()
        if not row:
            print('error_player_id')
            return
        # print_player(row)
        return row

    def get_club_id(self, cid):
        self.cur.execute("SELECT * from clubs WHERE id = " + str(cid))
        row = self.cur.fetchone()
        # print_club(row)
        if not row:
            print('error_club_id')
            return
        return row

    def get_agent_id(self, aid):
        self.cur.execute("SELECT * from agents WHERE id = " + str(aid))
        row = self.cur.fetchone()
        # print('Agent №' + str(row[0]) + ': ' + row[1] + ' | $' + str(row[2]))
        if not row:
            print('error_agent_id')
            return
        return row

    def get_random_club_id(self):
        self.cur.execute("SELECT clubs.id from clubs Where clubs.id > 0 ORDER BY clubs.id")
        rows = self.cur.fetchall()
        id = rows[random.randint(0, len(rows)-1)]
        return int(''.join(c for c in str(id) if c not in punctuation))

    def get_random_agent_id(self):
        self.cur.execute("SELECT agents.id from agents Where agents.id > 0 ORDER BY agents.id")
        rows = self.cur.fetchall()
        id = rows[random.randint(0, len(rows)-1)]
        return int(''.join(c for c in str(id) if c not in punctuation))
    # def get_player_name(self, name):
    #     self.cur.execute(f"SELECT * from players WHERE fullname = '{name}'")
    #     row = self.cur.fetchone()
    #     if not row:
    #         print('error_player_name')
    #         return
    #     print_player(row)
    #
    # def get_club_name(self, name):
    #     self.cur.execute(f"SELECT * from clubs WHERE title = '{name}'")
    #     row = self.cur.fetchone()
    #     if not row:
    #         print("error_club_name")
    #         return
    #     print_club(row)
    #
    # def get_agent_name(self, name):
    #     self.cur.execute(f"SELECT * from agents WHERE fullname = '{name}'")
    #     row = self.cur.fetchone()
    #     print('Agent №' + str(row[0]) + ': ' + row[1] + ' | $' + str(row[2]))

    def new_player(self, player):
        self.cur.execute(f"INSERT INTO players (fullname, birth, pos, market_value, club_id, agent_id) \
        VALUES('{player.fullname}','{player.birth}','{player.position}',{player.value}, {player.club_id}, {player.agent_id})")
        self.conn.commit()

    def new_club(self, club):
        self.cur.execute(f"INSERT INTO clubs (title, coach, league, euro_cups) \
        VALUES('{club.title}', '{club.coach}', '{club.league}', '{club.euro_cups}')")
        self.conn.commit()

    def new_agent(self, agent):
        self.cur.execute(f"INSERT INTO agents (fullname, salary) \
        VALUES('{agent.fullname}','{agent.salary}')")
        self.conn.commit()

    def update_player(self, player, pid):
        self.cur.execute(f"UPDATE players SET market_value = {player.value},"
                         f" pos = '{player.position}',"
                         f" club_id = {player.club_id},"
                         f" agent_id = {player.agent_id} \
        where players.id = {pid}")
        self.conn.commit()

    def update_club(self, club, cid):
        self.cur.execute(f"UPDATE clubs SET coach = '{club.coach}', "
                         f"league = '{club.league}', "
                         f"euro_cups = {club.euro_cups} \
                         where clubs.id = {cid}")
        self.conn.commit()

    def update_agent(self, agent, aid):
        self.cur.execute(f"UPDATE agents SET salary = {agent.salary} \
                                 where agents.id = {aid}")
        self.conn.commit()

    def delete_player(self, pid):
        self.cur.execute("DELETE from players where players.id = " + str(pid))
        self.conn.commit()

    def delete_club(self, cid):
        self.cur.execute("DELETE FROM clubs where clubs.id = " + str(cid))
        self.cur.execute("UPDATE players SET club_id = 0 where club_id = " + str(cid))
        self.conn.commit()

    def delete_agent(self, aid):
        self.cur.execute("DELETE FROM agents where agents.id = " + str(aid))
        self.cur.execute("UPDATE players SET agent_id = 0 where agent_id = " + str(aid))
        self.conn.commit()
