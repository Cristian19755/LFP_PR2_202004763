from msilib.schema import Error
from tkinter import  RAISED,Button, Entry, Label, Menu, Menubutton, Text, Tk, filedialog,END
from easygui import msgbox
from analizadorLexico import AnalizadorLexico
from analizadorSintactico import AnalizadorSintactico
import webbrowser
from functools import partial
import csv 
class main:
    def __init__(self):
        self.texto = 'BOT: HOLA USUARIO!!!'
        self.geted = ''
        self.root = Tk()

    def add(self):
        self.geted = self.J.get()
        ToEr = AnalizadorLexico()
        ToEr.analizar(self.geted)
        Tokens = ToEr.listaTokens
        Errores = ToEr.listaErrores
        ToEr.imprimirTokens()
        ToEr.imprimirErrores()
        k = AnalizadorSintactico(Tokens)
        k.analizar()
        res = open('respuestas.txt','r')
        res = res.read()
        out = '\nBOT: ' + str(res)
        entry = self.texto + '\nUser: '+ self.geted + out
        F = Label(self.root, text=entry,bg='yellow', font=('Verdana',14), justify='left')
        F.grid(row=0,column=0)
        self.texto += '\nUser: '+ self.geted + out
        self.geted = ''
        
    def Fecha(x=str):
        with open('LaLigaBot-LFP.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['Fecha'] == x:
                    print(row['Fecha'])
    def Temporada(x=int):
        with open('LaLigaBot-LFP.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            contador = 0
            for row in reader:
                if x == contador:
                    print(row['Fecha'])
                    break
                else:
                    contador +=1
    def Jornada(x=int):
        with open('LaLigaBot-LFP.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            contador = 0
            for row in reader:
                if x == contador:
                    print(row['Fecha'])
                    break
                else:
                    contador +=1

    def interfaz(self):

        self.root.geometry('645x600')

        ##########################################################################
        C = Menubutton(self.root, text='REPORTES', relief=RAISED,  bg='blue', fg='white',height=3, width=15)
        C.grid(row=0, column=3, sticky='E')
        C.menu = Menu( C, tearoff = 0)
        C["menu"] =  C.menu

        C.menu.add_command(label='Reporte de Errores')
        C.menu.add_command(label='Limpiar log de Errores')
        C.menu.add_command(label='Reporte de Tokens')
        C.menu.add_command(label='Limpiar log de Tokens')
        C.menu.add_command(label='Manual Tecnico')
        C.menu.add_command(label='Manual de usuario')
        Label(self.root, text='                                                              ').grid(row=0,column=1)
        F = Label(self.root, text='Bot:   Hola Usuario!!!',bg='yellow', font=('Verdana',14))
        F.grid(row=0,column=0)

        ###########################################################################
        E = Button(self.root, text ='Enviar', command= self.add,  bg='blue', fg='white',height=3, width=15)
        E.grid(row=2, column=0)

        self.J = Entry(self.root, width=60)
        self.J.grid(row=1,column=0)


        self.root.mainloop()
M = main()
M.interfaz()
