from components import correosPandas
from components import mailingApp


var_columna1="Nombres"
var_columna2="Correo"

respDatos=correosPandas.mani_correos(var_columna1,var_columna2)
print(respDatos)

# Iteramos nuestro diccionario de correos
for key,val in respDatos.items():
    mailingApp(key,val)