from Doctor import Doctor
from read_file import rewrite

import tkinter as tk
from tkinter import Frame, Canvas, Scrollbar, Label

def register(btn_value,app,tk,doctors):
    # Implement the register function
    print(btn_value)

    def register_doctor(tk):
        print("Register")
        fname = first_name.get().strip().capitalize()
        lname = surename.get().strip().capitalize()
        spc = speciality.get().strip().capitalize()
        if fname and lname and spc:
            option_frame.destroy()
            print(fname, lname, spc)

            a = False

            for doctor in doctors:
                if fname == doctor.get_first_name() and lname == doctor.get_surname():
                    a = True
                    break
                    
            if a:
                print('Name already exists.')
                error_text = tk.Label(app, text="Doctor Already Exists", font=("Arial", 24, "roman"), fg="black")
                error_text.place(relx=0.5, rely=0.93, anchor=tk.CENTER)
                app.after(2000, error_text.destroy)
            else:
                doctors.append(Doctor(fname, lname, spc))
                success = tk.Label(app, text=f"Dr. {fname} {lname}, {spc} Registered Successfully!", font=("Arial", 24, "roman"), fg="black")
                success.place(relx=0.55, rely=0.5, anchor=tk.CENTER)
                app.after(2100, success.destroy)
                print(doctors)
                        
        else:
            print("Can't Be Empty")
            error_text = tk.Label(app, text="Fields Can't Be Empty", font=("Arial", 24, "roman"), fg="black")
            error_text.place(relx=0.75, rely=0.93, anchor=tk.CENTER)
            app.after(2000, error_text.destroy)

    def update_doctor(index,doctor):

        def update_doctor_info():
            print("Update Clicked")
            fname = first_name_entry.get().strip().capitalize()
            lname = surname_entry.get().strip().capitalize()
            spc = speciality_entry.get().strip().capitalize()
            if fname and lname and spc:
                print(original_spc,original_fname)
                update_frame.destroy()
                doctor.set_first_name(fname)
                doctor.set_surname(lname)
                doctor.set_speciality(spc)
                success_label = tk.Label(app, text=f"Dr. {doctor.get_first_name()} {doctor.get_surname()}, {doctor.get_speciality().strip()} Updated Successfully!", font=("Arial", 24, "roman"), fg="black")
                success_label.place(relx=0.5, rely=0.65, anchor=tk.CENTER)
                app.after(2100, success_label.destroy)
            else:
                error_label = tk.Label(update_frame, text="Fields Can't Be Empty", font=("Arial", 24, "roman"), fg="black", bg="#E6CECE")
                error_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
                app.after(2000, error_label.destroy)

        option_frame.destroy()

        print(index,doctor.full_name())

        update_frame = tk.Frame(app, bg="#E6CECE", borderwidth=2, relief=tk.SOLID, width=300, height=300)
        update_frame.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

        choose_text = tk.Label(update_frame, text="Enter Doctor Details", font=("Arial", 24, "roman"), fg="black", bg="#E6CECE")
        choose_text.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        original_fname = tk.StringVar(value=doctor.get_first_name())
        original_lname = tk.StringVar(value=doctor.get_surname())
        original_spc = tk.StringVar(value=doctor.get_speciality().strip())

        first_name_label = tk.Label(update_frame, text="First Name:", font=("Arial", 18, "bold"), fg="black", bg="#E6CECE")
        first_name_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        first_name_entry = tk.Entry(update_frame, width=30, font=("Arial", 18))
        first_name_entry.insert(0, original_fname.get())
        first_name_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        surname_label = tk.Label(update_frame, text="Surname:", font=("Arial", 18, "bold"), fg="black", bg="#E6CECE")
        surname_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        surname_entry = tk.Entry(update_frame, width=30, font=("Arial", 18))
        surname_entry.insert(0, original_lname.get())
        surname_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        speciality_label = tk.Label(update_frame, text="Speciality:", font=("Arial", 18, "bold"), fg="black", bg="#E6CECE")
        speciality_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")
        speciality_entry = tk.Entry(update_frame, width=30, font=("Arial", 18))
        speciality_entry.insert(0, original_spc.get())
        speciality_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        update_button = tk.Button(update_frame, text="Update", font=("Arial", 20, "bold"), fg="white", bg="#4158D0", width=15, height=1, command=update_doctor_info)
        update_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def delete_doctor(index,doctor):
        option_frame.destroy()
        success = tk.Label(app, text=f"Dr. {doctor.full_name()} has been removed",font=("Aerial", 24,"roman"),fg="black")
        success.place(relx=0.5, rely=0.55, anchor=tk.CENTER)
        app.after(2100, success.destroy)
        doctors.pop(index)
        print("Doctor Deleted")

    if btn_value == 1:
    
        option_frame = tk.Frame(app, bg="#E6CECE", bd=2, width=500, height=500)
        option_frame.place(relx=0.4, rely=0.7, anchor=tk.CENTER)

        choose_text = tk.Label(option_frame, text="Enter Doctor Details", font=("Arial", 24, "roman"), fg="black")
        choose_text.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        
        first_name_label = tk.Label(option_frame, text="Firstname:", fg="black", bg="#E6CECE", font=("Arial", 14))
        first_name_label.grid(row=1, column=0, padx=10, pady=(0, 0), sticky="e")

        surename_label = tk.Label(option_frame, text="Surename:", fg="black", bg="#E6CECE", font=("Arial", 14))
        surename_label.grid(row=2, column=0, padx=10, pady=(0, 0), sticky="e")

        speciality_label = tk.Label(option_frame, text="Speciality:", fg="black", bg="#E6CECE", font=("Arial", 14))
        speciality_label.grid(row=3, column=0, padx=10, pady=(0, 0), sticky="e")

        first_name = tk.Entry(option_frame, width=20,font=("Arial", 14))
        surename = tk.Entry(option_frame, width=20,font=("Arial", 14))
        speciality = tk.Entry(option_frame, width=20,font=("Arial", 14))


        first_name.grid(row=1, column=1, padx=10, pady=(20, 5))
        surename.grid(row=2, column=1, padx=10, pady=(10, 20))
        speciality.grid(row=3, column=1, padx=10, pady=(10, 20))

        add = tk.Button(option_frame, text="Register", fg="white", bg="#4158D0", font=("Arial", 20), width=15, height=1, command= lambda : register_doctor(tk))
        add.grid(row=4, columnspan=2, padx=10, pady=10)
    
    if btn_value == 2:
        print("View")

        if doctors:

            option_frame = tk.Frame(app, bg="#E6CECE", width=400, height=200)
            option_frame.place(relx=0.5, rely=0.69, anchor=tk.CENTER)

            choose_text = tk.Label(option_frame, text="List of Doctors", font=("Arial", 24, "bold"), bg="#E6CECE", fg="black")
            choose_text.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

            doctor_info_spec = tk.Label(option_frame, text="Full name", font=("Arial", 24, "bold"), bg="#E6CECE", fg="black")
            doctor_info_spec.grid(row=1, column=0, padx=10, pady=10)

            doctor_info = tk.Label(option_frame, text="Speciality", font=("Arial", 24, "bold"), bg="#E6CECE", fg="black")
            doctor_info.grid(row=1, column=1, padx=10, pady=10)

            # Scrollable Frame
            canvas = Canvas(option_frame, bg="#E6CECE", width=700, height=120, highlightthickness=0)
            canvas.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

            scrollbar = Scrollbar(option_frame, orient="vertical", command=canvas.yview)
            scrollbar.grid(row=2, column=2, sticky="ns")

            inner_frame = Frame(canvas, bg="#E6CECE")
            inner_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

            canvas.create_window((0, 0), window=inner_frame, anchor="nw")

            for i, doctor in enumerate(doctors, start=1):
                register_name = tk.Label(inner_frame, text=doctor, font=("Arial", 24, "roman"), bg="#E6CECE", fg="black")
                register_name.grid(row=i+1, column=0, padx=0, pady=10)

                register_speciality = tk.Label(inner_frame, text=doctor.get_speciality(), font=("Arial", 24, "roman"), bg="#E6CECE", fg="black")
                register_speciality.grid(row=i+1, column=1, padx=10, pady=10)
            
            def resize(event):
                canvas.itemconfig(inner_frame, width=event.width)

            canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

            canvas.configure(yscrollcommand=scrollbar.set)

            app.after(6000, option_frame.destroy)

        else:
            print("No Doctors")
            error_text = tk.Label(app, text="There are No any Doctors In The System", font=("Arial", 24, "roman"), fg="black")
            error_text.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
            app.after(2000, error_text.destroy)

    if btn_value == 3:

        if doctors:

            option_frame = tk.Frame(app, bg="#E6CECE", bd=2, width=500, height=500)
            option_frame.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

            choose_text = tk.Label(option_frame, text="Choose Doctor To Update", font=("Arial", 24, "bold"), bg="#E6CECE", fg="black")
            choose_text.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

            font_style = ("Arial", 16, "bold")
            
            for index, doctor_name in enumerate(doctors, start=0):
                register = tk.Button(option_frame, text=doctor_name.full_name(), command=lambda index=index, doctor_name=doctor_name: update_doctor(index, doctor_name), width=30, height=2, font=font_style)
                register.grid(row=index+1, column=0, columnspan=2, padx=10, pady=10)

        else:
            print("No Doctors")
            error_text = tk.Label(app, text="There are No any Doctors In The System", font=("Arial", 24, "roman"), fg="black")
            error_text.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
            app.after(2000, error_text.destroy)
    
    if btn_value == 4:

        if doctors:
        
            option_frame = tk.Frame(app, bg="#E6CECE", bd=2, width=500, height=500)
            option_frame.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

            choose_text = tk.Label(option_frame, text="Choose Doctor To Delete", font=("Arial", 24, "bold"), bg="#E6CECE", fg="black")
            choose_text.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

            font_style = ("Arial", 16, "bold")
            
            for index, doctor_name in enumerate(doctors, start=0):
                register = tk.Button(option_frame, text=doctor_name.full_name(), command=lambda index=index, doctor_name=doctor_name: delete_doctor(index,doctor_name), width=30, height=2, font=font_style)
                register.grid(row=index+1, column=0, columnspan=2, padx=10, pady=10)

        else:
            print("No Doctors")
            error_text = tk.Label(app, text="There are No any Doctors In The System", font=("Arial", 24, "roman"), fg="black")
            error_text.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
            app.after(2000, error_text.destroy)

