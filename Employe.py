import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Combobox
import main

class Employ:
    global w, mainfram, e1, producthelper, mycurser,e2,e3,treev,toal
    category = []
    Employ={"junaid" : "kummil","kadakkal":"kollam"}

    def catogorycallbacks(self, input,):
        print("combobox updated to ", self.e1.get())
        self.e2.set("")

        # self.producthelper.place(y=120, x=130)
        self.list_Catogories("NAME",change=self.e1.get())
        self.e2["values"]=self.category
        #self.addtocart()

        return True

    def uplist(self, a):
        print("ssee")
        pass

    def __init__(self, addproduct, im, sch, mycurser,atc,rmv,clr,ext):
        global e1
        self.totalvl = 0

        self.mycurser = mycurser
        self.w = tk.Canvas(addproduct,
                      width=1000,
                      height=800, bg="white")
        self.w.create_image(0, 0, image=im, anchor="nw")
        # w.pack(padx=0,pady=0,fill="both")
        self.w.create_image(0, 0, image=im, anchor="nw")
        self.w.pack(fill='both', ipadx=600, ipady=800, expand=1)
        self.list_Catogories("CATEGORY",'')

        mainfram = tk.Frame(self.w, width=600, height=100, bg="white", highlightbackground='black', highlightthickness=1)
        mainfram.pack(side='left', anchor="nw", expand=1, fill="both", padx=30, pady=30)
        l3 = tk.Label(mainfram, text='BILLING SYSTEM', bg='white')
        l3.pack(side="top", anchor="n", pady=(50, 30))
        extbut=tk.Button(mainfram,image=ext,border=0)
        extbut.place(x=10,y=60,)
        extbut.bind('<Button-1>',self.exitt)

        l3.configure(font=("Helvetica", 20,))
        topfram = tk.Frame(mainfram, width=600, height=100, bg="white", highlightbackground='black',
                           highlightthickness=1)
        topfram.pack(side='top', expand=1, fill="x", padx=10, pady=(0, 3), ipady=(8))
       # bootm = tk.Frame(mainfram, width=300, height=20, bg="blue", highlightbackground='black',
          #               highlightthickness=1)
       #bootm.pack(side='bottom', anchor="nw", expand=1, fill="both", padx=(2, 2), pady=(13, 0))

        leftfram = tk.Frame(mainfram, width=300, height=800, bg="white", highlightbackground='black',
                            highlightthickness=1)
        leftfram.pack(side='left', expand=1, fill="both", padx=(10, 2), pady=(0, 10))

        rightfram = tk.Frame(mainfram, width=300, height=800, bg="white", highlightbackground='black',
                             highlightthickness=1)
        rightfram.pack(side='right', padx=(2, 10), expand=1, fill="x", pady=(0, 10),ipadx=350)
        # l3=tk.Label(, text='         NAME:', bg='white',anchor='nw',justify='left').pack(pady=200,fill='none')
        # e3=tk.Entry(framadd, border=1, fg="black", width='40', bg='white', )
        lines = tk.Canvas(leftfram, width=200,
                          height=200, bg="white")
        lines.pack(side="left", fill="both", expand=1)
        toplines = tk.Canvas(topfram, width=200,
                             height=200, bg="white")
        toplines.pack(side="left", fill="both", expand=1)

        toplines.create_line(76, 60, 300, 60)
        # lines.create_line(130, 180, 350, 180)
        # lines.create_line(130, 240, 350, 240)
        billlabel = tk.Label(toplines, text='Bill NO:', bg='white').pack(side='left', padx=(20, 10), pady=(20, 0))
        billno = tk.Entry(toplines, border=0, fg="black", width='38', bg='white', )
        billno.pack(side='left', anchor='nw', pady=(40, 0), padx=(0, 3), fill='none', expand=0)
        billbut = tk.Button(toplines, image=sch, text="Search", border=0, )

        billbut.pack(side='left', padx=(20, 10), pady=(20, 0))

        # e1 = tk.Entry(w, border=0, fg="black", width='40', bg='white', )
        # l2 = tk.Label(w, text='         PRICE:', bg='white').place(y=165, x=20)
        # e2 = tk.Entry(w, border=0, fg="black", width='40', bg='white', )
        # l3=tk.Label(framadd, text='         NAME:', bg='white',anchor='nw',justify='left').pack(pady=200,fill='none')
        # e3=tk.Entry(framadd, border=1, fg="black", width='40', bg='white', )
        # e1.place(y=100, x=130)
        # e2.place(y=160, x=130)

        l1 = tk.Label(lines, text='         Catogory:', bg='white').place(y=105, x=20)

        self.e1 = tk.ttk.Combobox(lines, textvariable=("e1"),
                             state='readonly', height='6',
                             justify='left', width=35, values=self.category)
        self.e1.bind("<<ComboboxSelected>>", self.catogorycallbacks)
        l2 = tk.Label(lines, text='         Products:', bg='white').place(y=165, x=20)
        self.e2 = tk.ttk.Combobox(lines, textvariable=("e2"),
                             state='readonly', height='6',
                             justify='left', width=35)
        l3 = tk.Label(lines, text='         Quantity:', bg='white').place(y=225, x=20)
        self.e3 = tk.ttk.Combobox(lines, textvariable=("e3"),
                             state='both', height='6',
                             justify='left', width=35)


        # reg=lines.register(self.on_field_change)
        # e1 = Combobox(lines,  values=["foo", "bar", "baz"])
        # e1.config(validate="key", validatecommand=(reg, '%P','%d', '%i', '%S'))
        # self.producthelper=tk.Listbox(lines,width=23)
        # self.producthelper.insert(1,"jaunaid")

        # addproduct.bind("<Down>",self.uplist)

        self.e1.place(y=100, x=130)
        self.e2.place(y=160, x=130)
        self.e3.place(y=220, x=130)
        atc = tk.Button(lines, image=atc, text="Search", border=0, )
        atc.bind('<Button>', self.addtocart)

        atc.pack(side='left', padx=(20, 10), pady=(180, 0))

        #clr = tk.Button(lines, image=rmv, text="Search", border=0, )

        #clr.pack(side='left', padx=(10, 10), pady=(180, 0))

        rmv = tk.Button(lines, image=rmv, text="Search", border=0, )
        rmv.bind('<Button-1>',self.delt)
        rmv.pack(side='left', padx=(10, 10), pady=(180, 0))
        clrr = tk.Button(lines, image=clr, text="Search", border=0, )
        clrr.bind('<Button-1>',self.clear)
        clrr.pack(side='left', padx=(10, 10), pady=(180, 0))
        rightcanvas=tk.Canvas(rightfram,width=200,
                          height=600, bg="white")
        rightcanvas.pack(side="left",expand=1,fill="both",ipady=600)
        heading= tk.Label(rightcanvas, font='Times',text='CYBARZ PRODUCTIONS PVT LTD', bg='white').pack(side='top',pady=(10,0))
        heading= tk.Label(rightcanvas,text='Kadkkal kollam kerala', bg='white').pack(side='top',pady=(2,0))
        heading= tk.Label(rightcanvas,text='No:8848542918', bg='white').pack(side='top',pady=(2,0))
        GSTNO= tk.Label(rightcanvas,text='GST No:8848542918456', bg='white')
        GSTNO.pack(side='top',pady=(2,0))
        name= tk.Label(rightcanvas,text='Name:', bg='white')
        name.place(x=80,y=120)
        #name.pack(side='left',anchor='nw',pady=(20,0),padx=(40,0),expand=0)
        relt= tk.Label(rightcanvas,)
        relt.pack(side='right',anchor='nw')

        phno= tk.Label(rightcanvas,text='Phone No:554567546786', bg='white')
        phno.place(in_=relt, relx=-1.0, x=-180,y=10, rely=0)
        #phno.pack(side='right',anchor='nw',pady=(10,2),padx=(0,40),ipady=0,ipadx=0)

        heading= tk.Label(rightcanvas,text='Date:12/12/2020', bg='white').place(x=0,y=20,in_=name, relx=0.0,  rely=0)
        heading= tk.Label(rightcanvas,text='Bill No:343564644', bg='white').place(in_=phno, relx=0.0, x=0,y=20, rely=0)
        prodct= tk.Label(rightcanvas,text='  Product Name', bg='white').place(in_=name, relx=0.0, x=19,y=75, rely=0)
        quantity= tk.Label(rightcanvas,text='Quantity', bg='white').place(in_=GSTNO, relx=0.0, x=30,y=70, rely=2.5)
        price= tk.Label(rightcanvas,text='Price', bg='white').place(in_=phno, relx=0.0, x=15,y=82, rely=0)
        bottombill = tk.Frame(rightcanvas, width=600, height=50, bg="white", highlightbackground='black',
                           highlightthickness=0)
        bottombill.pack(side='bottom', expand=1, fill="x", padx=(6,0), pady=(0, 0), ipady=(6))
        bottomcanvas=tk.Canvas(bottombill,width=300,
                          height=50, bg="white")
        bottomcanvas.pack(side='left',fill='x',expand=1, pady=(0))
        #bottomcanvas.create_line(0, 5, 6009, 5)
        bottomcanvas.create_line(0, 40, 6009, 40)

        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=1, bd=2, font=('Calibri', 11))
        rightcanvas.create_line(0, 180, 6009, 180)
        rightcanvas.create_line(0, 220, 6009, 220)
        self.toal= tk.Label(bottomcanvas,text='Total:200', bg='white')
        self.toal.pack(side='right',ipady=5,padx=(0,40))
        self.toal.configure(text='Total 0')
        self.treev = ttk.Treeview(rightcanvas, selectmode='browse',style="mystyle.Treeview")

        self.treev.pack(side='top', expand=1, fill='both',pady=(116,0),padx=(6,0) )
        #treev.configure(bd=0)
        # Constructing vertical scrollbar
        # with treeview
        verscrlbar = ttk.Scrollbar(rightcanvas,
                                   orient="vertical",
                                   command=self.treev.yview)

        # Calling pack method w.r.to verical
        # scrollbar
        verscrlbar.place(in_=self.treev, relx=0.0, x=1,y=82, rely=0)

        # Configuring treeview
        self.treev.configure(xscrollcommand=verscrlbar.set)
        self.treev.bind("<Button-1>", self.select)

        # Defining number of columns
        self.treev["columns"] = ("1", "2", "3")

        # Defining heading
        self.treev['show'] = 'headings'

        # Assigning the width and anchor to  the
        # respective columns
        self.treev.column("1", width=50, anchor='c')
        self.treev.column("2", width=50, anchor='c')
        self.treev.column("3", width=50, anchor='c')


        # Assigning the heading names to the
        # respective columns

        #treev.heading("1", text="NAME")
       # treev.heading("2", text="CATOGORY")
        #treev.heading("3", text="PRICE")

        # print(s)
        # print(self.a)

    def list_Catogories(self, value,change):
        self.category = []

        if(change==''):
            self.mycurser.execute("SELECT DISTINCT  " + value + " FROM Products ")

        else:
            self.mycurser.execute("SELECT DISTINCT  " + value + " FROM Products where CATEGORY = '"+change+"'" )
        print("SELECT DISTINCT  '" + value + "' FROM Products ")
        # print(self.mycurser)
        for temp in self.mycurser:
            t2 = ''
            # print(temp)
            print(list(temp))
            tem1 = str(list(temp))
            for i in tem1:
                if (i == '[' or i == ']' or i == "'"):
                    # print(i)
                    pass
                else:
                    print(i)
                    # @str.join(t2,i)
                    t2 = t2 + i
                    print(t2)

            list.append(self.category, t2)
            # print(str.__len__(temp))

            # list.append(self.category,temp)
