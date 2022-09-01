from datetime import datetime
import pathlib
import sqlite3
import os
import sys


class Menu:

    @staticmethod
    def menu():
        print(
            """
                BINE AI VENIT ! 

            1. Adauga masina
            2. Adauga client
            3. Adauga rezervare
            4. Vezi rezervari
            5. Anuleaza rezervare
            0. Iesire program
        """)

    def read_option():
        return input("Selecteaza optiunea:")

    @staticmethod
    def add_car_menu():
        return {
            "marca": input("Introduceti marca:"),
            "model": input("Introduceti model:"),
            "an_fabricatie": input("Introduceti an fabricatie:"),
            "tip_caroserie": input("Introduceti tipul caroseriei:"),
            "serie_sasiu": input("Introduceti serie sasiu:"),
            "numar_inmatriculare": input("Introduceti numarul de inmatriculare:")
        }

    @staticmethod
    def add_client_menu():
        return {
            "nume": input("Introduceti numele de familie:"),
            "prenume": input("Introduceti prenume:"),
            "cnp": input("Introduceti cnp:"),
            "adresa": input("Introduceti adresa:"),
            "telefon": input("Introduceti numar de telefon:"),
            "email": input("Introduceti email:")
        }

    @staticmethod
    def add_rezervari_menu():
        return {
            "data_start": datetime.strptime(input("Introduceti data start dorita:"), '%Y-%m-%d').date(),
            "data_end": datetime.strptime(input("Introduceti data end dorita:"), '%Y-%m-%d').date(),
            "client_id": input("Introduceti id-ul unui client:"),
            "masina_id": input("Introduceti id-ul unei masini:")
        }
