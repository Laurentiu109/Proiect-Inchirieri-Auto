from datetime import datetime
from car import Car
from client import Client
from database import DataBase
from menu import Menu
from rezervari import Rezervari
import pathlib
import sqlite3
import sys

ROOT = pathlib.Path(__file__).parent
DB_FILE = ROOT.joinpath("inchirieri.db")


repo = DataBase(DB_FILE)

repo.client_table_db()
repo.car_table_db()
repo.reservations_table_db()


def enter():
    input("Apasa ENTER pentru a reveni la meniul principal!")


"""Check if the car is booked in the same period of time by 2 different customers"""


def validate_reservation(reservation):
    for r in repo.validate_reservation_db():
        if datetime.strptime(r[1], '%Y-%m-%d').date() <= reservation.get_data_end() and \
            datetime.strptime(r[2], '%Y-%m-%d').date() >= reservation.get_data_start() and \
                r[4] == int(reservation.get_masina_id()):
            return False
    return True


while True:
    Menu.menu()
    option = Menu.read_option()
    match option:
        case '0': sys.exit()
        case '1':
            car_input = Menu.add_car_menu()
            car1 = Car(car_input)
            repo.add_car_db(car_input)
            print("Masina a fost adaugata cu succes.\n")
            repo.read_cars()
            enter()
        case '2':
            user_input = Menu.add_client_menu()
            user1 = Client(user_input)
            repo.add_client_db(user_input)
            print("Clientul a fost adaugat cu succes.\n")
            repo.read_client()
            enter()
        case '3':
            try:
                rezervare_input = Menu.add_rezervari_menu()
                rezervare = Rezervari(rezervare_input)
                if (validate_reservation(rezervare)):
                    repo.add_reservation_db(rezervare_input)
                    repo.read_reservations()
                else:
                    print("Masina este deja rezervata")
            except sqlite3.IntegrityError as err:
                print('Eroare in db!')
            finally:
                enter()
        case '4':
            n = int(input(
                "1.Vezi toate rezervarile\n2.Vezi rezervarile dupa numarul de inmatriculare\nAlege optiunea:"))
            if n == 1:
                repo.read_reservations()
            elif n == 2:
                number_plate = input("Numar de inmatriculare: ")
                if (repo.wrong_car_number_plate(number_plate)):
                    repo.show_car_number_plate(number_plate)
                else:
                    print("Numarul de inmatriculare nu exista in lista de rezervari!")
            else:
                print("Optiune inexistenta!")
            enter()
        case '5':
            reservation_id = input(
                "Id-ul rezervarii pe care vrei sa o anulezi: ")
            if (repo.wrong_reservation(reservation_id)):
                repo.delete_reservation(reservation_id)
                print("Rezervarea a fost anulata!!\n")
            else:
                print("ID-ul introdus nu exista in lista de rezervari!")
            enter()
        case _:

            print("Optiune inexistenta!")
