import pandas as pd

class Ikaslea:
    def __init__(self, izena, adina, ikasgela, nota):
        self.izena = izena
        self.adina = adina
        self.ikasgela = ikasgela
        self.nota = nota

ikasleen_zerrenda = []

irakurrita = pd.read_csv("ikasleak.csv")
    
for fila in irakurrita.values:
    alumno = Ikaslea(fila[0], fila[1], fila[2], fila[3])
    ikasleen_zerrenda.append(alumno)

ikasleen_zerrenda.sort(key=lambda x: x.nota, reverse=True)

for ikasle in ikasleen_zerrenda:
    print(f"{ikasle.izena} - Nota: {ikasle.nota}")




