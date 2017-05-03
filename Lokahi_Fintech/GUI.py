
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from functools import partial
import Crypto

from Crypto.Cipher import ARC4
import hashlib
import urllib.request
import requests




import psycopg2


global conn


# conn = psycopg2.connect(dbname="users", user="postgres", password="password")
#conn = "test"
conn = psycopg2.connect("postgres://pkieqmtpiorhih:b7fd461ef59e70babae7fd38506faaa1f57cd8cd27a2c107cacd8b1223aa818c@ec2-107-21-205-25.compute-1.amazonaws.com:5432/dee7mbd0c0kua9")
#conn = "test"



class Window:
    def __init__(self):
        self.root = Tk()
        self.root.wm_geometry(u'10x10+0+0')
        self.root.geometry('{}x{}'.format(500,500))
        self.root.protocol("WM_DELETE_WINDOW", self.root.destroy)

        self.login_page = Frame(self.root)
        self.title = Label(self.login_page, text="Login to account")

        self.username_label = Label(self.login_page, text="Username:")

        self.username_entry = Entry(self.login_page)
        self.username_entry.focus_set()
        self.password_label = Label(self.login_page, text="Password:")
        self.password_entry = Entry(self.login_page, show="*", width = 15)
        self.login_button = Button(self.login_page, text="Login", command=self.login)

        self.title.grid(row='0')
        self.username_label.grid(row='1', column='0', pady='20')
        self.username_entry.grid(row='1', column='1', pady='2')
        self.password_label.grid(row='2', column='0', pady='2')
        self.password_entry.grid(row='2', column='1', pady='2')
        self.login_button.grid(row='3', column='1', pady='2')

        #first page

        self.first_page = Frame(self.root)
        self.encryptfile_button = Button(self.first_page, text = 'Encrypt File', command=self.show_encryptPage, height = 10, width = 15)

        self.reports_button = Button(self.first_page, text='Browse Reports', command=self.show_reportsPage, height = 10, width = 15)

        self.first_page_title = Label(self.first_page, text="Main Page")
        self.first_page_title.grid(row='0')
        self.encryptfile_button.grid(row='1', column = '0', pady='3', padx='3')
        self.reports_button.grid(row='1', column = '1', pady='3', padx='3')


        #encrypt file page

        self.encrypt_file_page = Frame(self.root)
        self.encr_title = Label(self.encrypt_file_page, text="Encypt File")
        self.browse_label = Label(self.encrypt_file_page, text="Browse for File")
        self.browseButton = Button(self.encrypt_file_page, text = "Browse:", command = self.loadtemplate)
        self.fileEntry = Entry(self.encrypt_file_page)
        self.fileLabel = Label(self.encrypt_file_page, text="File name: ")
        self.keylabel = Label(self.encrypt_file_page, text = "Encryption key: ")
        self.key_entry = Entry(self.encrypt_file_page)
        self.encrypt_button = Button(self.encrypt_file_page, text = 'Encrypt', command = self.encryptFile)
        self.back_button = Button(self.encrypt_file_page, text = 'Back', command= self.show_mainPage)

        self.encr_title.grid(row = 0)
        self.browse_label.grid(row=1, column=0)
        self.browseButton.grid(row=1, column=1)
        self.fileEntry.grid(row = 2, column = 1)
        self.fileLabel.grid(row = 2, column = 0)
        self.keylabel.grid(row=3, column = 0)
        self.key_entry.grid(row=3, column=1)
        self.encrypt_button.grid(row=4, column =0)
        self.back_button.grid(row = 4, column = 1)


        #reports page

        self.reports_page = Frame(self.root)
        self.back_button2 = Button(self.reports_page, text='Back', command=self.show_mainPage)
        self.reports_title = Label(self.reports_page, text="Reports")
        self.reports_title.pack()
        self.back_button2.pack()




        self.docs_page = Frame(self.root)



    def login(self, *args):
        print("Do login stuff")
        #do login stuff
        #self.login_page.pack_forget()
        #self.encrypt_file_page.forget()
        #self.reports_page.pack_forget()
        #self.first_page.pack()

        self.user = self.username_entry.get()
        password = self.password_entry.get()

        #send to login script

        # URL = "http://localhost:8000/Lokahi/login" #need url

        URL = "http://lit-headland-35537.herokuapp.com/Lokahi/login" #need url
        session = requests.Session()
        session.get(URL)
        csrftoken = session.cookies['csrftoken']
        payload = {'username' : self.user, 'password' : password, 'next': 'validate.html','csrfmiddlewaretoken': csrftoken }
        response = session.post(URL, data=payload)
        #print(response.text)
        if(response.text == "success"):
            self.show_mainPage()
        else:
            messagebox.showinfo("Login Failed", "Login Failed")


    def show_mainPage(self):
        self.login_page.pack_forget()
        self.encrypt_file_page.forget()
        self.reports_page.pack_forget()
        self.docs_page.pack_forget()
        self.first_page.pack()
        self.canvas.destroy()
        self.scrollbar.destroy()

    def show_loginPage(self):
        #self.root.blind("<Return>", self.login)
        self.login_page.pack()
        self.root.mainloop()

    def show_encryptPage(self):
        print("open encrypt page")
        self.login_page.pack_forget()
        self.first_page.pack_forget()
        self.reports_page.pack_forget()
        self.encrypt_file_page.pack()


    def show_reportsPage(self):
        self.login_page.pack_forget()
        self.first_page.pack_forget()
        self.encrypt_file_page.pack_forget()
        self.reports_page.pack()

        self.canvas = Canvas(self.reports_page, bd=1,scrollregion=(0,0,1000,1000))
        self.scrollbar = Scrollbar(self.reports_page, orient=VERTICAL, command=self.canvas.yview)
        self.canvas.config(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.canvas.pack(expand=YES, fill=BOTH)




        reports = self.getReports()

        x = 0
        y = 0

        if reports.__len__() == 0:
            print("No reports")
        for report in reports:


            row = 0

            self.reportsframe = Frame(highlightbackground="black", highlightcolor="black", highlightthickness=1, width=100, height=100,bd= 0)

            self.canvas.create_window(0, y, anchor=NW, window=self.reportsframe)
            y = y+120

            report_title = Label(self.reportsframe, text="Report Title: " + report[2])  #report title index
            report_date = Label(self.reportsframe, text="Date: " + report[1]) #date index
            reports_desc = Label(self.reportsframe, text="Company: " + report[4])  #decription index
            repport_owner = Label(self.reportsframe, text="Owner: " + report[8])  #owner index
            view_docs_butt = Button(self.reportsframe, text='View Documents', command=partial(self.show_docsPage, report))

            report_title.grid(row=row)
            row += 1
            report_date.grid(row=row)
            row += 1
            reports_desc.grid(row=row)
            row += 1
            repport_owner.grid(row=row)
            row += 1
            view_docs_butt.grid(row=row)
            row += 1





    def encryptFile(self):

        filename = self.fileEntry.get()
        key_entry = self.key_entry.get()
        pubkey = key_entry.encode('utf-8')
        key = hashlib.sha256(pubkey).digest()
        obj = ARC4.new(key)

        try:
            with open(filename, 'rb') as in_file:
                with open(filename + ".enc", 'wb') as out_file:
                    while True:
                        chunk = in_file.read(8192)
                        if len(chunk) == 0:
                            break
                        out_file.write(obj.encrypt(chunk))
            messagebox.showinfo("File Encoded", "Encoded file saved to " + filename + ".enc")
            return True
        except FileNotFoundError:
            print("Wrong file or file path")
            return False


    def loadtemplate(self):

        filename = filedialog.askopenfilename(filetypes=(("Template files", "*.tplate")
                                                           , ("HTML files", "*.html;*.htm")
                                                           , ("All files", "*.*")))

        print(filename)
        self.fileEntry.insert(0,filename)

        return filename


    def download_file(self, doc):
        # url = 'http://localhost:8000/' + doc[4]  #name field
        url = 'http://lit-headland-35537.herokuapp.com/static/documents/' + doc[4]  #name field
        filename = url.split('/')[-1]
        u = urllib.request.urlopen(url)
        f = open(filename, 'wb')

        print(filename)

        block_sz = 8192

        while True:
            buffer = u.read(block_sz)
            if not buffer:
                break

            f.write(buffer)
        f.close()


        # filename = doc[4] #name field
        # response = urllib.request.urlopen(url)
        # data = response.read()
        # fw = open("downloads/" + filename, 'wb');
        # fw.write(data);

        if(doc[1]):  #is encoded field
                pubkey = doc[2] #public key field
                key = hashlib.sha256(pubkey.encode('utf-8')).digest()
                out = filename.replace(".enc", "")
                obj = ARC4.new(key)
                try:
                    with open(filename, 'rb') as in_file:
                        with open(out, 'wb') as out_file:
                            while True:
                                chunk = in_file.read(8192)
                                if len(chunk) == 0:
                                    break
                                out_file.write(obj.decrypt(chunk))
                    messagebox.showinfo("File Decrypted", out + "Downloaded and Decrypted")
                    return True

                except FileNotFoundError:
                    print("Wrong file or file path")
                    return False
        else:
            messagebox.showinfo("File Download", filename + " downloaded.")


    def getReports(self):
        global conn
        curs = conn.cursor()
        curs.execute("SELECT * FROM  report")  ##whatever we call reports
        reports = curs.fetchall()
        reportsList = []
        for report in reports:
            print(report[13])
            if (str(report[13]) == "None"):
                # What ever index public is
                reportsList.append(report)
        return (reportsList)

    def get_Docs(self, report):
        global conn
        curs = conn.cursor()
        curs.execute("SELECT * FROM file")  # whatever we call docs
        allfiles = curs.fetchall()
        files = []

        for file in allfiles:
            if (str(file[5]) == str(report[0])):  # if the doc is in report
                files.append(file)
        return files

    def show_docsPage(self, report):
        self.encrypt_file_page.pack_forget()
        self.docs_page.pack_forget()
        self.docs_page.destroy()
        self.docs_page = Frame(self.root, borderwidth = 2, highlightbackground = "black", highlightcolor = "blue", highlightthickness = 1, bd = 0)

        docs = self.get_Docs(report)
        row = 0
        self.doc_page_title = Label(self.docs_page, text="Documents from " + str(report[1]))  #name filed
        self.doc_page_title.grid(row=row)
        row += 1
        for doc in docs:
            doc_title = Label(self.docs_page, text="Title: " + str(doc[4]))  #doc title field
            download_button = Button(self.docs_page, text='Download', command=partial(self.download_file, doc))

            doc_title.grid(row=row, column=0)
            download_button.grid(row=row, column=1)
            row += 1

        #self.canvas.create_window(10, 300, anchor=NW, window=self.docs_page)
        self.docs_page.pack(side = BOTTOM)


page = Window()
page.show_loginPage()
