from tkinter import *
from unidecode import *
from openpyxl import *

import os

class taouser:
    
    def __init__(self,root):
        self.root = root
        self.root.geometry("550x350+700+100")
        self.root.config(bg="#fff")
        self.root.title("Đổi mật khẩu")
    
    def focus1(event):
        acc_field.focus_set()
        
    def focus2(event):
        pw_field.focus_set()
    
    def focus3(event):
        ou_field.focus_set()
        
    def focus4(event):
        dm1_field.focus_set()   
    
def changePasswd(account, passwd, ou, domain):
    command = f'dsmod user "CN={account},ou={ou},OU=QTM_CTY,dc={domain},dc=.com" -pwd "{passwd}"'
    print(command)
    os.system(command)
def executed():
        account = acc_field.get()
        passwd = pw_field.get()
        ou =ou_field.get()
        domain =dm1_field.get()
        command = f'dsmod user "CN={account},ou={ou},OU=QTM_CTY,dc={domain},dc=.com" -pwd "{passwd}"'
        if account and passwd and ou and domain:
            changePasswd(account, passwd, ou, domain)
            result_label.insert(0,command)

if __name__ == "__main__":
    root = Tk()
    obj = taouser(root)
    
    heading_flame = Frame(root,width=400,height=300,bg="#fff",bd=5).place(x=80,y=30)
    heading = Label(heading_flame,text=" Hàm cập nhật mật khẩu của Một User.",font="arial 15 bold",fg="black").place(x=70,y=50)

    acc = Label(heading_flame,text="Nhập user: ",font="arial 11",bg="#fff",fg="black").place(x=50,y=110)
    pw = Label(heading_flame,text="Nhập password: ",font="arial 11",bg="#fff",fg="black").place(x=50,y=150)
    ou = Label(heading_flame,text="Nhập ou: ",font="arial 11",bg="#fff",fg="black").place(x=50,y=190)
    dm1 = Label(heading_flame,text="Nhập doman: ",font="arial 11",bg="#fff",fg="black").place(x=50,y=230)
    
    result_label = Entry(heading_flame,font="arial 11",bg='#fff',fg="black", text= "",width=55)
    result_label.place(x=50, y=310)
    
    acc_field = Entry(root,width=35,bd=3)
    pw_field = Entry(root,width=35,bd=3)
    ou_field = Entry(root,width=35,bd=3)
    dm1_field = Entry(root,width=35,bd=3)
    
    acc_field.bind("<Return>", taouser.focus2)
    pw_field.bind("<Return>", taouser.focus3)
    ou_field.bind("<Return>", taouser.focus4)
    dm1_field.bind("<Return>", taouser.focus4)
    
    acc_field.place(x=200,y=110)
    pw_field.place(x=200,y=150)
    ou_field.place(x=200,y=190)
    dm1_field.place(x=200,y=230)

    kq = Button(root, text="Submit", fg="Black",bg="green", command=lambda : executed(),width=12).place(x=250,y=270)
    
    
    root.mainloop()
    