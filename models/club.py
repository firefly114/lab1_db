class Club:
    title = ''
    coach = ''
    league = ''
    euro_cups = False

    def __init__(self, title='', coach='', league='', e_c=False):
        self.title = title
        self.coach = coach
        self.league = league
        self.euro_cups = e_c
