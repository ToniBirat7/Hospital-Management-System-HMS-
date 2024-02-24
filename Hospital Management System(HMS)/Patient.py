from Person import Person

class Patient(Person):
    """Patient class"""

    def __init__(self, first_name, surname, age, mobile, postcode, symptoms = []):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            age (int): Age
            mobile (string): the mobile number
            address (string): address
        """

        #ToDo1
        super().__init__(first_name,surname)
        self.__age = age
        self.__mobile = mobile
        self.__postcode = postcode
        self.__doctor = 'None'
        self.__symptoms = symptoms
        self.__illness = 'None'
    
    def get_age(self):
        return self.__age
    
    def get_postcode(self):
        return self.__postcode
    
    def get_mobile(self):
        return self.__mobile

    def get_doctor(self) :
        #ToDo3
        return self.__doctor
    
    def set_doctor(self,doctor):
        self.__doctor = doctor

    def link(self, doctor):
        """Args: doctor(string): the doctor full name"""
        self.__doctor = doctor

    def print_symptoms(self):
        """prints all the symptoms"""
        #ToDo4
        return self.__symptoms
    
    def get_illness(self):
        return self.__illness
    
    def set_illness(self,illness):
        self.__illness = illness
    
    def string_symptoms(self):
        symptoms = ''
        for item in self.__symptoms:
            symptoms = symptoms + item + " "
        return symptoms.strip()

    def __str__(self):
        return f'{self.full_name():^30}|{self.__doctor:^40}|{self.__age:^5}|{self.__mobile:^15}|{self.__postcode:^10}|{self.string_symptoms():^25}'
        # {"ID":^3}|{"Full Name":^30}|{"Doctor's Full Name":^40}|{"Age":^5}|{"Mobile":^15}|{"Postcode":^10}|{"Symptoms":^25}|"