def button_event(app,admin,doctors,patients):

    print("Register/View")
    app = tk.Tk()
    app.geometry("1000x600")
    app.title("Hospital Management System")

    option_frame = tk.Frame(app, bg="#E6CECE", bd=2)
    option_frame.place(relx=0.5, rely=0.22, anchor=tk.CENTER)

    choose_text = tk.Label(option_frame, text="Choose From The Operation Below", font=("Arial", 24, "roman"), fg="black")

    font_style = ("Arial", 16, "bold")

    button1 = tk.Button(option_frame, text="Register", command=lambda: register(1,app,tk,doctors), width=30, height=2, font=font_style)
    button2 = tk.Button(option_frame, text="View", command=lambda: register(2, app,tk, doctors), width=30, height=2, font=font_style)
    button3 = tk.Button(option_frame, text="Update", command=lambda: register(3, app,tk, doctors), width=30, height=2, font=font_style)
    button4 = tk.Button(option_frame, text="Delete", command=lambda: register(4, app,tk, doctors), width=30, height=2, font=font_style)
    
    # Add space between buttons
    padx = 10
    pady = 10

    choose_text.grid(row=0, columnspan=2, padx=padx, pady=pady, sticky="nsew")
    button1.grid(row=1, column=0, padx=padx, pady=pady, sticky="nsew")
    button2.grid(row=1, column=1, padx=padx, pady=pady, sticky="nsew")
    button3.grid(row=2, column=0, padx=padx, pady=pady, sticky="nsew")
    button4.grid(row=2, column=1, padx=padx, pady=pady, sticky="nsew")

    # Center the buttons
    option_frame.grid_rowconfigure(0, weight=1)
    option_frame.grid_rowconfigure(1, weight=1)
    option_frame.grid_rowconfigure(2, weight=1)

    option_frame.grid_columnconfigure(0, weight=1)
    option_frame.grid_columnconfigure(1, weight=1)

    app.mainloop()

