# This is a sample Python script.


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os

import mysql.connector
import pymysql
import tkinter as tk
from tkinter import ttk, messagebox
import Employe
import Startui

def rounded_rect(canvas, x, y, w, h, c):
    canvas.create_arc(x, y, x + 2 * c, y + 2 * c, start=90, extent=90, style="arc")
    canvas.create_arc(x + w - 2 * c, y + h - 2 * c, x + w, y + h, start=270, extent=90, style="arc")
    canvas.create_arc(x + w - 2 * c, y, x + w, y + 2 * c, start=0, extent=90, style="arc")
    canvas.create_arc(x, y + h - 2 * c, x + 2 * c, y + h, start=180, extent=90, style="arc")
    canvas.create_line(x + c, y, x + w - c, y)
    canvas.create_line(x + c, y + h, x + w - c, y + h)
    canvas.create_line(x, y + c, x, y + h - c)
    canvas.create_line(x + w, y + c, x + w, y + h - c)


def createdb():
    print(mydb)
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE blling")
    mycursor.execute("SHOW DATABASES")
    for x in mycursor:
        print(x)
    mycursor.execute("USE  blling")
    # mycursor.execute("DELETE TABLE EMPLOYEE")
    print(mycursor.execute("CREATE TABLE products  ( NO INT PRIMARY KEY AUTO_INCREMENT ,NAME VARCHAR(50)  ,CATEGORY VARCHAR(50),  PRICE DOUBLE )"))

    #j = mycursor.execute("DESCRIBE  products")
    f = [0]
    k = 0
    for i in mycursor:
        print("www")
        # print(i)

        list.append(f, i)
        k = k + 1

    print(f)


def adminwin():
    for i in range(col):
        addproduct.grid_rowconfigure(i, weight=1)
        addproduct.grid_columnconfigure(i, weight=1)

    heigth = addproduct.winfo_height()
    width = addproduct.winfo_width()

    canvas_width = 800
    canvas_height = 400
    # img=tk.Image.open('bg.png')
    bg = tk.PhotoImage(file="bg.png")
    w = tk.Canvas(addproduct,
                  width=10000,
                  height=800, bg="white")
    # w.create_image(0, 0, image=bg,anchor="nw")
    # w.pack(padx=0,pady=0,fill="both")
    w.grid(column=0, row=0)
    # rounded_rect(w, 20, 20, 1000, 800, 10)

    # first=tk.Frame(w, width=1000, height=700, bg="white")
    # first.place(x=0,y=0)
    fram3 = tk.Frame(w, width=600, height=800, bg="black", )
    fram4 = tk.Frame(fram3, width=800, height=800, bg="white", )
    fram4.pack(padx=(1), pady=1, fill="x", anchor="nw")
    imgc = tk.PhotoImage(file="add.png")
    # fram1.place(x=0,y=0)
    fram3.pack(side='right', padx=(500, 8), pady=(100, 8), fill="x", anchor="nw")
    # add.pack(expand=1,fill='both',padx=2,pady=2)

    upat = tk.PhotoImage(file="update.png")

    # add.pack(side='left')
    # pk.pack_info()

    # outerfram = tk.Frame(w, width=800, height=800, bg="black", )
    # innerfram = tk.Frame(outerfram, width=800, height=800, bg="white", )

    # outerfram.pack(padx=(1), pady=1,anchor="nw")
    # innerfram.pack( padx=(10,8), pady=(100,8),anchor="nw")

    add = tk.Button(w, image=imgc, text="     VALIDATE     ", bg='white', fg="black", border=0, )
    add.place(x=200, y=250)

    update = tk.Button(w, text="     VALIDATE     ", fg="black", border=0, image=upat)
    update.place(x=200, y=300)
    upt = tk.PhotoImage(file="del.png")
    delete = tk.Button(w, text="     VALIDATE     ", fg="black", border=0, image=upt)
    delete.place(x=200, y=350)
    w.create_rectangle(150, 200, 400, 400, outline="black")
    number = tk.Entry(addproduct, text="enter value", border=1, width=25, font=('calibre', 10, 'normal'),
                      )
    number.place(x=200, y=220)
    # number.grid(column=0, row=0)

    # w.forget()

