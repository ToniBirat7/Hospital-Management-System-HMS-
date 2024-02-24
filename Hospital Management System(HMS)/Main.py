from tk_after_login import admin_panel
from Initializer import admin,doctors,patients,discharged_patients
import tkinter as tk

def credentials():
    uname = username.get()
    pswd = password.get()
    print(uname, pswd)

    if admin.login(uname, pswd):
        app.destroy()
        admin_panel(admin, doctors, patients, discharged_patients)
    elif uname == '' or pswd == '':
        error_msg = tk.Label(app, text="Please Enter Username and Password Both", fg="black", font=("Arial", 24))
        error_msg.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
        app.after(1500, error_msg.destroy)
    else:
        error_msg = tk.Label(app, text="Username or Password Didn't Match", fg="black", font=("Arial", 24))
        error_msg.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
        app.after(2000, error_msg.destroy)

app = tk.Tk()
app.geometry("1000x600")
app.title("Hospital Management System")

welcome_text = tk.Label(app, text="Welcome to BCU Hospital Management System!", fg="black", font=("Arial", 24))
welcome_text.place(relx=0.5, rely=0.16, anchor=tk.CENTER)

login_frame = tk.Frame(app, bg="#E6CECE", bd=2, relief=tk.SOLID, width=300, height=250)
login_frame.pack_propagate(False)
login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

admin_login = tk.Label(login_frame, text="Admin Login", fg="black", bg="#E6CECE", font=("Arial", 24))
admin_login.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

username_label = tk.Label(login_frame, text="Username:", fg="black", bg="#E6CECE", font=("Arial", 14))
username_label.grid(row=1, column=0, padx=10, pady=(20, 5), sticky="e")

password_label = tk.Label(login_frame, text="Password:", fg="black", bg="#E6CECE", font=("Arial", 14))
password_label.grid(row=2, column=0, padx=10, pady=(0, 0), sticky="e")

username = tk.Entry(login_frame, width=20,font=("Arial", 14))
password = tk.Entry(login_frame, width=20,font=("Arial", 14))

username.grid(row=1, column=1, padx=10, pady=(20, 10))
password.grid(row=2, column=1, padx=10, pady=(20, 10))

login = tk.Button(login_frame, text="Login", fg="white", bg="#4158D0", font=("Arial", 20), width=15, height=1, command=credentials)
login.grid(row=3, columnspan=2, padx=10, pady=10)

app.mainloop()
