from calendar import c
from datetime import datetime
import pathlib
import sqlite3
from unicodedata import numeric
from rezervari import Rezervari


class DataBase:
    def __init__(self, connection):
        self.conn = sqlite3.connect(connection)

# Create cars table

    def car_table_db(self):
        self.conn.cursor()
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS masini (
            id INTEGER PRIMARY KEY,
            marca TEXT NOT NULL,
            model TEXT NOT NULL,
            an_fabricatie INTEGER NOT NULL,
            tip_caroserie TEXT NOT NULL,
            serie_sasiu TEXT NOT NULL,
            numar_inmatriculare TEXT NOT NULL
        )
            """)
        self.conn.commit()

# Create customers table
    def client_table_db(self):
        self.conn.cursor()
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS clienti (
            id INTEGER PRIMARY KEY,
            nume TEXT NOT NULL,
            prenume TEXT NOT NULL,
            cnp INTEGER NOT NULL,
            adresa TEXT NOT NULL,
            telefon INTEGER NOT NULL,
            email TEXT NOT NULL
        )
            """)
        self.conn.commit()

# Create reservations table

    def reservations_table_db(self):
        self.conn.cursor()
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS rezervare (
            id INTEGER PRIMARY KEY,
            data_start DATE,
            data_end DATE,
            client_id INTEGER,
            masina_id INTEGER,
            FOREIGN KEY (client_id) REFERENCES clienti(id),
            FOREIGN KEY (masina_id) REFERENCES masini(id)
        )
            """)

        self.conn.commit()

# Insert cars into 'masini' table

    def add_car_db(self, car_db):
        self.conn.cursor()
        self.conn.execute("""INSERT INTO masini (marca, model, an_fabricatie, tip_caroserie, serie_sasiu, numar_inmatriculare) VALUES (?,?,?,?,?,?)""", (
            car_db["marca"], car_db["model"], car_db["an_fabricatie"], car_db["tip_caroserie"], car_db["serie_sasiu"], car_db["numar_inmatriculare"]))
        self.conn.commit()

# Insert customers into 'clienti' table
    def add_client_db(self, client_db):
        self.conn.cursor()
        self.conn.execute("""INSERT INTO clienti (nume, prenume, cnp, adresa, telefon, email) VALUES (?,?,?,?,?,?)""", (
            client_db["nume"], client_db["prenume"], client_db["cnp"], client_db["adresa"], client_db["telefon"], client_db["email"]))
        self.conn.commit()

# Insert reservations into 'rezervare' table'
    def add_reservation_db(self, reservation_db):
        self.conn.cursor()
        self.conn.execute("""INSERT INTO rezervare (data_start,data_end,client_id,masina_id) VALUES (?,?,?,?)""", (
            reservation_db["data_start"], reservation_db["data_end"], reservation_db["client_id"], reservation_db["masina_id"]))
        self.conn.commit()

# Select all cars saved into 'masini' table and print only indexes 0, 1, 2, 6
    def read_cars(self):
        cur = self.conn.cursor()

        rows = cur.execute("SELECT * FROM masini")

        row_list = list(rows)

        for i in row_list:
            print(
                f"Id_masina: {i[0]} --- Marca: {i[1]} --- Model: {i[2]} --- Numar inmatriculare {i[6]}")
        self.conn.commit()

# Select all customers saved into 'clienti' table and print only indexe 0,1,2
    def read_client(self):
        cur = self.conn.cursor()

        rows = cur.execute("SELECT * FROM clienti")

        row_list = list(rows)

        for i in row_list:
            print(
                f"Id_client: {i[0]} --- Nume: {i[1]} --- Prenume: {i[2]}")
        self.conn.commit()

# Select all reservations saved into 'rezervare' table and prints only indexe 0,1,2,3,4
    def read_reservations(self):
        cur = self.conn.cursor()
        rows = cur.execute("SELECT * FROM rezervare")
        row_list = list(rows)
        for i in row_list:
            print(
                f"id_rezervare: {i[0]} --- data_start: {i[1]} --- data_end: {i[2]} --- client_id: {i[3]} --- masina_id: {i[4]}")
        self.conn.commit()

# Delete reservations chosed by user
    def delete_reservation(self, reservation_id):
        db = 'DELETE FROM rezervare WHERE id=?'
        cur = self.conn.cursor()
        cur.execute(db, (reservation_id,))
        self.conn.commit()

# User can search if the car is booked by car number plate
    def show_car_number_plate(self, numar_inmatriculare):
        cur = self.conn.cursor()
        rows = cur.execute('SELECT rezervare.id, rezervare.data_start, rezervare.data_end, rezervare.client_id, rezervare.masina_id, masini.numar_inmatriculare from rezervare INNER JOIN masini ON rezervare.masina_id = masini.id WHERE masini.numar_inmatriculare=?', (numar_inmatriculare,))
        row_list = list(rows)
        self.conn.commit()
        for i in row_list:
            print(
                f"id_rezervare: {i[0]} --- data_start: {i[1]} --- data_end: {i[2]} --- client_id: {i[3]} --- masina_id: {i[4]} --- numar inmatriculare:{i[5]}")

    def validate_reservation_db(self):
        cur = self.conn.cursor()
        rows = cur.execute("SELECT * FROM rezervare")
        self.conn.commit()
        row_list = list(rows)
        return row_list

    def wrong_reservation(self, wrong_id):
        cur = self.conn.cursor()
        rows = cur.execute("SELECT * FROM rezervare WHERE id=?", (wrong_id, ))
        self.conn.commit()
        row_list = list(rows)
        return row_list

    def wrong_car_number_plate(self, wrong_plate):
        cur = self.conn.cursor()
        rows = cur.execute('SELECT rezervare.id, rezervare.data_start, rezervare.data_end, rezervare.client_id, rezervare.masina_id, masini.numar_inmatriculare from rezervare INNER JOIN masini WHERE masini.numar_inmatriculare=?', (wrong_plate,))
        self.conn.commit()
        row_list = list(rows)
        return row_list
