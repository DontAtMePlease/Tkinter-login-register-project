from tkinter import messagebox
import tkinter as tk
import json

class app(object):

    def register(self):
        with open('Accounts.json', 'r') as f:
            data = json.load(f)
            Save1 = data['Save1']['Used']
            Save2 = data['Save2']['Used']
            Save3 = data['Save3']['Used']
            Save4 = data['Save4']['Used']
            Save5 = data['Save5']['Used']
            f.close()

            username_text = self.username_field.get()
            password_text = self.password_field.get()

            if(Save1 == False):
                jsonFile = open("Accounts.json", "r")  # Open the JSON file for reading
                data = json.load(jsonFile)  # Read the JSON into the buffer
                jsonFile.close()  # Close the JSON file

                data['Save1']['Username'] = username_text
                data['Save1']['Password'] = password_text
                data['Save1']['Used'] = True

                jsonFile = open("Accounts.json", "w+") # <------ Saves Changes
                jsonFile.write(json.dumps(data))    # ^
                jsonFile.close()

                self.r_window.destroy()
                self.gui()
            elif (Save2 == False):
                jsonFile = open("Accounts.json", "r")  # Open the JSON file for reading
                data = json.load(jsonFile)  # Read the JSON into the buffer
                jsonFile.close()  # Close the JSON file

                data['Save2']['Username'] = username_text
                data['Save2']['Password'] = password_text
                data['Save2']['Used'] = True

                jsonFile = open("Accounts.json", "w+")  # <------ Saves Changes
                jsonFile.write(json.dumps(data))  # ^
                jsonFile.close()

                self.r_window.destroy()
                self.gui()
            elif (Save3 == False):
                jsonFile = open("Accounts.json", "r")  # Open the JSON file for reading
                data = json.load(jsonFile)  # Read the JSON into the buffer
                jsonFile.close()  # Close the JSON file

                data['Save3']['Username'] = username_text
                data['Save3']['Password'] = password_text
                data['Save3']['Used'] = True

                jsonFile = open("Accounts.json", "w+")  # <------ Saves Changes
                jsonFile.write(json.dumps(data))  # ^
                jsonFile.close()

                self.r_window.destroy()
                self.gui()
            elif(Save4 == False):
                jsonFile = open("Accounts.json", "r")  # Open the JSON file for reading
                data = json.load(jsonFile)  # Read the JSON into the buffer
                jsonFile.close()  # Close the JSON file

                data['Save4']['Username'] = username_text
                data['Save4']['Password'] = password_text
                data['Save4']['Used'] = True

                jsonFile = open("Accounts.json", "w+")  # <------ Saves Changes
                jsonFile.write(json.dumps(data))  # ^
                jsonFile.close()

                self.r_window.destroy()
                self.gui()
            elif(Save5 == False):
                jsonFile = open("Accounts.json", "r")  # Open the JSON file for reading
                data = json.load(jsonFile)  # Read the JSON into the buffer
                jsonFile.close()  # Close the JSON file

                data['Save5']['Username'] = username_text
                data['Save5']['Password'] = password_text
                data['Save5']['Used'] = True

                jsonFile = open("Accounts.json", "w+")  # <------ Saves Changes
                jsonFile.write(json.dumps(data))  # ^
                jsonFile.close()

                self.r_window.destroy()
                self.gui()
            else:
                tk.messagebox.showerror("Error", "All accounts filled")




    def register_window(self):
        self.main.destroy() # Closes other window
        # - - - - - WINDOW - - - - -
        self.r_window = tk.Tk()
        self.r_window.resizable(0,0)
        self.r_window.geometry("300x230")
        self.r_window.title("Register")
        self.r_window.configure(background="white")

        # - - - - - WINDOW ITEMS - - - - -
        r_title_label = tk.Label(text="Register Window", bg="black", width="300", height="2", fg="white", font=("Times New Roman", 15)).pack()
        r_username_label = tk.Label(bg="white", text="Username", font=("helvetica", 10)).pack()
        self.username_field = tk.Entry(width=20)
        self.username_field.pack()
        r_filler = tk.Label(bg="white")
        r_filler.pack()
        r_password_label = tk.Label(bg="white", text="Password", font=("helvetica", 10)).pack()
        self.password_field = tk.Entry(width=20)
        self.password_field.pack()
        r_filler2 = tk.Label(text="", bg="white")
        r_filler2.pack()
        register_button = tk.Button(text="Register", command=self.register)
        register_button.pack()

        self.r_window.mainloop()

    def login_window(self):
        self.main.destroy()
        self.lwindow = tk.Tk()
        self.lwindow.resizable(0,0)
        self.lwindow.geometry("300x230")
        self.lwindow.title("Login Window")

        # - - - - - Window Items - - - - -
        title_label = tk.Label(text="Login Window", bg="black", width="300", height="2", fg="white", font=("Times New Roman", 15)).pack()
        username_label = tk.Label(text="Username", font=("helvetica", 10)).pack()
        self.login_username_field = tk.Entry(width=20)
        self.login_username_field.pack()
        tk.Label(text="").pack()
        password_label = tk.Label(text="Password", font=("helvetica", 10)).pack()
        self.login_password_field = tk.Entry(width=20)
        self.login_password_field.pack()
        tk.Label(text="").pack()
        login_button = tk.Button(text="Login", command=self.login).pack()

        self.lwindow.mainloop()

    def login(self):
        with open('Accounts.json', 'r') as f:
            data = json.load(f)
            Save1 = data['Save1']['Used']
            Save2 = data['Save2']['Used']
            Save3 = data['Save3']['Used']
            Save4 = data['Save4']['Used']
            Save5 = data['Save5']['Used']

            if Save1 == True:
                json_username = data['Save1']['Username']
                json_password = data['Save1']['Password']
                if json_username == self.login_username_field.get() and json_password == self.login_password_field.get():
                    self.lwindow.destroy()
                    self.gui()
                    return
            if Save2 == True:
                json_username = data['Save2']['Username']
                json_password = data['Save2']['Password']
                if json_username == self.login_username_field.get() and json_password == self.login_password_field.get():
                    self.lwindow.destroy()
                    self.gui()
                    return

            if Save3 == True:
                json_username = data['Save3']['Username']
                json_password = data['Save3']['Password']
                if json_username == self.login_username_field.get() and json_password == self.login_password_field.get():
                    self.lwindow.destroy()
                    self.gui()
                    return

            if Save4 == True:
                json_username = data['Save4']['Username']
                json_password = data['Save4']['Password']
                if json_username == self.login_username_field.get() and json_password == self.login_password_field.get():
                    self.lwindow.destroy()
                    self.gui()
                    return

            if Save5 == True:
                json_username = data['Save5']['Username']
                json_password = data['Save5']['Password']
                if json_username == self.login_username_field.get() and json_password == self.login_password_field.get():
                    self.lwindow.destroy()
                    self.gui()
                    return

            tk.messagebox.showerror("Error", "Failed to login please try again")

            f.close()

    def deleteAccount1(self):
        jsonFile = open("Accounts.json", "r")  # Open the JSON file for reading
        data = json.load(jsonFile)  # Read the JSON into the buffer
        jsonFile.close()  # Close the JSON file

        data['Save1']['Used'] = False

        jsonFile = open("Accounts.json", "w+")  # <------ Saves Changes
        jsonFile.write(json.dumps(data))        # ^
        jsonFile.close()

        self.guilabel1.config(text="Used: False")
        self.button1.config(text="null")

    def deleteAccount2(self):
        jsonFile = open("Accounts.json", "r")  # Open the JSON file for reading
        data = json.load(jsonFile)  # Read the JSON into the buffer
        jsonFile.close()  # Close the JSON file

        data['Save2']['Used'] = False

        jsonFile = open("Accounts.json", "w+")  # <------ Saves Changes
        jsonFile.write(json.dumps(data))  # ^
        jsonFile.close()

        self.guilabel2.config(text="Used: False")
        self.button2.config(text="null")

    def deleteAccount3(self):
        jsonFile = open("Accounts.json", "r")  # Open the JSON file for reading
        data = json.load(jsonFile)  # Read the JSON into the buffer
        jsonFile.close()  # Close the JSON file

        data['Save3']['Used'] = False

        jsonFile = open("Accounts.json", "w+")  # <------ Saves Changes
        jsonFile.write(json.dumps(data))  # ^
        jsonFile.close()

        self.guilabel3.config(text="Used: False")
        self.button3.config(text="null")

    def deleteAccount4(self):
        jsonFile = open("Accounts.json", "r")  # Open the JSON file for reading
        data = json.load(jsonFile)  # Read the JSON into the buffer
        jsonFile.close()  # Close the JSON file

        data['Save4']['Used'] = False

        jsonFile = open("Accounts.json", "w+")  # <------ Saves Changes
        jsonFile.write(json.dumps(data))  # ^
        jsonFile.close()

        self.guilabel4.config(text="Used: False")
        self.button4.config(text="null")

    def deleteAccount5(self):
        jsonFile = open("Accounts.json", "r")  # Open the JSON file for reading
        data = json.load(jsonFile)  # Read the JSON into the buffer
        jsonFile.close()  # Close the JSON file

        data['Save5']['Used'] = False

        jsonFile = open("Accounts.json", "w+")  # <------ Saves Changes
        jsonFile.write(json.dumps(data))  # ^
        jsonFile.close()

        self.guilabel5.config(text="Used: False")
        self.button5.config(text="null")

    def gui(self):
        self.guiwindow = tk.Tk()
        self.guiwindow.title("Main")

        # - - - - - Check Used - - - - -
        with open('Accounts.json', 'r') as h:
            data = json.load(h)
            used1 = data['Save1']['Used']
            used2 = data['Save2']['Used']
            used3 = data['Save3']['Used']
            used4 = data['Save4']['Used']
            used5 = data['Save5']['Used']


        # - - - - - LABELS - - - - -
        if used1 == True:
            self.guilabel1 = tk.Label(text="Used: True", font=("Time New Roman", 10))
            self.guilabel1.grid(column=0, row=0)
            button1text = "Delete " + data['Save1']['Username']
        else:
            self.guilabel1 = tk.Label(text="Used: False", font=("Time New Roman", 10))
            self.guilabel1.grid(column=0, row=0)
            button1text = "null"
        if used2 == True:
            self.guilabel2 = tk.Label(text="Used: True", font=("Time New Roman", 10))
            self.guilabel2.grid(column=0, row=1)
            button2text = "Delete " + data['Save2']['Username']
        else:
            self.guilabel2 = tk.Label(text="Used: False", font=("Time New Roman", 10))
            self.guilabel2.grid(column=0, row=1)
            button2text = "null"
        if used3 == True:
            self.guilabel3 = tk.Label(text="Used: True", font=("Time New Roman", 10))
            self.guilabel3.grid(column=0, row=2)
            button3text = "Delete " + data['Save3']['Username']
        else:
            self.guilabel3 = tk.Label(text="Used: False", font=("Time New Roman", 10))
            self.guilabel3.grid(column=0, row=2)
            button3text = "null"
        if used4 == True:
            self.guilabel4 = tk.Label(text="Used: True", font=("Time New Roman", 10))
            self.guilabel4.grid(column=0, row=3)
            button4text = "Delete " + data['Save4']['Username']
        else:
            self.guilabel4 = tk.Label(text="Used: False", font=("Time New Roman", 10))
            self.guilabel4.grid(column=0, row=3)
            button4text = "null"
        if used5 == True:
            self.guilabel5 = tk.Label(text="Used: True", font=("Time New Roman", 10))
            self.guilabel5.grid(column=0, row=4)
            button5text = "Delete " + data['Save5']['Username']
        else:
            self.guilabel5 = tk.Label(text="Used: False", font=("Time New Roman", 10))
            self.guilabel5.grid(column=0, row=4)
            button5text = "null"

        # - - - - - BUTTONS - - - - -
        self.button1 = tk.Button(text=button1text, command=self.deleteAccount1)
        self.button1.grid(column=1, row=0)
        self.button2 = tk.Button(text=button2text, command=self.deleteAccount2)
        self.button2.grid(column=1, row=1)
        self.button3 = tk.Button(text=button3text, command=self.deleteAccount3)
        self.button3.grid(column=1, row=2)
        self.button4 = tk.Button(text=button4text, command=self.deleteAccount4)
        self.button4.grid(column=1, row=3)
        self.button5 = tk.Button(text=button5text, command=self.deleteAccount5)
        self.button5.grid(column=1, row=4)

        h.close()
        self.guiwindow.mainloop()

    def main_window(self):
        self.main = tk.Tk()
        self.main.resizable(0,0)
        self.main.geometry("300x230")
        self.main.title("Project")
        self.main.configure(background="white")

        title_label = tk.Label(text="Login Forum", bg="black", width="300", height="2", fg="white", font=("Times New Roman", 15)).pack()
        tk.Label(text="").pack() # <---- Space Filler
        tk.Button(text="Login", height="2", width="30", command=self.login_window).pack()
        tk.Label(text="").pack()  # <---- Space Filler
        tk.Button(text="Register", height="2", width="30", command=self.register_window).pack()

        self.main.mainloop()

App = app()
App.main_window()
