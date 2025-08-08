from multiprocessing import connection
import os
import sqlite3


class DB:

    def __init__(self):
        self.connection = sqlite3.connect("Human_DB")
        self.cur = self.connection.cursor()

        if os.path.exists("Human_DB"):
            print("DB Connected")
            if not self.DoesTableExist():
                self.CreateTable()

    def DoesTableExist(self):
        command = "SELECT name FROM sqlite_master WHERE type='table' AND name='person';"
        res = self.cur.execute(command)
        if res.fetchone() != None:
            return True
        return False

    def CreateTable(self):
        command = "CREATE TABLE IF NOT EXISTS person(person_id INTEGER PRIMARY KEY, first_name TEXT NOT NULL, last_name TEXT NOT NULL, email TEXT NOT NULL UNIQUE CHECK(email LIKE '%@%'), phone TEXT UNIQUE);"
        res = self.cur.execute(command)
        self.connection.commit()

        print("DB created")
        res.fetchone()

    def CreateEntry(self, personData):
        print(type(personData))
        command = (
            "INSERT INTO person (first_name,last_name,email,phone) VALUES (?,?,?,?);"
        )

        self.cur.execute(
            command,
            (
                personData.firstName,
                personData.lastName,
                personData.email,
                personData.phone,
            ),
        )
        self.connection.commit()

    def GetAllEntry(self):
        command = "SELECT * FROM person"
        self.cur.execute(command)

        people = self.cur.fetchall()
        for x in people:
            print(x)

    def GetEntryByID(self, id):
        command = "SELECT * FROM person WHERE person_id=?;"
        self.cur.execute(command, id)
        return self.cur.fetchall()

    def Update(self, updateData, id):
        command = "UPDATE person SET first_name = ?, last_name = ?, email = ?, phone = ? WHERE person_id = ?;"
        self.cur.execute(
            command,
            (
                updateData.firstName,
                updateData.lastName,
                updateData.email,
                updateData.phone,
                int(id),
            ),
        )
        self.connection.commit()
