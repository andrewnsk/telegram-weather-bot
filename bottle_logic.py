import sqlite3
import logging
import random

MALE = '1'
FEMALE = '0'
BI = '10'


class Bottle:
    def __init__(self):
        self.males = [
            "Андрей",
            "Александр",
            "Антон",
            "Борис",
            "Данил",
            "Денис",
            "Евгений",
            "Константин",
            "Павел"
        ]

        self.females = [
            "Анна",
            "Анастасия",
            "Валентина",
            "Екатерина",
            "Мария"
        ]

        self.gamers = [
            "Андрей",
            "Александр",
            "Антон",
            "Борис",
            "Данил",
            "Денис",
            "Евгений",
            "Константин",
            "Павел",
            "Анна",
            "Анастасия",
            "Валентина",
            "Екатерина",
            "Мария"
        ]

        self.phrases = [
            "нежно целует в щечку",
            "целует взасос",
            "шлепает по попке"

        ]

        self.db_connection = sqlite3.connect(":memory:")
        self.db_connection.isolation_level = None
        self.cur = self.db_connection.cursor()
        self.cur.execute('''CREATE TABLE players
                            (id INTEGER PRIMARY KEY, name TEXT, gender TEXT, flags INTEGER, description TEXT)''')
        self.db_connection.commit()

    def define_gender(self, name):
        if name not in self.males:
            return FEMALE
        elif name not in self.females:
            return MALE
        else:
            return BI

    def players(self, names):

        self.db_connection = sqlite3.connect(":memory:")
        self.db_connection.isolation_level = None
        self.cur = self.db_connection.cursor()

        for human in names:
            self.cur.execute('''INSERT INTO bot(name, gender)
                            VALUES(?,?,?,?)''', (human, self.define_gender(human)))

    @staticmethod
    def rnd(obj):
        quantity = len(obj)
        return random.randint(0, quantity - 1)

    def kiss(self):
        self.rnd(self.phrases)


new_game = Bottle()
kissed = new_game.rnd(new_game.gamers)
print(kissed)
gamer = new_game.gamers[kissed]
print(gamer)

if gamer[-1:] == 'я':
    gamered = gamer[:len(gamer) - 1] + 'ю'
elif gamer[-1:] == 'й':
    gamered = gamer[:len(gamer) - 1] + 'я'
elif gamer[-1:] == 'а':
    gamered = gamer[:len(gamer) - 1] + 'у'
elif gamer[-1:] == 'р':
    gamered = gamer + 'а'

else:
    gamered = gamer

print(gamered)





