from Doctor import Doctor
import datetime

class Admin:
    """A class that deals with the Admin operations"""
    def __init__(self, username, password, address = ''):
        """
        Args:
            username (string): Username
            password (string): Password
            address (string, optional): Address Defaults to ''
        """
        self.__username = username
        self.__password = password
        self.__address =  address

    def set_username(self,uname):
        self.__username = uname
    
    def set_password(self,password):
        self.__password = password

    def set_address(self,address):
        self.__address = address

    def view(self,a_list):
        """
        print a list
        Args:
            a_list (list): a list of printables
        """
        for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}')

    def login(self,username="admin",password="123") :
        """
        A method that deals with the login
        Raises:
            Exception: returned when the username and the password ...
                    ... don`t match the data registered
        Returns:
            string: the username
        """
    
        # print("-----Login-----")
        #Get the details of the admin

        # username = input('Enter the username: ').strip()
        # password = input('Enter the password: ').strip()

        # check if the username and password match the registered ones
        #ToDo1
        if username == "admin" and password == "123":
            return self.__username

    def find_index(self,index,doctors):
        
            # check that the doctor id exists          
        if index in range(0,len(doctors)):
            
            return True
        
        # if the id is not in the list of doctors
        else:
            return False
    
    def enter_number(self):
        print("\n!!! Please Enter a Number")

    def loop_report_data(self,a_dict):
        for i,j in a_dict.items():
            print(f"Dr.{i} : {j}")

    def take_id(self,actor):
        value = True
        while value:
            try:
                index = int(input(f"\nEnter the ID of {actor}:"))
                value = False
                return index - 1
            except ValueError:
                self.enter_number()
       
    def get_doctor_details(self) :
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname and ...
                            ... the speciality of the doctor in that order.
        """
        #ToDo2
        first_name = input("Enter First Name of Doctor: ").capitalize().strip()
        surname = input("Enter Surname of Doctor: ").capitalize().strip()
        speciality = input("Enter Speciality of Doctor: ").capitalize().strip()

        return first_name, surname, speciality

    def doctor_management(self, doctors):
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """

        print("-----Doctor Management-----")

        # menu
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')

        #ToDo3
        op = input("Choose Option: ")

        # register
        if op == '1':
            print("-----Register-----")

            # get the doctor details
            print('Enter the doctor\'s details:')
            #ToDo4
            first_name, surname, speciality = self.get_doctor_details()

            # check if the name is already registered
            name_exists = False
            for doctor in doctors:
                if first_name == doctor.get_first_name() and surname == doctor.get_surname():
                    print('Name already exists.')
                    #ToDo5
                    return name_exists 

            #ToDo6
            doctors.append(Doctor(first_name,surname,speciality))
                                                         
            print(f'\nDoctor {first_name} {surname}, {speciality} Registered!\n') 

        # View
        elif op == '2':
            print("-----List of Doctors-----")
            #ToDo7
            for doctor in doctors:
                 print(doctor)

        # Update
        elif op == '3':
            while True:
                print("-----Update Doctor`s Details-----")
                print('ID |          Full name           |  Speciality')
                self.view(doctors)
                try:
                    index = int(input('Enter the ID of the doctor: ')) - 1
                    doctor_index=self.find_index(index,doctors)
                    if doctor_index!=False:
                        break
                    else:
                        print("Doctor not found")

                    
                        # doctor_index is the ID mines one (-1)
                        

                except ValueError: # the entered id could not be changed into an int
                    print('The ID entered is incorrect')

            # menu
            print('Choose the field to be updated:')
            print(' 1 First name')
            print(' 2 Surname')
            print(' 3 Speciality')

            op = input('Choose Option :  ')
            
            #ToDo8
            if op == '1':
                first_name = input("Enter New First Name: ")
                doctors[index].set_first_name(first_name)

            elif op == '2':
                surname = input("Enter Updated Surname: ")
                doctors[index].set_surname(surname)

            elif op == '3':
                speciality = input("Enter Updated Speciality: ")
                doctors[index].set_speciality(speciality)

            else:
                print("Please Enter Valid Option")

        # Delete
        elif op == '4':
            print("-----Delete Doctor-----")
            print('ID |          Full Name           |  Speciality')
            self.view(doctors)

            doctor_index = self.take_id("Doctor")
            #ToDo9
            if self.find_index(doctor_index,doctors):
                print(f"{doctors[doctor_index].full_name()} is successfully removed.")
                doctors.pop(doctor_index)
            else:
                print('The id entered is incorrect')

        # if the id is not in the list of patients
        else:
            print('Invalid operation choosen. Check your spelling!')

        return True

    def view_patient(self, patients):
        """
        print a list of patients
        Args:
            patients (list<Patients>): list of all the active patients
        """
        print("-----View Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode |       Symptoms          |')
        #ToDo10
        self.view(patients)

    def assign_doctor_to_patient(self, patients, doctors):
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        print("-----Assign-----")

        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode |      Symptoms      ')
        self.view(patients)

        patient_index = input('Please enter the patient ID: ')

        try:
            # patient_index is the patient ID mines one (-1)
            patient_index = int(patient_index) -1

            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return # stop the procedures

        except ValueError: # the entered id could not be changed into an int
            print('The id entered is incorrect')
            return # stop the procedures

        print("-----Doctors Select-----")
        print('Select the doctor that fits these symptoms:')

        self.view(patients[patient_index].print_symptoms()) # print the patient symptoms

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        doctor_index = input('Please enter the doctor ID: ')

        try:
            # doctor_index is the patient ID mines one (-1)
            doctor_index = int(doctor_index) -1

            # check if the id is in the list of doctors
            if self.find_index(doctor_index,doctors)!=False:
                    
                # link the patients to the doctor and vice versa
                #ToDo11
                doctor_to_assign = doctors[doctor_index]
                patient_to_assign = patients[patient_index]

                patients[patient_index].set_doctor(doctor_to_assign.full_name())
                doctors[doctor_index].add_patient(patient_to_assign.full_name())

                doctors[doctor_index].add_appointment(patient_to_assign.full_name())
                # print(patients[patient_index].get_doctor())

                print(f'\nThe patient {patient_to_assign.full_name()} is now assign to the Dr. {doctor_to_assign.full_name()}, {doctor_to_assign.get_speciality()}\n')

            # if the id is not in the list of doctors
            else:
                print('The id entered was not found.')

        except ValueError: # the entered id could not be changed into an in
            print('The id entered is incorrect')


    def discharge(self, patients, discharged_patients):
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patients>): the list of all the active patients
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        
        print("-----Discharge Patient-----")

        #ToDo12
        self.view_patient(patients)
        value = True
        while True:
            try:
                patient_index = int(input('\nPlease enter the patient ID: ')) - 1
                value = False
                return patient_index 
            except ValueError:
                print("\n!!! Please Enter Number")

    def view_discharge(self, discharged_patients):
        """
        Prints the list of all discharged patients
        Args:
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        #ToDo13
        if discharged_patients:
            print("-----Discharged Patients-----")
            self.view_patient(discharged_patients)
        else:
            print("\nNone of the patients is discharged\n")

    def add_patients(self):

        first_name = input("Enter patient first name : ")
        surname = input("Enter patient surname : ")
        while True:
            try:
                age = int(input("Enter patient age : "))
                break
            except:
                print("Please Enter Number")

        mobile = input("Enter patient mobile : ")
        postcode = input("Enter patient postcode : ")
        symptoms = input("Enter symptoms(Separated by a space) : ").split(" ")
        print(symptoms)

        return first_name,surname,age,mobile,postcode,symptoms

    def update_details(self):
        """
        Allows the user to update and change username, password and address
        """

        print('Choose the field to be updated:')
        print(' 1 Username')
        print(' 2 Password')
        print(' 3 Address')

        try:
            op = int(input('Input: '))
        except ValueError:
            print("Please Enter Valid Operator")
            return None

        if op == 1:
            new_username = input("Enter New Username: ")
            self.__username = new_username
            print(f"New admin username is {new_username}")

        elif op == 2:
            password = input('Enter the new password: ')
            # validate the password
            if password == input('Enter the new password again: '):
                self.__password = password
                print(f"New admin password is {password}")

        elif op == 3:
            #ToDo15
            new_address = input("Enter Address: ")
            self.__address = new_address
            print(f"New admin address is {new_address}")

        else:
            #ToDo16
            print("Enter Valid Operator")

    def view_appointment(self,doctors):
        print('-------Doctor List-------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)

        # Check ID
        doctor_index = self.take_id("Doctor")

        if self.find_index(doctor_index,doctors):
            doctor = doctors[doctor_index]
            appointment_list = doctors[doctor_index].get_appointment()
            if appointment_list:
                print(f"\nAppointments of {doctor.full_name()} are:\n")
                self.view(appointment_list)
                print("\n")
            else:
                print(f"\nThere is no any appointment for Dr. {doctor.full_name()}\n")
        else:
            print(f"\nThe Doctor with ID {doctor_index + 1} does not exist.\n")
    
    def relocate(self,patients,doctors):
        print("\n--------Patient List--------\n")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode |      Symptoms      ')
        self.view(patients)

        print("-----Doctor List-----")
        print('ID |          Full name           |  Speciality')
        self.view(doctors)

        patient_index = self.take_id("Patient")
        doctor_index = self.take_id("Doctor to Assign")
        previous_doctor = self.take_id("Previous Doctor")

        if self.find_index(patient_index,patients) and self.find_index(doctor_index,doctors) and self.find_index(previous_doctor,doctors):
            patient_to_assign = patients[patient_index]
            doctor_to_assign = doctors[doctor_index]
            patient_to_remove = doctors[previous_doctor]

            patients[patient_index].set_doctor(doctor_to_assign.full_name())

            doctors[doctor_index].add_patient(patient_to_assign.full_name())
            doctor_to_assign.add_appointment(patient_to_assign.full_name())

            patient_to_remove.get_appointment().remove(patient_to_assign.full_name())
            patient_to_remove.get_patient_list().remove(patient_to_assign.full_name())

        else:
            print("!!! ID Does Not Exist")

    def report(self,patients,doctors):
        print("----Management Report----")

        # Total number of doctors in the system
        print(f'There are {len(doctors)} Doctors in Total\n')
        print(f'There are {len(patients)} Patients in Total\n')

        # Total number of patients per doctor
        patients_per_doctor = {doctor.full_name(): len(doctor.get_patient_list()) for doctor in doctors}
        print("Patients per Doctor\n")
        self.loop_report_data(patients_per_doctor)

        # Total number of appointments per month per doctor
        appointments_per_doctor = {doctor.full_name(): len(doctor.get_appointment()) for doctor in doctors}
        current_month = datetime.datetime.now().strftime("%B")
        print(f"\nAppointments Per Month Per Doctor For {current_month}\n")
        self.loop_report_data(appointments_per_doctor)
    
        # Total number of patients based on the illness type
        illness_type = set([patient.get_illness() for patient in patients])
        number_of_patient_illness = {illness: list(filter(lambda x: (x.get_illness() == illness), patients)) for illness in illness_type}
        
        print("\nNumber of Patients Based on the Illness Type\n")
        for i,j in number_of_patient_illness.items():
            print(f"{i}: {len(j)}")

        # print('***************')
        # print(number_of_patient_illness)
        # print('***************')
        
        return patients_per_doctor,appointments_per_doctor,number_of_patient_illness

    def assign_illness(self,patients):
        print("Assign Illness Based On Symptoms")
        print("\n--------Patient List--------\n")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode |      Symptoms      ')
        self.view(patients)
        patient_index = self.take_id("Patient")
        if self.find_index(patient_index,patients):
            illness = input("\nEnter Illness: ").capitalize().strip()
            patients[patient_index].set_illness(illness)
            print(f"\nPatient {patients[patient_index].full_name()} has {illness}")
        else:
            print(f"\nThe Patient with ID {patient_index + 1} does not exist.")
            



        
        
        
        
        









        