def view_patient(app,patients):

    if patients:

        app = tk.Tk()
        app.geometry("1000x600")
        app.title("Hospital Management System")

        option_frame = tk.Frame(app, bg="#E6CECE", bd=2)
        option_frame.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        choose_text = tk.Label(option_frame, text="List of Patients", font=("Arial", 24, "bold"), bg="#E6CECE", fg="black")
        choose_text.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

        # Scrollable Frame
        canvas = Canvas(option_frame, bg="#E6CECE", width=800, height=120, highlightthickness=0)
        canvas.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        scrollbar = Scrollbar(option_frame, orient="vertical", command=canvas.yview)
        scrollbar.grid(row=2, column=2, sticky="ns")

        inner_frame = Frame(canvas, bg="#E6CECE")
        inner_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=inner_frame, anchor="nw")
        
        for i, patient in enumerate(patients, start=1):
            patient_info = f'{i:^3}){patient.full_name():^30}|{patient.get_doctor():^40}|{patient.get_age():^5}|{patient.get_mobile():^15}|{patient.get_postcode():^10}|{patient.string_symptoms():^25}'
            patient_label = tk.Label(inner_frame, text=patient_info, font=("Arial", 12), bg="#E6CECE", fg="black")
            patient_label.grid(row=i+1, column=0, padx=10, pady=10, sticky="w")
        
        def resize(event):
            canvas.itemconfig(inner_frame, width=event.width)

        canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.configure(yscrollcommand=scrollbar.set)

    else:
        print("No Doctors")
        error_text = tk.Label(app, text="There are No any Patients In The System", font=("Arial", 24, "roman"), fg="black")
        error_text.place(relx=0.5, rely=0.93, anchor=tk.CENTER)
        app.after(2000, error_text.destroy)

