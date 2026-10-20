from Database import Database

class Person():
    def __init__(self, name, year, gender, namecount, total):
        self.__name = name
        self.__year = year
        self.__gender = gender
        self.__namecount = namecount
        self.__total = total

    @staticmethod
    def fetch_person(name, gender):
        return Database.fetch_person(name, gender)

    def get_name(self):
        return self.__name

    def get_year(self):
        return self.__year

    def get_gender(self):
        return self.__gender

    def get_namecount(self):
        return self.__namecount

    def get_total(self):
        return self.__total

