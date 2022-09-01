class Car:

    def __init__(self, car_db):
        self.__marca = car_db["marca"]
        self.__model = car_db["model"]
        self.__an_fabricatie = car_db["an_fabricatie"]
        self.__tip_caroserie = car_db["tip_caroserie"]
        self.__serie_sasiu = car_db["serie_sasiu"]
        self.__numar_inmatriculare = car_db["numar_inmatriculare"]

    # def __init__(self, car_data: list):
    #     self.__id = car_data[0]
    #     self.__marca = car_data[1]
    #     self.__model = car_data[2]
    #     self.__an_fabricatie = car_data[3]
    #     self.__tip_caroserie = car_data[4]
    #     self.__serie_sasiu = car_data[5]
    #     self.__numar_inmatriculare = car_data[6]