def assign_doctor_patient(doctors,patients,app):

    def assign_doctor(patient):

        def assign_doctor_to_patient(index):

            print(doctors[index].full_name())

            option_frame1.destroy()
            doctor_frame.destroy()

            doctor_to_assign = doctors[index]
            patient_to_assign = patient

            patient.set_doctor(doctor_to_assign.full_name())
            doctors[index].add_patient(patient_to_assign.full_name())

            doctors[index].add_appointment(patient_to_assign.full_name())

            print(f'\nThe patient {patient_to_assign.full_name()} is now assign to the Dr. {doctor_to_assign.full_name()}, {doctor_to_assign.get_speciality().strip()}\n')

            success_label = tk.Label(app, text=f"The patient {patient_to_assign.full_name()} is now assign to the Dr. {doctor_to_assign.full_name()}", font=("Arial", 24, "roman"), fg="black")
            success_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

            def destroy_labels_and_app():
                success_label.destroy()
                app.destroy()

            app.after(2100, destroy_labels_and_app)


        print(patient.full_name())

        choose_text.destroy()
        option_frame.destroy()

        option_frame1 = tk.Frame(app, bg="#E6CECE", width=400, height=100)
        option_frame1.pack_propagate(False)
        option_frame1.place(relx=0.5, rely=0.15, anchor="center")

        symptoms_info = tk.Label(option_frame1, text=f"Symptoms of {patient.full_name()}", font=("Arial", 24, "roman"), bg="#E6CECE", fg="black")
        symptoms_info.grid(row=0, column=0, padx=10, pady=10)

        for index, symptom in enumerate(patient.print_symptoms(), start=1):
            register = tk.Label(option_frame1, text=f"{index}. {symptom}", font=("Arial", 14, "roman"), bg="#E6CECE", fg="black")
            register.grid(row=index, column=0, padx=10, pady=10)

        doctor_frame = tk.Frame(app, bg="#E6CECE", bd=2, width=500, height=500)
        doctor_frame.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

        choose_text_1 = tk.Label(doctor_frame, text="Choose Doctor To Assign", font=("Arial", 24, "roman"), fg="black")
        choose_text_1.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        font_style = ("Arial", 16, "bold")
        
        for index, doctor in enumerate(doctors, start=0):
            register = tk.Button(doctor_frame, text=doctor.full_name(), command=lambda index=index: assign_doctor_to_patient(index), width=30, height=2, font=font_style)
            register.grid(row=index+1, column=0, columnspan=2, padx=10, pady=10)

    if patients and doctors:
                    
        app = tk.Tk()
        app.geometry("1000x600")
        app.title("Hospital Management System")

        choose_text = tk.Label(app, text="Choose Patient To Assign Doctor", font=("Arial", 24, "roman"), fg="black")
        choose_text.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
            
        option_frame = tk.Frame(app, bg="#E6CECE", bd=2, width=500, height=500)
        option_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        font_style = ("Arial", 16, "bold")
        
        for index, patient in enumerate(patients, start=0):
            register = tk.Button(option_frame, text=patient.full_name(), command=lambda index=index, doctor_name=patient: assign_doctor(doctor_name), width=30, height=2, font=font_style)
            register.grid(row=index+1, column=0, columnspan=2, padx=10, pady=10)

        app.mainloop()
    
    else:
        print("No Patients")
        error_text = tk.Label(app, text="There are No Any Patients", font=("Arial", 24, "roman"), fg="black")
        error_text.place(relx=0.5, rely=0.93, anchor=tk.CENTER)
        app.after(2000, error_text.destroy)