def dbupdate(a):
    global e, e1, e2
    print("dbupaat")
    t1 = e.get()
    t2 = e1.get()
    t3 = e2.get()

    if (t1 != '' and t2 != '' and t3 != ''):
        print("insrt1")
        # no=mycursor.execute("SELECT NO FROM items WHERE NO IN MAXVALUE ")
        print("update table products set NAME='"+t1+"',CATOGORY='"+t2+"',PRICE="+t3+" where NO =  "+ item_text[0] )

        mycursor.execute("update   products set NAME='"+str.upper(t1)+"',CATEGORY='"+str.upper(t2)+"',PRICE="+t3+" where NO = "+ item_text[0])
        mycursor.execute("SELECT * FROM products")
        print(mycursor)
        # records = mycursor.fetchall()
        for i in treev.get_children():
            treev.delete(i)
        for k in mycursor:
            # treev.delete()

            treev.insert("", 'end', text="L1",
                         values=k)

        mydb.commit()


def updated(a):
    addproduct.bind('<Return>', dbupdate)

    global e1, e2, e,framadd,bacg,bw
    fram.forget()
    framadd = tk.Frame(w, width=400, height=800, bg="white", highlightbackground='black', highlightthickness=1, )
    lines = tk.Canvas(framadd, width=50,
                      height=50, bg="white")
    lines.pack(side='left', fill='both', expand=1)
    framadd.pack(side='left', padx=(10, 2), pady=(100, 100), fill='both', expand=0, ipadx=30)
    # tk.Label(framadd,text='ADD ',bg='white').pack(side='top',expand=1,fill="both",ipadx=100)
    # framadd1 = tk.Frame(framadd, width=300, height=800, bg="white", highlightbackground='black', highlightthickness=1,)
    # framadd2 = tk.Frame(framadd, width=300, height=800, bg="white", highlightbackground='black', highlightthickness=1,)

    uptt = tk.Button(lines, image=upat, text="     VALIDATE     ", bg='white', fg="black", border=0, )
    uptt.place(y=210, x=190)
    uptt.bind('<Button-1>', dbupdate)
    bw = tk.Button(w, image=bacg, text="     VALIDATE     ", bg='white', fg="black", border=0, )
    bw.place(y=33, x=30)
    bw.bind('<Button-1>', backword)
    # framadd2.pack(side='left',   expand=1,)

    # framadd1.pack(side='left', pady=(1),  expand=1,)
    lines.create_line(130, 120, 350, 120)
    lines.create_line(130, 180, 350, 180)
    lines.create_line(130, 60, 350, 60)
    tk.Label(lines, text='         NAME:', bg='white').pack(side='left', anchor='nw', pady=(45, 0), fill='x', padx=20,
                                                              expand=0)
    # tk.Label(framadd,text='        PRIZE: ',bg='white').pack(side='top',anchor='nw',ipady=50)
    # tk.Label(framadd,text='CATOGORY: ',bg='white').pack(side='top',anchor='nw',pady=0)

    e= tk.Entry(lines, border=0, fg="black", width='40', bg='white', )
    e.pack(side='left', anchor='n', pady=(40, 0),padx=(20, 3), fill='none', expand=0)

    l1 = tk.Label(lines, text='         CATOGORY:', bg='white').place(y=105, x=20)
    e1 = tk.Entry(lines, border=0, fg="black", width='40', bg='white', )
    l2 = tk.Label(lines, text='         PRICE:', bg='white').place(y=165, x=20)
    e2 = tk.Entry(lines, border=0, fg="black", width='40', bg='white', )
    # l3=tk.Label(framadd, text='         NAME:', bg='white',anchor='nw',justify='left').pack(pady=200,fill='none')
    # e3=tk.Entry(framadd, border=1, fg="black", width='40', bg='white', )
    e1.place(y=100, x=130)
    e2.place(y=160, x=130)
    print(e1.get()+"this")


def backword(a):
    addproduct.bind('<Return>', cb)

    global framadd,bw
    framadd.forget()
    fram.forget()
    w.forget()
    adminmain()
    #fram.pack(side='left', padx=(30, 0), pady=200, fill='y', expand=0)
    bw.place_forget()


