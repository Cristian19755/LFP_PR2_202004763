import csv

def resultado(equipoA, equipoB, temporada):
    equipoA = equipoA.replace('"','')
    equipoB = equipoB.replace('"','')
    with open('LaLigaBot-LFP.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if equipoA == row['Equipo1'] and equipoB == row['Equipo2'] and temporada == row['Temporada']:
                x = row['Equipo1']+' ' +str(row['Goles1'])+' '+row['Equipo2']+ ' '+str(row['Goles2'])
                return x
            