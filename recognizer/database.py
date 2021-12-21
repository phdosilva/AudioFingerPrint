import mysql.connector

from recognizer.mysql_commands import (CREATE_SONGS_TABLE)


class Database:

    def __init__(self, host="localhost", user="root", passwd="BHU*nji9"):
        self.mydb = mysql.connector.connect(
            host=host,
            user=user,
            passwd=passwd
        )

        self.cur = self.mydb.cursor()

    def setup(self):
        self.cur.execute("CREATE DATABASE IF NOT EXISTS SongsDatabase")
        self.cur.execute("USE SongsDatabase")

        self.cur.execute(CREATE_SONGS_TABLE)
        self.cur.execute("SHOW TABLES")
        for x in self.cur:
            print(x)

    def populate(self):
        pass