def adder(a):
    addproduct.bind('<Return>', insrt)

    global e1, e2, e,framadd,bacg,bw
    fram.forget()
    framadd = tk.Frame(w, width=400, height=800, bg="white", highlightbackground='black', highlightthickness=1, )
    lines = tk.Canvas(framadd, width=50,
                      height=50, bg="white")
    lines.pack(side='left',fill='both',expand=1)
    framadd.pack(side='left', padx=(10, 2), pady=(100, 100), fill='both', expand=0, ipadx=30)
    # tk.Label(framadd,text='ADD ',bg='white').pack(side='top',expand=1,fill="both",ipadx=100)
    # framadd1 = tk.Frame(framadd, width=300, height=800, bg="white", highlightbackground='black', highlightthickness=1,)
    # framadd2 = tk.Frame(framadd, width=300, height=800, bg="white", highlightbackground='black', highlightthickness=1,)
    lines.create_line(130, 120, 350, 120)
    lines.create_line(130, 180, 350, 180)
    lines.create_line(130, 60, 350,60)
    add = tk.Button(lines, image=imgc, text="     VALIDATE     ", bg='white', fg="black", border=0, )
    add.place(y=210, x=190)
    add.bind('<Button-1>', insrt)
    bw = tk.Button(w, image=bacg, text="     VALIDATE     ", bg='white', fg="black", border=0, )
    bw.place(y=33, x=30)
    bw.bind('<Button-1>', backword)
    # framadd2.pack(side='left',   expand=1,)

    # framadd1.pack(side='left', pady=(1),  expand=1,)

    tk.Label(lines, text='         NAME:', bg='white').pack(side='left', anchor='nw', pady=(45, 0), fill='x', padx=20,
                                                              expand=0)
    # tk.Label(framadd,text='        PRIZE: ',bg='white').pack(side='top',anchor='nw',ipady=50)
    # tk.Label(framadd,text='CATOGORY: ',bg='white').pack(side='top',anchor='nw',pady=0)

    e= tk.Entry(lines, border=0, fg="black", width='40', bg='white', )
    e.pack(side='left', anchor='n', pady=(40, 0),padx=(20, 3), fill='none', expand=0)

    l1 = tk.Label(lines, text='         CATOGORY:', bg='white').place(y=105, x=20)
    e1 = tk.Entry(lines, border=0, fg="black", width='40', bg='white', )
    l2 = tk.Label(lines, text='         PRICE:', bg='white').place(y=165, x=20)
    e2 = tk.Entry(lines, border=0, fg="black", width='40', bg='white', )
    # l3=tk.Label(framadd, text='         NAME:', bg='white',anchor='nw',justify='left').pack(pady=200,fill='none')
    # e3=tk.Entry(framadd, border=1, fg="black", width='40', bg='white', )
    e1.place(y=100, x=130)
    e2.place(y=160, x=130)
    print(e1.get()+"this")

    # e3.place(y=120, x=130)
    # e1.pack(padx=(0,10))

def insrt(a):
    global e, e1, e2
    print("insrt")
    t1=e.get()
    t2=e1.get()
    t3=e2.get()

    if (t1!='' and t2!='' and t3!=''):
        print("insrt1")
        # no=mycursor.execute("SELECT NO FROM items WHERE NO IN MAXVALUE ")
        print("INSERT INTO products (NAME ,CATEGORY,PRICE) VALUES (" + t1 + ", " + t2 + "," + t3 + ")")

        mycursor.execute("INSERT INTO products (NAME,CATEGORY,PRICE) VALUES (" + "'"+str.upper(t1)+"'" + ", " + "'"+str.upper(t2)+"'" + "," + t3+")")
        mycursor.execute("SELECT * FROM products")
        print(mycursor)
        #records = mycursor.fetchall()
        for i in treev.get_children():
            treev.delete(i)
        for k in mycursor:
            #treev.delete()
            
                
                treev.insert("", 'end', text="L1",
                             values=k)




        mydb.commit()

# Press the green button in the gutter to run the script.
def createalert(a):
    global alertwindow,acces
    try:
        if (item_text != None and acces==1):
            acces=0
            alertwindow = tk.Tk()
            alertwindow.title('Delete')
            alertwindow.geometry("350x150+500+350")
            tk.Label()
            alertwindow.protocol("WM_DELETE_WINDOW", on_closing)
            # createdb()
            tk.Label(alertwindow, text='Do you want to delete?', ).pack(side='left', anchor="nw", pady=(20, 0),
                                                                       padx=(15, 0), expand=0, fill="none")
            alertwindow.resizable(False, False)
            yes = tk.Button(alertwindow, text="     Yes     ", fg="black", border=1, bg="Red")
            yes.pack(side='right', padx=(5, 70), pady=(85, 0), anchor='nw')
            yes.bind('<Button-1>', dele)
            addproduct.bind('<Return>', dele)

            alertwindow.mainloop(0)

    except:
        print()




