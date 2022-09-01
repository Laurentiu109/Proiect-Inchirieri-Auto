class Client:

    def __init__(self, client_db):
        self.__nume = client_db["nume"]
        self.__prenume = client_db["prenume"]
        self.__cnp = client_db["cnp"]
        self.__adresa = client_db["adresa"]
        self.__telefon = client_db["telefon"]
        self.__email = client_db["email"]
