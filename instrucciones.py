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

def goles(condicion, equipo, temporada):
    equipo = equipo.replace('"','')
    with open('LaLigaBot-LFP.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        Tgoles = 0
        if condicion == 'TOTAL':
            for row in reader:
                if equipo == row['Equipo1'] and temporada == row['Temporada']:
                    k = int(row['Goles1'])
                    Tgoles = Tgoles + k
                elif equipo == row['Equipo2'] and temporada == row['Temporada']:
                    k = int(row['Goles2'])
                    Tgoles = Tgoles + k
            return Tgoles
        elif condicion == 'LOCAL':
            for row in reader:
                if equipo == row['Equipo1'] and temporada == row['Temporada']:
                    k = int(row['Goles1'])
                    Tgoles = Tgoles + k
            return Tgoles
        elif condicion == 'VISITANTE':
            for row in reader:
                if equipo == row['Equipo2'] and temporada == row['Temporada']:
                    k = int(row['Goles2'])
                    Tgoles = Tgoles + k
            return Tgoles                