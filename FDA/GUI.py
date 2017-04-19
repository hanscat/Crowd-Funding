
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from functools import partial
import Crypto

from Crypto.Cipher import ARC4
import hashlib
import urllib.request




#import psycopg2


global conn

conn = "test"

#conn = psycopg2.connect(dbname="test, user="postgres", password="secret")




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
        self.reports = Canvas(self.reports_page)
        scroll = Scrollbar(self.reports_page, orient=VERTICAL, command=self.reports.yview)
        scroll.pack(side='right', fill='y')
        self.reports.pack()
        self.reports.configure(yscrollcommand=scroll.set)
        self.reportsframe = Frame(self.reports)

        self.docs_page = Frame(self.root)



    def login(self, *args):
        print("Do login stuff")
        #do login stuff
        self.login_page.pack_forget()
        self.encrypt_file_page.forget()
        self.reports_page.pack_forget()
        self.first_page.pack()

        self.user = self.username_entry.get()
        password = self.password_entry.get()

        #send to login script

        #if (respose == True):
            #self.show_mainPage()
        #else:
            #print("Login failed try again")

    def show_mainPage(self):
        self.login_page.pack_forget()
        self.encrypt_file_page.forget()
        self.reports_page.pack_forget()
        self.first_page.pack()

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
        self.reportsframe.pack_forget()
        self.reports_page.pack()

        self.reportsframe.destroy()
        self.reportsframe = Frame(self.reports_page, borderwidth=4, bg="lightblue")
        self.reports.create_window(0, 0, window=self.reportsframe, anchor='w')

        reports = self.getReports()
        row = 0

        for report in reports:
            report_title = Label(self.reportsframe, text="Report Title: " + reports[1])  #report title index
            report_date = Label(self.reportsframe, text="Date: " + report[1].strftime('%m/%d/%Y')) #date index
            reports_desc = Label(self.reportsframe, text="Report Description: " + report[2])  #decription index
            repport_owner = Label(self.reportsframe, text="Owner: " + report[1 ])  #owner index
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


        print("open reports page")


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
        url = 'documents url' + doc[1]  #name field
        filename = doc[1] #name field
        response = urllib.request.urlopen(url)
        data = response.read()
        fw = open("downloads/" + filename, 'wb');
        fw.write(data);

        if(doc[2]):  #is encoded field
                pubkey = doc[3] #public key field
                key = hashlib.sha256(pubkey.encode('utf-8')).digest()
                out = "downloads/" + filename.replace(".enc", "")
                obj = ARC4.new(key)
                try:
                    with open("downloads/" + filename, 'rb') as in_file:
                        with open(out, 'wb') as out_file:
                            while True:
                                chunk = in_file.read(8192)
                                if len(chunk) == 0:
                                    break
                                out_file.write(obj.decrypt(chunk))
                    messagebox.showinfo("File Encoded", "Encoded file saved to downloads/" + filename)
                    return True

                except FileNotFoundError:
                    print("Wrong file or file path")
                    return False
        else:
            messagebox.showinfo("File Encoded", "Encoded file saved to downloads/" + filename )


    def getReports(self):
        global conn
        curs = conn.cursor()
        curs.execute("SELECT * FROM  report")  ##whatever we call reports
        reports = curs.fetchall()
        reportsList = []
        for report in reports:
            if (report[1] == True):  # What ever index public is
                reportsList.append(report)
        return (reportsList)

    def get_Docs(self, report):
        global conn
        curs = conn.cursor()
        curs.execute("SELECT * FROM doc")  # whatever we call docs
        documents = curs.fetchall()
        docs = []
        for doc in documents:
            if (doc[1] == report[0]):  # if the doc is in report
                docs.append(doc)
        return documents

    def show_docsPage(self, report):
        self.encrypt_file_page.pack_forget()
        self.docs_page.pack_forget()
        self.docs_page.destroy()
        self.docs_page = Frame(self.root, borderwidth = 2, bg= "blue")

        docs = self.get_Docs(report)
        row = 0
        self.doc_page_title = Label(self.docs_page, text="Documents from " + report[1])  #name filed
        self.doc_page_title.grid(row=row)
        row += 1
        for doc in docs:
            doc_title = Label(self.docs_page, text="Title: " + doc[1])  #doc title field
            download_button = Button(self.docs_page, text='Download', command=partial(self.download_file, doc))

            doc_title.grid(row=row, column=0)
            download_button.grid(row=row, column=1)
            row += 1

        self.docs_page.pack()


page = Window()
page.show_loginPage()