def same_family(app,patients):
    if patients:
        surnames = set([patient.get_surname() for patient in patients])
        family = {surname: list(filter(lambda x: (x.get_surname() == surname), patients)) for surname in surnames}

        app = tk.Tk()
        app.geometry("1000x600")
        app.title("Patients by Family")

        option_frame = tk.Frame(app, bd=2, width=500, height=500)
        option_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        choose_text = tk.Label(app, text="Members of Same Family", font=("Arial", 24, "roman"), fg="black")
        choose_text.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

        row = 0
        for surname, members in family.items():
            tk.Label(option_frame, text=f"{surname} Family:", font=("Arial", 18, "bold")).grid(row=row, column=0, sticky="w", padx=10, pady=5)
            row += 1

            for index, patient in enumerate(members, start=1):
                tk.Label(option_frame, text=f"{index}. {patient}", font=("Arial", 14)).grid(row=row, column=0, sticky="w", padx=20)
                row += 1
        app.mainloop()
    else:
        print("No Patients")
        error_text = tk.Label(app, text="There are No Any Patients", font=("Arial", 24, "roman"), fg="black")
        error_text.place(relx=0.5, rely=0.93, anchor=tk.CENTER)
        app.after(2000, error_text.destroy)

def assign_illness(patients):
    
    def enter_illness(patient):

        def give_illness(patient):

            illness_value = illness.get()

            option_frame1.destroy()
            illness_frame.destroy()

            patient.set_illness(illness_value)
            print(f"\nPatient {patient.full_name()} has {illness_value}")
            print(patient.get_illness())

            success_label = tk.Label(app, text=f"The patient {patient.full_name()} is diagnosed with {illness_value}", font=("Arial", 24, "roman"), fg="black")
            success_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

            def destroy_labels_and_app():
                success_label.destroy()
                app.destroy()

            app.after(2100, destroy_labels_and_app)

        choose_text.destroy()
        option_frame.destroy()

        option_frame1 = tk.Frame(app, bg="#E6CECE", width=400, height=100)
        option_frame1.pack_propagate(False)
        option_frame1.place(relx=0.5, rely=0.15, anchor="center")

        symptoms_info = tk.Label(option_frame1, text=f"Symptoms of {patient.full_name()}", font=("Arial", 24, "roman"), bg="#E6CECE", fg="black")
        symptoms_info.grid(row=0, column=0, padx=10, pady=10)

        for index, symptom in enumerate(patient.print_symptoms(), start=1):
            register = tk.Label(option_frame1, text=f"{index}. {symptom}", font=("Arial", 14, "roman"), bg="#E6CECE", fg="black")
            register.grid(row=index, column=0, padx=10, pady=10)
        
        illness_frame = tk.Frame(app, bg="#E6CECE", bd=2, width=500, height=500)
        illness_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        label = tk.Label(illness_frame, text="Enter Illness", fg="black", bg="#E6CECE", font=("Arial", 14))
        label.grid(row=0, columnspan=2, padx=10, pady=10)

        illness = tk.Entry(illness_frame, width=20,font=("Arial", 14))
        illness.grid(row=1, columnspan=2, padx=10, pady=10)

        add_illness = tk.Button(illness_frame, text="Assign", fg="white", bg="#4158D0", font=("Arial", 20), width=15, height=1, command= lambda : give_illness(patient))
        add_illness.grid(row=2, columnspan=2, padx=10, pady=10)

    app = tk.Tk()
    app.geometry("1000x600")
    app.title("Hospital Management System")

    choose_text = tk.Label(app, text="Choose Patient To Assign Illness", font=("Arial", 24, "roman"), fg="black")
    choose_text.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
        
    option_frame = tk.Frame(app, bg="#E6CECE", bd=2, width=500, height=500)
    option_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    font_style = ("Arial", 16, "bold")
    
    for index, patient in enumerate(patients, start=0):
        register = tk.Button(option_frame, text=patient.full_name(), command=lambda index=index, doctor_name=patient: enter_illness(doctor_name), width=30, height=2, font=font_style)
        register.grid(row=index+1, column=0, columnspan=2, padx=10, pady=10)

    app.mainloop()

