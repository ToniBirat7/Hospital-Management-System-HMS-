from Admin import Admin
from Doctor import Doctor
from Patient import Patient
from read_file import load_patient, rewrite

print("Main Has Started")

# Initializing the actors

admin = Admin('admin','123','B1 1AB') # username is 'admin', password is '123'
doctors = [Doctor('John','Smith','Internal Med.'), Doctor('Harry','Maguire','Pediatrics'), Doctor('Harry','Kane','Cardiology')]    
patients = [Patient('Sara','Smith', 20, '07012345678','B1 234',['Fever','Headache']), Patient('Mike','Jones', 37,'07555551234','L2 2AB',['Fever','Nausea']), Patient('Daivd','Smith', 15, '07123456789','C1 ABC',['Fever','Dizziness'])]
discharged_patients = []

# Load from file or create new file
load_patient(patients)

def main():
    """
    the main function to be ran when the program runs
    """

    # keep trying to login tell the login details are correct
    while True:
        # username = input('Enter the username: ').strip()
        # password = input('Enter the password: ').strip()
        if admin.login("admin","123"):
            running = True # allow the program to run
            break
        else:
            print('Incorrect username or password.')
    while True:
        # print the menu
        print('Choose the operation:')
        print(' 1- Register/view/update/delete doctor')
        print(' 2- Discharge patients')
        print(' 3- View discharged patient')
        print(' 4- Assign doctor to a patient')
        print(' 5- Update admin details')
        print(' 6- Add Patient')
        print(' 7- View Patient')
        print(' 8- View Doctor Appointment')
        print(' 9- View Patient of Same Family')
        print(' 10- Relocate Patient')
        print(' 11- Display Report')
        print(' 12- Assign Illness')
        print(' 13- Quit')

        # get the option
        op = input('Enter Option: ')

        if op == '1':
            # 1- Register/view/update/delete doctor
         #ToDo1
          admin.doctor_management(doctors)  

        elif op == '2':
            # 2- View or discharge patients
            #ToDo2
            if patients:
                patient_index = admin.discharge(patients,discharged_patients)

                if admin.find_index(patient_index,patients):
                 
                 while True:
                    op = input('Do you want to discharge the patient(Y/N):').lower()

                    if op == 'yes' or op == 'y':
                        #ToDo3
                        discharged_patients.append(patients[patient_index])

                        print(f"\n!!! Good News! Patient {patients[patient_index].full_name()} has been discharged !!!\n")

                        patients.pop(patient_index)

                        rewrite(patients)

                        if patients:
                            print("Updated Patient List\n")
                            admin.view_patient(patients)

                        break

                    elif op == 'no' or op == 'n':
                        break

                    # unexpected entry
                    else:
                        print('Please answer by yes or no.')
                else:
                    print(f"!!! Patient with ID {patient_index + 1} does not exists !!!")
            else: 
                print("\nThere Are No Any Patients In The Hospital\n")

        elif op == '3':
            # 3 - view discharged patients
            #ToDo4
            admin.view_discharge(discharged_patients)

        elif op == '4':
            # 4- Assign doctor to a patient
            admin.assign_doctor_to_patient(patients, doctors)

        elif op == '5':
            # 5- Update admin detais
            admin.update_details()

        elif op == '6':
            first_name,surname,age,mobile,postcode,symptoms = admin.add_patients()
            print(symptoms)

            patients.append(Patient(first_name.strip(),surname.strip(),age,mobile.strip(),postcode.strip(),symptoms))
            print(patients[-1].string_symptoms())

            rewrite(patients)

        elif op == '7':
            print("\n--------Patient List--------\n")
            print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode |      Symptoms      ')
            admin.view(patients)

        elif op == '8':
            admin.view_appointment(doctors)

        elif op == '9':
            surnames = set([patient.get_surname() for patient in patients])
            family = {surname: list(filter(lambda x: (x.get_surname() == surname), patients)) for surname in surnames}

            print("------Patient of Same Family------")
            for i,j in family.items():
                print(f"\n{i} Family:")
                print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode |      Symptoms      ')
                for index, item in enumerate(j):
                    print(f'{index+1:3}|{item}')

        elif op == '10':
            admin.relocate(patients,doctors)
        
        elif op == "11":
            admin.report(patients,doctors)

        elif op == "12":
            admin.assign_illness(patients)

        elif op == '13':
            #ToDo5
            break

        else:
            # the user did not enter an option that exists in the menu
            print('Invalid option. Try again')

