from encodings import utf_8
import pandas as pd

def mani_correos(columnas1,columna2):
    df=pd.read_csv("../data/directiva.csv",delimiter=';',encoding="unicode_escape")

    #Filtramos la columna con titulo 'correos'
    list_cor=df[columnas1]
    list_nom=df[columna2]
    datos={}
    for i in range(len(list_cor)):
        datos.update({list_nom[i]:list_cor[i]})

    return datos