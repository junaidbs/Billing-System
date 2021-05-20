import tkinter as tk
import main
import Employe
class startui:

    def __init__(self,addproduct,im,bg1,asset,emp):
        self.addp=addproduct
        self.w = tk.Canvas(addproduct,
                      width=1000,
                      height=800, bg="white")
        self.w.create_image(0, 0, image=im, anchor="nw",)
        # w.pack(padx=0,pady=0,fill="both")

        self.w.pack(fill='both', ipadx=600, ipady=800, expand=1)
        mainfram = tk.Frame(self.w, width=600, height=100, bg="white", highlightbackground='black', highlightthickness=1)
        mainfram.pack(side='left', anchor="nw", expand=1, fill="both", padx=30, pady=30)
        maincanvas=tk.Canvas(mainfram, width=1000,
                      height=800, bg="white")
        maincanvas.create_image(0, 0, image=bg1, anchor="nw")
        maincanvas.pack(fill='both', ipadx=600, ipady=800, expand=1)
        adm=tk.Button(maincanvas,image=asset,border=0,bg='white')
        adm.pack(side='left',padx=(250,0),expand=1)
        adm.bind('<Button-1>',self.calladmin)
        empl=tk.Button(maincanvas,image=emp,border=0,bg='white')
        empl.pack(side='right',padx=(0,250),expand=1)


        pass
    def callemp(self):
        Employe.Employ()

        pass
    def calladmin(self,a):
        self.w.forget()
        main.adminmain(self.addp)
        pass
