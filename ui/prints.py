def print_choose_entity():
    print("1 - Players")
    print("2 - Clubs")
    print("3 - Agents")


def print_main():
    print("1 - New entity")
    print("2 - New random entities")
    print("3 - Show all")
    print("4 - Show one")
    print("5 - Update (id)")
    print("6 - Delete (id)")
    print("7 - Search")


def print_player(player):
    print('| ' + str(player[1]) + '| ' + player[0])
    print('| ' + player[2].strftime("%b %d, %Y") + ' | $' + str(player[3]) + "M | " + player[8].strip()+" | "+player[4]+" |\n")


def print_club(row):
    print('| ' + str(row[0]) + '| ' + row[1].strip())
    print('| ' + row[2] + ' | ' + row[3].strip() + ' | ' + str(row[4])+" |\n")


def print_agent(row):
    print('| ' + str(row[0]) + '| ' + row[1] + ' | $' + str(row[2]) + " |\n")
