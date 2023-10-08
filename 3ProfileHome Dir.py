from tkinter import *
from unidecode import *
from openpyxl import *
import os

class taouser:
    
    def __init__(self,root):
        self.root = root
        self.root.geometry("550x400+700+100")
        self.root.config(bg="#fff")
        self.root.title("Đổi mật khẩu")
    
    def focus1(event):
        acc_field.focus_set()
        
    def focus2(event):
        ip_field.focus_set()
    
    def focus3(event):
        ou_field.focus_set()
        
    def focus4(event):
        dm1_field.focus_set()   
        
    def focus5(event):
        namefd_field.focus_set()  
        
def createProfileAndHomeDir(account,nameFolder, ou, domain,ip_server):
    cmdMkdir = f'mkdir C:\\{nameFolder}'
    os.system(cmdMkdir)
    cmdshare = f'net share {nameFolder}= C:\\{nameFolder}'
    print(cmdshare)
    os.system(cmdshare)
    path_profile = f'-profile \\{ip_server}\\profiles\\{account}'
    command2 = f'dsmod user "CN={account},OU={ou},OU=QTM_CTY,dc={domain},dc=com" {path_profile}'
    print(command2)
    os.system(command2)
def executed():
        account = acc_field.get()
        ip = ip_field.get()
        ou =ou_field.get()
        domain =dm1_field.get()
        namefd = namefd_field.get()
        path_profile = f'-profile \\{ip}\\profiles\\{account}'
        command2 = f'dsmod user "CN={account},OU={ou},OU=QTM_CTY,dc={domain},dc=com" {path_profile}'
        if account and namefd and ou and domain and ip:
            createProfileAndHomeDir(account,ip,ou,domain,namefd)
            result_label.insert(0,command2)


if __name__ == "__main__":
    root = Tk()
    obj = taouser(root)
    
    heading_flame = Frame(root,width=400,height=300,bg="#fff",bd=5).place(x=80,y=30)
    heading = Label(heading_flame,text=" Hàm tạo Profile và Home Dir cho Một user .",font="arial 15 bold",fg="black").place(x=70,y=50)

    acc = Label(heading_flame,text="Nhập user: ",font="arial 11",bg="#fff",fg="black").place(x=50,y=110)
    ip = Label(heading_flame,text="Nhập ip server: ",font="arial 11",bg="#fff",fg="black").place(x=50,y=150)
    ou = Label(heading_flame,text="Nhập ou: ",font="arial 11",bg="#fff",fg="black").place(x=50,y=190)
    dm1 = Label(heading_flame,text="Nhập doman: ",font="arial 11",bg="#fff",fg="black").place(x=50,y=230)
    namefd = Label(heading_flame,text="Nhập tên Folder: ",font="arial 11",bg="#fff",fg="black").place(x=50,y=270)
    
    acc_field = Entry(root,width=35,bd=3)
    ip_field = Entry(root,width=35,bd=3)
    ou_field = Entry(root,width=35,bd=3)
    dm1_field = Entry(root,width=35,bd=3)
    namefd_field = Entry(root,width=35,bd=3)
    
    acc_field.bind("<Return>", taouser.focus1)
    ip_field.bind("<Return>", taouser.focus2)
    ou_field.bind("<Return>", taouser.focus3)
    dm1_field.bind("<Return>", taouser.focus4)
    namefd_field.bind("<Return>", taouser.focus5)
    
    acc_field.place(x=200,y=110)
    ip_field.place(x=200,y=150)
    ou_field.place(x=200,y=190)
    dm1_field.place(x=200,y=230)
    namefd_field.place(x=200,y=270)
    
    result_label = Entry(heading_flame,font="arial 11",bg='#fff',fg="black", text= "",width=55)
    result_label.place(x=50, y=350)
    
    kq = Button(root, text="Submit", fg="Black",bg="green", command=executed,width=12).place(x=250,y=310)
    
    
    
    root.mainloop()
    