#        self.addtocart()
        print(self.category)
        pass

    def addtocart(self,a):

        prdt = self.e2.get()
        cat = self.e1.get()

        quantity=int(self.e3.get())
        #prdt="apple"
        print(prdt+"here it id")
        #quantity=self.e3.get()
        self.mycurser.execute("select price from PRODUCTS where NAME='"+prdt+"' and CATEGORY='"+cat+"'")
        for i in self.mycurser:
            temp=""
            price=i
            price=str(list(i))
            for j in price:
                if(j=='[' or j==']'):
                    pass
                else:
                    temp=temp+j

        print(temp)
        price=float(temp)
        print(price)
        actprice=price*quantity
        self.treev.insert("", 'end', text="L1",
                     values=(prdt,quantity,actprice))

        self.totalvl= self.totalvl+actprice
        self.toal.configure(text='Total :'+str(self.totalvl))

    def clear(self,a):
        for i in self.treev.get_children():
            self.treev.delete(i)
            self.toal.configure(text='Total :0 ')
            self.totalvl=0.0
    def select(self,d):
        global item_text
        self.cordin=d
        self.item_text = self.treev.identify('item', d.x, d.y)
        self.treev.identify("item", d.x, d.y)
        self.item_text = self.treev.item(self.item_text, "values")
        pass

    def delt(self,a):

        if(self.item_text!=None):
            self.treev.delete(self.treev.identify("item", self.cordin.x, self.cordin.y))
            self.totalvl= self.totalvl-float(self.item_text[2])
            self.toal.configure(text='Total : '+  str(self.totalvl))




    def exitt(self,a):
        self.w.forget()
        return "1"
        main.began()
        pass
