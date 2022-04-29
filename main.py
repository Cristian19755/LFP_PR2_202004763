import csv
from easygui import msgbox 

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
print(msgbox('ADIOS','ADIOS'))
exit()


            