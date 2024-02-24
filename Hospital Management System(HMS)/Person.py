class Person:
    def __init__(self,first_name, surname):
        self.__first_name = first_name
        self.__surname = surname

    def full_name(self) :
        return f"{self.__first_name} {self.__surname}"

    def get_first_name(self) :
        return f"{self.__first_name}"

    def set_first_name(self, new_first_name):
        self.__first_name = new_first_name

    def get_surname(self) :
        return f"{self.__surname}"

    def set_surname(self, new_surname):
        self.__surname = new_surname