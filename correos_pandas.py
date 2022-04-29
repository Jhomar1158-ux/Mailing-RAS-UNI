from encodings import utf_8
import pandas as pd

def mani_correos(columnas1,columna2):
    #Para csv con separadores ';'
    df=pd.read_csv("dataRas.csv",delimiter=';',encoding="unicode_escape")

    #Para archivos excel
    #df=pd.read_excel("correos.xlsx")

    #Filtramos la columna con titulo 'correos'
    list_cor=df[columnas1]
    list_nom=df[columna2]

    #Se puede usar como una lista de python
    #print(type(list_cor))
    #print(list_cor[0])

    datos={}

    #Recorremos todos los correos
    #print(dir(datos))
    for i in range(len(list_cor)):
        #print(list_nom[i],list_cor[i])
        datos.update({list_nom[i]:list_cor[i]})
    #print(datos)
    #print(list_cor)
    return datos