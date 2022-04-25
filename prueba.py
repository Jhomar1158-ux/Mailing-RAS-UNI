import correos_pandas
var_archivocsv=input("Nombre de tu archivo csv: ")+".csv"
var_columna1=input("Nombre de tu columna 1: ")
var_columna2=input("Nombre de tu columna 2: ")

resp_datos=correos_pandas.mani_correos(var_archivocsv,var_columna1,var_columna2)
#print(resp_datos)
correos_list=[]
nombres_list=[]
for key,val in resp_datos.items():
    correos_list.append(key)
    nombres_list.append(val)
    print(key,val)
    print(f"Estimado {val} con correo {key}, se le invita al evento magistral ")

# for key in resp_datos.keys():
#     correos_list.append(key)
#     #print(key)

print(correos_list)
print(nombres_list)

