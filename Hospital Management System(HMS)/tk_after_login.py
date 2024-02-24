import tkinter as tk
from tk_options import button_event, view_patient, assign_doctor_patient, same_family, assign_illness, relocate, discharge_patient, view_discharge_patient, update_admin
from tk_report import doctor_patient_report,patient_per_doctor,appointment_per_month,patient_illness

def report(admin,doctors,patients):
    
    patients_per_doctor,appointments_per_doctor,number_of_patient_illness = admin.report(patients,doctors)

    app = tk.Tk()
    app.geometry("1000x600")
    app.title("Hospital Management System")

    # Create a frame for the report options
    option_frame = tk.Frame(app, bg="#E6CECE", bd=2)
    option_frame.place(relx=0.5, rely=0.48, anchor=tk.CENTER)

    # Create labels and buttons for the report options
    choose_text = tk.Label(option_frame, text="Choose Report Options From Below", font=("Arial", 24, "roman"), bg="#E6CECE", fg="black")
    choose_text.grid(row=0, columnspan=2, padx=10, pady=10)

    font_style = ("Arial", 14, "bold")

    button1 = tk.Button(option_frame, text="Number Of Doctors and Patients", command=lambda: doctor_patient_report(patients, doctors, app), width=30, height=2, font=font_style)
    button2 = tk.Button(option_frame, text="Patient Per Doctor", command=lambda: patient_per_doctor(patients_per_doctor, app), width=30, height=2, font=font_style)
    button3 = tk.Button(option_frame, text="Appointments Per Month Per Doctor", command=lambda: appointment_per_month(appointments_per_doctor, app), width=30, height=2, font=font_style)
    button4 = tk.Button(option_frame, text="Number Of Patients Based On Illness Types", command=lambda: patient_illness(number_of_patient_illness, app), width=40, height=2, font=font_style)

    padx = 10
    pady = 10

    button1.grid(row=1, column=0, padx=padx, pady=pady, sticky="nsew")
    button2.grid(row=1, column=1, padx=padx, pady=pady, sticky="nsew")
    button3.grid(row=2, column=0, padx=padx, pady=pady, sticky="nsew")
    button4.grid(row=2, column=1, padx=padx, pady=pady, sticky="nsew")

    # Configure row and column weights for resizing
    option_frame.grid_rowconfigure(0, weight=1)
    option_frame.grid_rowconfigure(1, weight=1)
    option_frame.grid_rowconfigure(2, weight=1)

    option_frame.grid_columnconfigure(0, weight=1)
    option_frame.grid_columnconfigure(1, weight=1)

    # Start the Tkinter event loop
    app.mainloop()

def admin_panel(admin, doctors, patients, discharged_patients):
    app = tk.Tk()
    app.geometry("1000x600")
    app.title("Hospital Management System")

    option_frame = tk.Frame(app, bg="#E6CECE", bd=2)
    option_frame.place(relx=0.5, rely=0.55, anchor=tk.CENTER)

    admin_text = tk.Label(app, text="Welcome Admin!", font=("Arial", 24, "bold"), fg="black")
    admin_text.place(relx=0.5, rely=0.1, anchor='center')

    choose_text = tk.Label(option_frame, text="Choose From The Operation Below", font=("Arial", 24, "roman"), fg="#3E2723")

    font_style = ("Arial", 16, "bold")

    button1 = tk.Button(option_frame, text="Register/view/update/delete doctor", command=lambda: button_event(app,admin,doctors,patients), width=30, height=1, font=font_style)
    button2 = tk.Button(option_frame, text="Discharge patients", command=lambda: discharge_patient(app,patients,discharged_patients), width=30, height=1, font=font_style)
    button3 = tk.Button(option_frame, text="View discharged patient", command=lambda: view_discharge_patient(app,discharged_patients), width=30, height=1, font=font_style)
    button4 = tk.Button(option_frame, text="Assign doctor to a patient", command=lambda: assign_doctor_patient(doctors,patients,app), width=30, height=1, font=font_style)
    button5 = tk.Button(option_frame, text="Update admin details", command=lambda: update_admin(admin), width=30, height=1, font=font_style)
    button6 = tk.Button(option_frame, text="View Patient", command=lambda: view_patient(app,patients), width=30, height=1, font=font_style)
    button7 = tk.Button(option_frame, text="View Patient of Same Family", command=lambda: same_family(app,patients), width=30, height=1, font=font_style)
    button8 = tk.Button(option_frame, text="Relocate Patient", command=lambda: relocate(app,patients,doctors), width=30, height=1, font=font_style)
    button9 = tk.Button(option_frame, text="Display Report", command=lambda: report(admin,doctors,patients), width=30, height=1, font=font_style)
    button10 = tk.Button(option_frame, text="Assign Illness", command=lambda: assign_illness(patients), width=30, height=1, font=font_style)
    button11 = tk.Button(option_frame, text="Quit", command=app.destroy, width=30, height=1, font=font_style)

    # Add space between buttons
    padx = 7
    pady = 7

    choose_text.grid(row=0, columnspan=2, padx=padx, pady=pady, sticky="nsew")
    button1.grid(row=1, column=0, padx=padx, pady=pady, sticky="nsew")
    button2.grid(row=1, column=1, padx=padx, pady=pady, sticky="nsew")
    button3.grid(row=2, column=0, padx=padx, pady=pady, sticky="nsew")
    button4.grid(row=2, column=1, padx=padx, pady=pady, sticky="nsew")
    button5.grid(row=3, column=0, padx=padx, pady=pady, sticky="nsew")
    button6.grid(row=3, column=1, padx=padx, pady=pady, sticky="nsew")
    button7.grid(row=4, column=0, padx=padx, pady=pady, sticky="nsew")
    button8.grid(row=4, column=1, padx=padx, pady=pady, sticky="nsew")
    button9.grid(row=5, column=0, padx=padx, pady=pady, sticky="nsew")
    button10.grid(row=5, column=1, padx=padx, pady=pady, sticky="nsew")
    button11.grid(row=6, columnspan=2, padx=padx, pady=pady, sticky="nsew")

    # Center the buttons
    for i in range(8):
        option_frame.grid_rowconfigure(i, weight=1)
        option_frame.grid_columnconfigure(i, weight=1)

    app.mainloop()

