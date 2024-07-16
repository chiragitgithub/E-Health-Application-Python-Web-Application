from cgitb import text
from email.mime import image
from msilib.schema import Font
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
from tkinter.tix import IMAGE
from turtle import bgcolor
from xml.etree.ElementTree import tostring
import mysql.connector
from pymysql import ROWID
import os


def update(rows):
    trv.delete(*trv.get_children())
    for i in rows:
        trv.insert('', 'end', values=i)


def search():
    q2 = q.get()
    query = "SELECT * FROM data1 WHERE ID LIKE '%" + q2 + "%' OR HOSPITALNAME LIKE '%" + q2 + "%' OR TYEP LIKE '%" + q2 + "%' OR ADDRESS like '%" + q2 + "%' OR STATE LIKE '%" + q2 + "%' OR CITY LIKE '%" + q2 + "%'OR PINCODE LIKE '%" + q2 + "%'OR CONTACTNO LIKE '%" + q2 + "%'"
    cursor.execute(query)
    rows = cursor.fetchall()
    update(rows)


def clear():
    query = "select * from data1"
    cursor.execute(query)
    rows = cursor.fetchall()
    update(rows)


"""def getgrow(event):
    rowid=trv.identify_row(event.y)
    item=trv.item(trv.focus())
    t1.set(item['values'][0])
    t2.set(item['values'][1])
    t3.set(item['values'][2])
    t4.set(item['values'][3])
    t5.set(item['values'][4])"""

# def dex():
#    Hospital_Name=t1.get()


mydb = mysql.connector.connect(host="localhost", user="root", password="chirag123", database="hospitals",
                               auth_plugin="mysql_native_password")
cursor = mydb.cursor()
root = Tk()
q = StringVar()
"""t1=StringVar()
t2=StringVar()
t3=StringVar()
t4=StringVar()
t5=StringVar()"""

wrapper1 = LabelFrame(root, text="HOSPITALS", font=150, fg="dark blue", bg="light grey")
wrapper2 = LabelFrame(root, text="SEARCH", font=150, fg="navy blue", bg="light grey")
# wrapper3=LabelFrame(root, text="Data")

wrapper1.pack(fill="both", expand="yes", padx=20, pady=10)
wrapper2.pack(fill="both", expand="yes", padx=20, pady=10)
# wrapper3.pack(fill="both",expand="yes",padx=20,pady=10)

trv = ttk.Treeview(wrapper1, columns=(1, 2, 3, 4, 5, 6, 7, 8), show="headings", height="14")
trv.pack(side=LEFT)
trv.place(x=0, y=0)

trv.heading(1, text="ID")
trv.heading(2, text="HOSPITAL NAME")
trv.heading(3, text="TYPE")
trv.heading(4, text="ADDRESS")
trv.heading(5, text="STATE")
trv.heading(6, text="CITY")
trv.heading(7, text="PINCODE")
trv.heading(8, text="CONTACT NUMBER")
trv.column(1, width=20)
trv.column(2, width=350)
trv.column(3, width=150)
trv.column(4, width=300)
trv.column(5, width=100)
trv.column(6, width=80)
trv.column(7, width=60)
trv.column(8, width=170)

yscrollbar = ttk.Scrollbar(wrapper1, orient="vertical", command=trv.yview)
yscrollbar.pack(side=RIGHT, fill="y")
# xscrollbar=ttk.Scrollbar(wrapper1, orient="horizontal", command=trv.xview)
# xscrollbar.pack(side=BOTTOM, fill="x")

# trv.tag_configure("even",yscrollcommand=yscrollbar.set)

query = "Select * from data1"
cursor.execute(query)
rows = cursor.fetchall()
update(rows)

# search feature
lbl = Label(wrapper2, text="Search", font=25)
lbl.pack(side=tk.LEFT, padx=10)
ent = Entry(wrapper2, textvariable=q)
ent.pack(side=tk.LEFT, padx=6)
btn = Button(wrapper2, text="Search", command=search, font=25, bg="light grey")
btn.pack(side=tk.LEFT, padx=6)
btn1 = Button(wrapper2, text="Clear", command=clear, font=25, bg="light grey")
btn1.pack(side=tk.LEFT, padx=6)
btn2 = Button(wrapper2, text="Exit", command=exit, font=25, bg="light grey")
btn2.pack(side=tk.LEFT, padx=6)



# data section
"""lbl1=Label(wrapper3, text="Hospital_Name")
lbl1.grid(row=0, column=0, padx=5, pady=3)
ent1=Entry(wrapper3, textvariable=t1)
ent1.grid(row=0, column=1, padx=5, pady=3)

lbl2=Label(wrapper3, text="Type")
lbl2.grid(row=1, column=0, padx=5, pady=3)
ent2=Entry(wrapper3, textvariable=t2)
ent2.grid(row=1, column=1, padx=5, pady=3)

lbl3=Label(wrapper3, text="Disease")
lbl3.grid(row=2, column=0, padx=5, pady=3)
ent3=Entry(wrapper3, textvariable=t3)
ent3.grid(row=2, column=1, padx=5, pady=3)

lbl4=Label(wrapper3, text="Pincode")
lbl4.grid(row=3, column=0, padx=5, pady=3)
ent4=Entry(wrapper3, textvariable=t4)
ent4.grid(row=3, column=1, padx=5, pady=3)

lbl5=Label(wrapper3, text="Email")
lbl5.grid(row=4, column=0, padx=5, pady=3)
ent5=Entry(wrapper3, textvariable=t5)
ent5.grid(row=4, column=1, padx=5, pady=3)"""""
def exit(self):
    root.destroy()



root.title("E-Health Appliaction")
root.geometry("1550x700")
root.config(background="light blue")
root.mainloop()