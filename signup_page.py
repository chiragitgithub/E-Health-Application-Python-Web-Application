from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import pymysql, os
import os


import credentials as cr

class SignUp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sign Up")
        self.root.geometry("1280x800+0+0")
        self.root.config(bg = "white")

        self.bg_img = ImageTk.PhotoImage(file="Images/wallpaperbetter.jpg")
        background = Label(self.root,image=self.bg_img).place(x=0,y=0,relwidth=1,relheight=1)


        frame = Frame(self.root, bg="white")
        frame.place(x=350,y=100,width=500,height=550)

        title1 = Label(frame, text="Sign Up", font=("times new roman",25,"bold"),bg="white").place(x=20, y=10)
        title2 = Label(frame, text="Join with us", font=("times new roman",13),bg="white", fg="gray").place(x=20, y=50)

        f_name = Label(frame, text="First name", font=("helvetica",15,"bold"),bg="white").place(x=20, y=100)
        l_name = Label(frame, text="Last name", font=("helvetica",15,"bold"),bg="white").place(x=240, y=100)

        self.fname_txt = Entry(frame,font=("arial"))
        self.fname_txt.place(x=20, y=130, width=200)

        self.lname_txt = Entry(frame,font=("arial"))
        self.lname_txt.place(x=240, y=130, width=200)

        email = Label(frame, text="Email", font=("helvetica",15,"bold"),bg="white").place(x=20, y=180)

        self.email_txt = Entry(frame,font=("arial"))
        self.email_txt.place(x=20, y=210, width=420)

        sec_question = Label(frame, text="Security questions", font=("helvetica",15,"bold"),bg="white").place(x=20, y=260)
        answer = Label(frame, text="Answer", font=("helvetica",15,"bold"),bg="white").place(x=240, y=260)

        self.questions = ttk.Combobox(frame,font=("helvetica",13),state='readonly',justify=CENTER)
        self.questions['values'] = ("Select","What's your pet name?","Your first teacher name","Your birthplace", "Your favorite movie")
        self.questions.place(x=20,y=290,width=200)
        self.questions.current(0)

        self.answer_txt = Entry(frame,font=("arial"))
        self.answer_txt.place(x=240, y=290, width=200)

        password =  Label(frame, text="New password", font=("helvetica",15,"bold"),bg="white").place(x=20, y=340)

        self.password_txt = Entry(frame,font=("arial"))
        self.password_txt.place(x=20, y=370, width=420)

        self.terms = IntVar()
        terms_and_con = Checkbutton(frame,text="I Agree The Terms & Conditions",variable=self.terms,onvalue=1,offvalue=0,bg="white",font=("times new roman",12)).place(x=20,y=420)
        self.signup = Button(frame,text="Sign Up",command=self.signup_func,font=("times new roman",18, "bold"),bd=0,cursor="hand2",bg="green2",fg="white").place(x=120,y=460,width=250)
        self.loginbt1 = Button(frame, text="Login page", command=self.log1, font=("times new roman", 18, "bold"), bd=0,cursor="hand2", bg="green2", fg="white").place(x=120, y=510, width=250)
    def signup_func(self):
        if self.fname_txt.get()=="" or self.lname_txt.get()=="" or self.email_txt.get()=="" or self.questions.get()=="Select" or self.answer_txt.get()=="" or self.password_txt.get() == "":
            messagebox.showerror("Error!","Sorry!, All fields are required",parent=self.root)

        elif self.terms.get() == 0:
            messagebox.showerror("Error!","Please Agree with our Terms & Conditions",parent=self.root)

        else:
            try:
                connection = pymysql.connect(host="localhost", user="root", password="chirag123", database="hospitals")
                cur = connection.cursor()
                cur.execute("select * from user_register where email=%s",self.email_txt.get())
                row=cur.fetchone()

                # Check if th entered email id is already exists or not.
                if row!=None:
                    messagebox.showerror("Error!","The email id is already exists, please try again with another email id",parent=self.root)
                else:
                    cur.execute("insert into user_register (f_name,l_name,email,question,answer,password) values(%s,%s,%s,%s,%s,%s)",
                                    (
                                        self.fname_txt.get(),
                                        self.lname_txt.get(),
                                        self.email_txt.get(),
                                        self.questions.get(),
                                        self.answer_txt.get(),
                                        self.password_txt.get()
                                    ))
                    connection.commit()
                    connection.close()
                    messagebox.showinfo("Congratulations!","Register Successful",parent=self.root)
                    self.reset_fields()
            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.root)

    def reset_fields(self):
        self.fname_txt.delete(0, END)
        self.lname_txt.delete(0, END)
        self.email_txt.delete(0, END)
        self.questions.current(0)
        self.answer_txt.delete(0, END)
        self.password_txt.delete(0, END)

    def log1(self):
        self.root.destroy()
        os.system("login_page.py")


if __name__ == "__main__":
    root = Tk()
    obj = SignUp(root)
    root.mainloop()
