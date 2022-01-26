  # -*- coding: utf-8 -*-
"""
Author: José Pablo Chaves
Fecha: 22-01-2022
Ejercicio de Clase 1 sobre Estructuras de datos
"""
"""
#1. Crear una lista con 5 nombres (str) 
#2. Crear una lista con 5 países (str)
#3. Lista con 5 edades (int)
#4. Lista con 5 salarios (float)
#5. Dictionary con llaves > name, country, age, salary 
# El dictinary debe almacenar las variables previas
#6. Importar el paquete pandas con su alias pd
#7. Convertir el dict a un DataFrame
"""
import pandas as pd
    
nombres = ['Caro','Pablo','Jose','Gaby','Valentina']
paises = ['Perú','Costa Rica','España','Portugal','Canadá']
edades = [38,35,64,60,1]
salarios = [100.5, 100.5, 200, 300, 10]

# Crear dictionary de listas
dict_info = {} #dict

dict_info["name"] = nombres
dict_info["country"] = paises
dict_info["age"] = edades
dict_info["salary"] = salarios

# creación del DataFrame
df = pd.DataFrame(dict_info)

print(type(dict_info), dict_info)
