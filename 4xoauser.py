import tkinter as tk
from unidecode import *
from openpyxl import *
from tkinter import *

import os

class taouser:
    
    def __init__(self,root):
        self.root = root
        self.root.geometry("550x400+700+100")
        self.root.config(bg="#fff")
        self.root.title("Tạo User")
    
    def focus1(event):
        ten_field.focus_set()
        
    
    def focus3(event):
        ou_field.focus_set()
        
    def focus4(event):
        dm1_field.focus_set()   
        
def delUser(account, ou, domain):
    command = f'dsrm user "CN={account},OU={ou},OU=QTM_CTY,{domain}"'
    print(command)
    os.system(command)
def executed():
        user = ten_field.get()
        ou =ou_field.get()
        domain =dm1_field.get()
        command = f'dsrm user "CN={user},OU={ou},OU=QTM_CTY,{domain}"'
        if user and ou and domain:
           delUser(user, ou, domain)
        result_label.insert(0,command)
if __name__ == "__main__":
    root = tk.Tk()
    obj = taouser(root)
    
    heading_flame = tk.Frame(root,width=400,height=300,bg="#fff",bd=5).place(x=80,y=30)
    heading = tk.Label(heading_flame,text=" Hàm xóa Một User trên hệ thống Domain Controller.",font="arial 14 bold",fg="black").place(x=50,y=50)
       
    ten = tk.Label(heading_flame,text="Nhập tên user: ",font="arial 11",bg="#fff",fg="black").place(x=50,y=110)
    ou = tk.Label(heading_flame,text="Nhập ou: ",font="arial 11",bg="#fff",fg="black").place(x=50,y=150)
    dm1 = tk.Label(heading_flame,text="Nhập doman: ",font="arial 11",bg="#fff",fg="black").place(x=50,y=190)
    
    result_label = tk.Entry(heading_flame,font="arial 11",bg='#fff',fg="black", text= "",width=55)
    result_label.place(x=50, y=270)
    
    ten_field = tk.Entry(root,width=35,bd=3)
    ou_field = tk.Entry(root,width=35,bd=3)
    dm1_field = tk.Entry(root,width=35,bd=3)
    
    ten_field.bind("<Return>", taouser.focus1)
    ou_field.bind("<Return>", taouser.focus3)
    dm1_field.bind("<Return>", taouser.focus4)
     
    ten_field.place(x=200,y=110)
    ou_field.place(x=200,y=150)
    dm1_field.place(x=200,y=190)

    kq = tk.Button(root, text="Submit", command= lambda: executed(), fg="Black",bg="green",width=12).place(x=210,y=230)
    
    root.mainloop()
     