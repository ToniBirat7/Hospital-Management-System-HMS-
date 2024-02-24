from Person import Person
class Doctor(Person):
    """A class that deals with the Doctor operations"""

    def __init__(self, first_name, surname, speciality):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            speciality (string): Doctor`s speciality
        """
        super().__init__(first_name,surname)
        # self.__first_name = first_name
        # self.__surname = surname
        self.__speciality = speciality
        self.__patients = []
        self.__appointments = []

    def get_speciality(self) :
        #ToDo6
        return f"{self.__speciality:^30}"

    def set_speciality(self, new_speciality):
        #ToDo7
        self.__speciality = new_speciality

    def add_patient(self, patient):
        self.__patients.append(patient)
    
    def get_patient_list(self):
        return self.__patients
    
    def add_appointment(self,patient):
        self.__appointments.append(patient)

    def get_appointment(self):
        return self.__appointments

    def __str__(self) :
        return f'{self.full_name():^30}|'
        # return f'{self.full_name():^30}|{self.__speciality:^15}'

