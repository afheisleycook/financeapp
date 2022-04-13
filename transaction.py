import pydoc

import tkinter
import  sqlite3
from  transaction import User
from  tkinter import messagebox
import sqlalchemy
MAX_SIZE = "400","400"
User = {
    "username" : "",
    "password":"",
}
import sqlite3
CONFIG_DB = sqlite3.connect("venv//bank.db")
class Mainwindow(tkinter.Tk):

    def __init__(self):

        super().__init__()
        self.resizable(False,False)
        self.apptitle = tkinter.Label(self,text="MY finance")
        self.apptitle.grid(row=0,column=3,columnspan=1,sticky=tkinter.N)
        self.luser = tkinter.Label(self,text="username")
        self.luser.grid(row=1,column=1)
        self.txtuser = tkinter.Entry(self)
        self.txtuser.grid(row=1,column=2, rowspan=1)
        self.lpasswwrd = tkinter.Label(self, text="password")
        self.lpasswwrd.grid(row=2,column=1)
        self.txtpassword = tkinter.Entry(self)
        self.txtpassword.grid(row=2,column=2)
        self.btnLogin = tkinter.Button(self,text="login", background='blue', foreground="red", command=self.login)
        self.btnLogin.grid(row=3,column=2)
    def login(self):

        logged = False
        userdata = CONFIG_DB.cursor()
        verify = userdata.execute(f"select * from users").fetchone()
        print(verify)
        if verify[1]==self.txtuser.get() and verify[2] == self.txtpassword.get():
            logged=True
            User["username"] = verify[1]
            User["password"] = verify[2]
        else:
            logged=False
            messagebox.showerror(f"invalid login:", f" username {self.txtuser.get().lower()} password {self.txtpassword.get().lower()}")

        if logged:
            """
            shows the info
            """
            return  CurrentInfo()



"""
gives the rest of the windows
"""


class CurrentInfo(tkinter.Tk):
    def __init__(self):
        super(CurrentInfo, self).__init__()
        self.title("current info")
        self.geometry("100x400")
        self.resizable(False,False)
        self.amount = tkinter.StringVar()
        self.total = CONFIG_DB.cursor().execute("select PURCHASE_AMOUNT from PURCHASE ")
        self.lblusername = tkinter.Label(self, text=f"user:{User['username']}")
        self.lblusername.grid(row=1,column=3)
        self.txtamount = tkinter.Entry(self)
        self.txtamount.grid(row=2,column=3)
        self.currentamount = tkinter.Label(self,text=sum(self.total.fetchall()))
        self.currentamount.grid(row=2,column=4)

    def show(self):
        self.mainloop()





app = Mainwindow()
app.mainloop()
