import sqlite3
import logging
import random

MALE = '1'
FEMALE = '0'
BI = '10'

class Bottle:
    def __init__(self):
        self.males = ["Андрей",
                      "Александр",
                      "Антон",
                      "Борис",
                      "Данил",
                      "Денис",
                      "Евгений",
                      "Константин",
                      "Павел"]

        self.females = ["Анна",
                        "Анастасия",
                        "Валентина",
                        "Екатерина",
                        "Мария" ]

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


    @property
    def rnd(self):
        quantity = len(self.gamers)
        return random.randint(1, quantity)

    def phrases(self):
        pass


