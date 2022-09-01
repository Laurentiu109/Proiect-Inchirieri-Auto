from datetime import datetime


class Rezervari:

    def __init__(self, reservation_db):
        self.__data_start = reservation_db["data_start"]
        self.__data_end = reservation_db["data_end"]
        self.__client_id = reservation_db["client_id"]
        self.__masina_id = reservation_db["masina_id"]

    def get_data_start(self):
        return self.__data_start

    def get_data_end(self):
        return self.__data_end

    def get_client_id(self):
        return self.__client_id

    def get_masina_id(self):
        return self.__masina_id

    # def __str__(self) -> str:
    #     pass