def relocate(app,patients,doctors):

    def patient_choose(patient):

        def assign_doctor_to_patient(doctor):

            doctor_frame.destroy()

            previous_doctor = patient.get_doctor()

            for index, item in enumerate(doctors):
                if previous_doctor == item.full_name():
                    previous_doctor = doctors[index]

                    previous_doctor.get_patient_list().remove(patient.full_name())
                    previous_doctor.get_appointment().remove(patient.full_name())
                    break

            patient.set_doctor(doctor.full_name())

            doctor.add_patient(patient.full_name())
            doctor.add_appointment(patient.full_name())

            print(f"Patient {patient.full_name()} has be assigned to {doctor.full_name()}")

            success_label = tk.Label(app, text=f"Patient {patient.full_name()} has be assigned to {doctor.full_name()}", font=("Arial", 24, "roman"), fg="black")
            success_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

            def destroy_labels_and_app():
                app.destroy()

            app.after(2500, destroy_labels_and_app)

        choose_text.destroy()
        option_frame.destroy()

        doctor_frame = tk.Frame(app, bg="#E6CECE", bd=2, width=500, height=500)
        doctor_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        choose_text_1 = tk.Label(doctor_frame, text="Choose Doctor To Relocate", font=("Arial", 24, "roman"), fg="black")
        choose_text_1.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        font_style = ("Arial", 16, "bold")
        
        for index, doctor in enumerate(doctors, start=0):
            register = tk.Button(doctor_frame, text=doctor.full_name(), command=lambda index=index,doc=doctor: assign_doctor_to_patient(doc), width=30, height=2, font=font_style)
            register.grid(row=index+1, column=0, columnspan=2, padx=10, pady=10)

    if patients:
        app = tk.Tk()
        app.geometry("1000x600")
        app.title("Hospital Management System")

        choose_text = tk.Label(app, text="Choose Patient To Relocate", font=("Arial", 24, "roman"), fg="black")
        choose_text.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
            
        option_frame = tk.Frame(app, bg="#E6CECE", bd=2, width=500, height=500)
        option_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        font_style = ("Arial", 16, "bold")
        
        for index, patient in enumerate(patients, start=0):
            register = tk.Button(option_frame, text=patient.full_name(), command=lambda index=index, doctor_name=patient: patient_choose(doctor_name), width=30, height=2, font=font_style)
            register.grid(row=index+1, column=0, columnspan=2, padx=10, pady=10)
    else:
        print("No Patients")
        error_text = tk.Label(app, text="There are No Any Patients", font=("Arial", 24, "roman"), fg="black")
        error_text.place(relx=0.5, rely=0.93, anchor=tk.CENTER)
        app.after(2000, error_text.destroy)

def discharge_patient(app,patients,discharged_patients):

    def choose_patient(index):

        choose_text.destroy()
        option_frame.destroy()

        patient_to_discharge = patients.pop(index)

        discharged_patients.append(patient_to_discharge)

        rewrite(patients)

        success_label = tk.Label(app, text=f"Good News! Patient {patient_to_discharge.full_name()} Has Been Discharged", font=("Arial", 24, "roman"), fg="black")
        success_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        def destroy_labels_and_app():
            app.destroy()

        app.after(2500, destroy_labels_and_app)

    if patients:
        app = tk.Tk()
        app.geometry("1000x600")
        app.title("Hospital Management System")

        choose_text = tk.Label(app, text="Choose Patient To Discharge", font=("Arial", 24, "roman"), fg="black")
        choose_text.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
            
        option_frame = tk.Frame(app, bg="#E6CECE", bd=2, width=500, height=500)
        option_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        font_style = ("Arial", 16, "bold")
        
        for index, patient in enumerate(patients, start=0):
            register = tk.Button(option_frame, text=patient.full_name(), command=lambda index=index: choose_patient(index), width=30, height=2, font=font_style)
            register.grid(row=index+1, column=0, columnspan=2, padx=10, pady=10)
    else:
        print("No Patients")
        error_text = tk.Label(app, text="There are No Any Patients", font=("Arial", 24, "roman"), fg="black")
        error_text.place(relx=0.5, rely=0.93, anchor=tk.CENTER)
        app.after(2000, error_text.destroy)

