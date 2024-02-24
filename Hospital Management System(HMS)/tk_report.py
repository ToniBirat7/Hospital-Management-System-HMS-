import tkinter as tk

def doctor_patient_report(patients, doctors, app):

    app.destroy()

    categories = ['Doctors', 'Patients']
    values = [len(doctors), len(patients)]

    root = tk.Tk()
    root.title("Hospital Management System Report")

    frame = tk.Frame(root)
    frame.grid(row=0, column=0)

    title_label = tk.Label(frame, text="Total Number of Patients and Doctor", font=("Arial", 20))
    title_label.pack()

    canvas = tk.Canvas(frame, width=600, height=400, bg="white")
    canvas.pack(expand=True)

    max_value = max(values)
    if max_value == 0:
        max_value = 1

    bar_width = 50
    bar_spacing = 20
    x_start = 50
    y_start = 300

    for i, (category, value) in enumerate(zip(categories, values)):
        
        x0 = x_start + i * (bar_width + bar_spacing)
        y0 = y_start
        x1 = x0 + bar_width
        y1 = y_start - (value / max_value) * 200

        canvas.create_rectangle(x0, y0, x1, y1, fill="blue")

        label_x = (x0 + x1) / 2
        label_y = y_start + 10
        canvas.create_text(label_x, label_y, text=category)

        value_x = (x0 + x1) / 2
        value_y = y1 - 10
        canvas.create_text(value_x, value_y, text=value)
    
    x_label = tk.Label(frame, text="Doctors and Patients", font=("Arial", 16),bg="white")
    x_label.pack()
    x_label.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

    y_label = canvas.create_text(20, 200, text="Values", font=("Arial", 16), anchor=tk.CENTER, angle=90)
    root.mainloop()

def patient_per_doctor(patients_per_doctor, app):

    app.destroy()

    categories = patients_per_doctor.keys()
    values = patients_per_doctor.values()

    root = tk.Tk()
    root.title("Hospital Management System Report")

    frame = tk.Frame(root)
    frame.grid(row=0, column=0)

    title_label = tk.Label(frame, text="Patients Per Doctor", font=("Arial", 20))
    title_label.pack()

    canvas = tk.Canvas(frame, width=600, height=400, bg="white")
    canvas.pack(expand=True)

    max_value = max(values)
    if max_value == 0:
        max_value = 1

    bar_width = 50
    bar_spacing = 20
    x_start = 50
    y_start = 300

    for i, (category, value) in enumerate(zip(categories, values)):
        
        x0 = x_start + i * (bar_width + bar_spacing)
        y0 = y_start
        x1 = x0 + bar_width
        y1 = y_start - (value / max_value) * 200

        canvas.create_rectangle(x0, y0, x1, y1, fill="blue")

        label_x = (x0 + x1) / 2
        label_y = y_start + 10
        canvas.create_text(label_x, label_y, text=category)

        value_x = (x0 + x1) / 2
        value_y = y1 - 10
        canvas.create_text(value_x, value_y, text=value)
    
    x_label = tk.Label(frame, text="Doctors", font=("Arial", 16),bg="white")
    x_label.pack()
    x_label.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

    y_label = canvas.create_text(20, 200, text="Patients", font=("Arial", 16), anchor=tk.CENTER, angle=90)

    root.mainloop()

def appointment_per_month(appointments_per_doctor, app):

    app.destroy()

    categories = appointments_per_doctor.keys()
    values = appointments_per_doctor.values()

    root = tk.Tk()
    root.title("Hospital Management System Report")

    frame = tk.Frame(root)
    frame.grid(row=0, column=0)

    title_label = tk.Label(frame, text="Appointments Per Month Per Doctor", font=("Arial", 20))
    title_label.pack()

    canvas = tk.Canvas(frame, width=600, height=400, bg="white")
    canvas.pack(expand=True)

    max_value = max(values)
    if max_value == 0:
        max_value = 1

    bar_width = 50
    bar_spacing = 20
    x_start = 50
    y_start = 300

    for i, (category, value) in enumerate(zip(categories, values)):
        
        x0 = x_start + i * (bar_width + bar_spacing)
        y0 = y_start
        x1 = x0 + bar_width
        y1 = y_start - (value / max_value) * 200

        canvas.create_rectangle(x0, y0, x1, y1, fill="blue")

        label_x = (x0 + x1) / 2
        label_y = y_start + 10
        canvas.create_text(label_x, label_y, text=category)

        value_x = (x0 + x1) / 2
        value_y = y1 - 10
        canvas.create_text(value_x, value_y, text=value)
    
    x_label = tk.Label(frame, text="Doctors", font=("Arial", 16),bg="white")
    x_label.pack()
    x_label.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

    y_label = canvas.create_text(20, 200, text="Patients", font=("Arial", 16), anchor=tk.CENTER, angle=90)

    root.mainloop()

def patient_illness(illness_type, app):
    app.destroy()

    categories = []
    values = []

    for i,j in illness_type.items():
            categories.append(i)
            values.append(len(j))

    root = tk.Tk()
    root.title("Hospital Management System Report")

    frame = tk.Frame(root)
    frame.grid(row=0, column=0)

    title_label = tk.Label(frame, text="Appointments Per Month Per Doctor", font=("Arial", 20))
    title_label.pack()

    canvas = tk.Canvas(frame, width=600, height=400, bg="white")
    canvas.pack(expand=True)

    max_value = max(values)
    if max_value == 0:
        max_value = 1

    bar_width = 50
    bar_spacing = 20
    x_start = 50
    y_start = 300

    for i, (category, value) in enumerate(zip(categories, values)):
        
        x0 = x_start + i * (bar_width + bar_spacing)
        y0 = y_start
        x1 = x0 + bar_width
        y1 = y_start - (value / max_value) * 200

        canvas.create_rectangle(x0, y0, x1, y1, fill="blue")

        label_x = (x0 + x1) / 2
        label_y = y_start + 10
        canvas.create_text(label_x, label_y, text=category)

        value_x = (x0 + x1) / 2
        value_y = y1 - 10
        canvas.create_text(value_x, value_y, text=value)
    
    x_label = tk.Label(frame, text="Illness Type", font=("Arial", 16),bg="white")
    x_label.pack()
    x_label.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

    y_label = canvas.create_text(20, 200, text="Values", font=("Arial", 16), anchor=tk.CENTER, angle=90)

    root.mainloop()