def listinert():
    global treev
    #mycursor.execute("describe products ")

    #mycursor.execute('delete from products')
    mycursor.execute("select * from products")
    records = mycursor.fetchall()
    print(records)
    #print( mycursor)
    for i in treev.get_children():
        treev.delete(i)
    for k in records:
        print(k[0])
        treev.insert("", 'end', text="L1",
                     values=k)


def select(d):
    global item_text

    item_text = treev.identify('item',d.x,d.y)
    treev.identify("item", d.x, d.y)
    item_text = treev.item(item_text, "values")



    print(item_text)



def dele(a):
    global alertwindow,item_text,acces
    print("deltes")
    mycursor.execute("delete  from products where No = "+item_text[0])
    mydb.commit()
    mycursor.execute("UPDATE products SET NO = NO-1 WHERE NO>"+item_text[0])
    mydb.commit()
    item_text = None
    mycursor.execute("ALTER TABLE products AUTO_INCREMENT = 1")
    mydb.commit()
    alertwindow.withdraw()
    acces=1
    addproduct.bind('<Return>', cb)

    listinert()

def on_closing():
    global acces

    acces=1
    alertwindow.destroy()

def cb(a):
    print("callbacsk")
def adminmain():
    global e1, e2, eme,framadd,treev,addproduct,w,fram,imgc,upt,upat,bacg

    # addproduct.grid_columnconfigure()
    w = tk.Canvas(addproduct,
                  width=1000,
                  height=800, bg="white")
    # w.create_image(0, 0, image=bg,anchor="nw")
    # w.pack(padx=0,pady=0,fill="both")
    w.pack(fill='both')


    imgc = tk.PhotoImage(file="add.png")
    upt = tk.PhotoImage(file="del.png")
    upat = tk.PhotoImage(file="update.png")
    bacg = tk.PhotoImage(file="bw.png")


    fram = tk.Frame(w, width=600, height=800, bg="white", highlightbackground='black', highlightthickness=1)
    fram.pack(side='left', padx=(30, 0), pady=200, fill='y', expand=0)
    framright = tk.Frame(w, width=600, height=800, bg="white", highlightbackground='black', highlightthickness=0)
    framright.pack(side='right', padx=(20, 7), fill='both', expand=1, pady=(100, 20), ipadx=200, ipady=800)
    add = tk.Button(fram, image=imgc, text="     VALIDATE     ", bg='white', fg="black", border=0, )
    add.pack(padx=5, pady=(90, 10))
    update = tk.Button(fram, text="     VALIDATE     ", fg="black", border=0, image=upat)
    update.pack(padx=5, pady=(6, 10))
    delete = tk.Button(fram, text="     VALIDATE     ", fg="black", border=0, image=upt)
    delete.pack(padx=5, pady=(6, 0))
    add.bind('<Button-1>', adder)
    w.create_line(0, 50, 10000, 50, )
    tk.Label(w, text='ADD PRODUCTS', bg='white').pack(side='top', pady=40, expand=0, fill="none")
    extbut = tk.Button(w, image=ext, border=0)
    extbut.place(x=30, y=40, )
    extbut.bind('<Button-1>', exitt)

    delete.bind('<Button-1>', createalert)
    update.bind('<Button-1>', updated)

    treev = ttk.Treeview(framright, selectmode='browse')
    treev.pack(side='right', expand=1, fill='both', )

    # Constructing vertical scrollbar
    # with treeview
    verscrlbar = ttk.Scrollbar(framright,
                               orient="vertical",
                               command=treev.yview)

    # Calling pack method w.r.to verical
    # scrollbar
    verscrlbar.pack(side='left', fill='y', )

    # Configuring treeview
    treev.configure(xscrollcommand=verscrlbar.set)

    # Defining number of columns
    treev["columns"] = ("1", "2", "3", "4")

    # Defining heading
    treev['show'] = 'headings'

    # Assigning the width and anchor to  the
    # respective columns
    treev.column("1", width=50, anchor='c')
    treev.column("2", width=50, anchor='c')
    treev.column("3", width=50, anchor='c')
    treev.column("4", width=50, anchor='c')

    # Assigning the heading names to the
    # respective columns
    treev.heading("1", text="NO")
    treev.heading("2", text="NAME")
    treev.heading("3", text="CATOGORY")
    treev.heading("4", text="PRICE")



    # Inserting the items and their features to the
    # columns built

    listinert()
    #item_text = treev.selection()
    treev.bind("<Button-1>", select)

    # adder()