def view_discharge_patient(app,discharged_patient):

    if discharged_patient:

        app = tk.Tk()
        app.geometry("1000x600")
        app.title("Hospital Management System")

        option_frame = tk.Frame(app, bg="#E6CECE", bd=2)
        option_frame.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        choose_text = tk.Label(option_frame, text="List of Discharged Patients", font=("Arial", 24, "bold"), bg="#E6CECE", fg="black")
        choose_text.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

        # Scrollable Frame
        canvas = Canvas(option_frame, bg="#E6CECE", width=750, height=120, highlightthickness=0)
        canvas.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        scrollbar = Scrollbar(option_frame, orient="vertical", command=canvas.yview)
        scrollbar.grid(row=2, column=2, sticky="ns")

        inner_frame = Frame(canvas, bg="#E6CECE")
        inner_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=inner_frame, anchor="nw")
        
        for i, patient in enumerate(discharged_patient, start=1):
            patient_info = f'{i:^3}){patient.full_name():^30}|{patient.get_doctor():^40}|{patient.get_age():^5}|{patient.get_mobile():^15}|{patient.get_postcode():^10}|{patient.string_symptoms():^25}'
            patient_label = tk.Label(inner_frame, text=patient_info, font=("Arial", 12), bg="#E6CECE", fg="black")
            patient_label.grid(row=i+1, column=0, padx=10, pady=10, sticky="w")

        def resize(event):
            canvas.itemconfig(inner_frame, width=event.width)

        canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.configure(yscrollcommand=scrollbar.set)

    else:
        print("No Discharge Patient")
        error_text = tk.Label(app, text="There are No any Discharged Patient In The System", font=("Arial", 24, "roman"), fg="black")
        error_text.place(relx=0.5, rely=0.93, anchor=tk.CENTER)
        app.after(2000, error_text.destroy)

def update_admin(admin):

    def update_details():

        uname = username_entry.get().strip().capitalize()
        pwsd = password_entry.get().strip().capitalize()
        add = address_entry.get().strip().capitalize()

        if uname and pwsd and add:

            update_frame.destroy()

            admin.set_username(uname)
            admin.set_password(pwsd)
            admin.set_address(add)

            print()

            success_label = tk.Label(app, text=f"Admin Details Has Been Updated", font=("Arial", 24, "roman"), fg="black")
            success_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

            def destroy_labels_and_app():
                app.destroy()

            app.after(2500, destroy_labels_and_app)

        else:
            error_label = tk.Label(update_frame, text="Fields Can't Be Empty", font=("Arial", 24, "roman"), fg="black", bg="#E6CECE")
            error_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
            app.after(2000, error_label.destroy)

    app = tk.Tk()
    app.geometry("1000x600")
    app.title("Hospital Management System")


    update_frame = tk.Frame(app, bg="#E6CECE", borderwidth=2, relief=tk.SOLID, width=300, height=300)
    update_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    choose_text = tk.Label(update_frame, text="Enter Admin Details To Update", font=("Arial", 24, "bold"), bg="#E6CECE", fg="black")
    choose_text.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

    username = tk.Label(update_frame, text="Username:", font=("Arial", 18, "bold"), fg="black", bg="#E6CECE")
    username.grid(row=1, column=0, padx=10, pady=10, sticky="e")

    username_entry = tk.Entry(update_frame, width=30, font=("Arial", 18))
    username_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    password = tk.Label(update_frame, text="Password:", font=("Arial", 18, "bold"), fg="black", bg="#E6CECE")
    password.grid(row=2, column=0, padx=10, pady=10, sticky="e")

    password_entry = tk.Entry(update_frame, width=30, font=("Arial", 18),show="*")
    password_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    address = tk.Label(update_frame, text="Address:", font=("Arial", 18, "bold"), fg="black", bg="#E6CECE")
    address.grid(row=3, column=0, padx=10, pady=10, sticky="e")

    address_entry = tk.Entry(update_frame, width=30, font=("Arial", 18))
    address_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")

    update_button = tk.Button(update_frame, text="Update", font=("Arial", 20, "bold"), fg="white", bg="#4158D0", width=15, height=1, command=update_details)
    update_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    app.mainloop()