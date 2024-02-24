from Patient import Patient

# Create patient objects after reading

def create_patient_object(file,patients):
    patients.clear()
    data = file.readlines()
    print(data)

    for item in data:
        if (item == 'Patient Details\n') or ('*' in item):
            continue
        first_name, surname, age, mobile, postcode, symptoms = item.split(',')
        symptoms = [x.replace("\n",'') for x in symptoms.split(' ')]
        patients.append(Patient(first_name.strip().capitalize(), surname.strip().capitalize(), int(age), mobile.strip(), postcode.strip(), symptoms))

def load_patient(patients):
    file = None
    try:
        file = open("patient.txt","r")
    except FileNotFoundError:
        print("The File is Not Found! Creating New File for Patients")

    if file: # If existing file 
        create_patient_object(file,patients)
    
    else:
        # Format the patient object into file writeable
        formatted_patients = []

        for patient in patients:
            symptoms_str = patient.string_symptoms()
            formatted_patient = f"{patient.get_first_name()},{patient.get_surname()},{patient.get_age()},{patient.get_mobile()},{patient.get_postcode()},{symptoms_str}"
            formatted_patients.append(formatted_patient)
        
        with open("patient.txt",'w') as file:
            file.write("Patient Details\n")
            file.write("***************\n")

            for item in formatted_patients:
                file.writelines(item)
                file.write("\n")

        file = open("patient.txt",'r')
        create_patient_object(file,patients)
            
    file.close()

# Rewrite file if there's change in the patient data
def rewrite(patients):
    with open("patient.txt",'w') as file:
        file.write("Patient Details\n")
        file.write("***************\n")

        for item in patients:
            file.writelines(f'{item.get_first_name()},{item.get_surname()},{item.get_age()},{item.get_mobile()},{item.get_postcode()},{item.string_symptoms()}')
            file.write("\n")