def exitt(a):
    w.forget()
    began()

def employee_ui():
    pass
    #lbox =tk.Listbox(lines, width=25, height=15)


def cll():
    pass

def calladmin(a):
    global w
    w.forget()
    adminmain()
    pass

def callemp(a):
    global w
    w.forget()
    jump=Employe.Employ(addproduct,im,sch,mycursor,atc,rmv,clr,ext,)
    began()

    #print(jump+"junaid")

def began():
    global addproduct,w
    w = tk.Canvas(addproduct,
                       width=1000,
                       height=800, bg="white")
    w.create_image(0, 0, image=im, anchor="nw")
    # w.pack(padx=0,pady=0,fill="both")

    w.pack(fill='both', ipadx=600, ipady=800, expand=1)
    mainfram = tk.Frame(w, width=600, height=100, bg="white", highlightbackground='black', highlightthickness=1)
    mainfram.pack(side='left', anchor="nw", expand=1, fill="both", padx=30, pady=30)
    maincanvas = tk.Canvas(mainfram, width=1000,
                           height=800, bg="white")
    maincanvas.create_image(0, 0, image=bg1, anchor="nw")
    maincanvas.pack(fill='both', ipadx=600, ipady=800, expand=1)
    adm = tk.Button(maincanvas, image=asset, border=0, bg='white')
    adm.pack(side='left', padx=(250, 0), expand=1)
    adm.bind('<Button-1>', calladmin)
    empl = tk.Button(maincanvas, image=emp, border=0, bg='white')
    empl.pack(side='right', padx=(0, 250), expand=1)
    empl.bind('<Button-1>',callemp)

if __name__ == '__main__':
    global item_text,bacg,framadd,bw,alertwindow,acces,w

    global e1, e2, eme,framadd,treev,addproduct,w,fram,imgc,upt,upat
    #db = pymysql.connect("localhost", "root", "", "testdb")
    acces=1
    # print_hi('PyCharm')
    print("hhh")
    mydb = pymysql.connect(

       "localhost",
        "junaid",
        "junaid@123",


    )

    #mydb.cursor(dictionary=True)
    #os.startfile("secret.txt", "print")
    mycursor = mydb.cursor()
    mycursor.execute("USE  blling")
    # mycursor.execute("DROP TABLE products;")
    #mycursor.execute("SELECT COUNT(NO)  FROM Products")
    mycursor.execute("ALTER TABLE products AUTO_INCREMENT=0")
    mydb.commit()
    records = mycursor.fetchall()
    print(records)
    # print( mycursor)
    nou=0
    for k in mycursor:
        print(k)
        nou=k[0]

    addproduct = tk.Tk()
    addproduct.title('googlemeat_cheater')
    addproduct.geometry("1000x700+10+20")
    addproduct.bind('<Return>', cb)
    im = tk.PhotoImage(file="bg.png")
    sch = tk.PhotoImage(file="scc.png")
    rmv = tk.PhotoImage(file="rmv.png")
    clr = tk.PhotoImage(file="clr.png")
    bg1=tk.PhotoImage(file='back.png')
    emp=tk.PhotoImage(file='emp.png')
    ext = tk.PhotoImage(file='ext.png')

    asset=tk.PhotoImage(file='Asset 2.png')



    atc=tk.PhotoImage(file="atc.png")
    #Startui.startui(addproduct,im,bg1,asset,emp)
    #Employe.Employ(addproduct,im,sch,mycursor,atc,rmv,clr)

    #Employe.Employ["junaid"]
    #createdb()
    col = 23
    #employee_ui()
    #adminmain()
    began()
    #createalert()
    addproduct.mainloop(0)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
