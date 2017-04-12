#Program that users browse reports and look at files

import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror

LARGE_FONT = ("Verdana", 12)



class FDAapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "File Download Application")
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand= True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (LoginPage, PageOne, ReportsPage, Encrypt_file_page):

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column = 0, sticky="nsew")

        self.show_frame(LoginPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class LoginPage(tk.Frame):

    controller = ""

    def __init__(self, parent, controller):

        self.controller = controller

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Login Page", font=LARGE_FONT, pady=10)
        label.grid(row=0, sticky='n')
        userName_label = tk.Label(self, text="Username")
        password_label = tk.Label(self, text="Password")

        userName_label.grid(row = 1)
        password_label.grid(row = 2)

        self.username = tk.Entry(self, width = 15)
        self.password = tk.Entry(self, show="*", width = 15)


        self.username.grid(row=1, column = 1)
        self.password.grid(row=2, column = 1)


        loginButton = ttk.Button(self, text="Login",  command=self.log_in)

        loginButton.grid(row=3, column =1, sticky='w', pady=4)



    def log_in(self):
        username = self.username.get()
        password = self.password.get()

        if username == 'Will':
            if password == 'password':
                self.controller.show_frame(PageOne)







class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        top = "Hello!"
        label = tk.Label(self, text=top, font=LARGE_FONT, pady=10)
        label.grid(row=0, sticky='n')

        view_reports_button = ttk.Button(self, text="View Reports",
                                command=lambda: controller.show_frame(ReportsPage))

        view_reports_button.grid(row=1, column=0, sticky='w', pady=4)

        encrypt_file_button = ttk.Button(self, text="Encrypt File",
                                        command=lambda: controller.show_frame(Encrypt_file_page))

        encrypt_file_button.grid(row=2, column=0, sticky='w', pady=4)


class ReportsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Reports:", font=LARGE_FONT, pady=10)
        label.grid(row=0, sticky='n')


class Encrypt_file_page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Encrypt file:", font=LARGE_FONT, pady=10)
        label.grid(row=0, sticky='n')

        self.button = Button(self, text="Browse for file", command=self.load_file,width=10)
        self.button.grid(row=1,column=0, sticky=W)

        self.encrypt = Button(self, text="Encrypt file", command=lambda: controller.show_frame(LoginPage), width=10)
        self.encrypt.grid(row=2, column=0, sticky=W)

    def load_file(self):
        fname = askopenfilename(filetypes=(("Template files", "*.tplate"),
                                           ("HTML files", "*.html;*.htm"),
                                           ("All files", "*.*") ))


        if fname:
            try:

                print("here is where we encode with key")
                print("""here it comes: self.settings["template"].set(fname)""")
            except:  # <- naked except is a bad idea
                showerror("Open Source File", "Failed to read file\n'%s'" % fname)
            return





app = FDAapp()
app.mainloop()



