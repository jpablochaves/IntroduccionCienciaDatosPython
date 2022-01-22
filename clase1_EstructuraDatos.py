# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 10:20:01 2022

@author: Pablo
Clase 1 de Introducción a Análisis en Ciencia de Datos con Python

"""

## Operaciones de Aritmética Básica ##
## SUMA

print(2+2)

# Concatendand una función con { }
print(f'vamos a aplicar una suma de 2+2: es igual a : {2+2}')


print(f'vamos a aplicar una suma de 2+2: es igual a : {2+2}', 
      'Hola',sep = '\n')

## Resta
print(10-5)


## Multiplicación
print(20*5)


## Potencia
print(3**3)


## Division
print(10/2)


## Mod (residuo o resto de una división entera)
print(10 % 2)


## Variables y sus tipos de datos
var1 = 'Pablo' ## str puede ser '' o ""

# Conjunto de números
var2 = 20   # int
var3 = 40.1 # float
var4 = 2j   # compleja - complex

var5 = True # bool


## Consultar el tipo de dato
print(type(var1),
      type(var2),
      type(var3),
      type(var4),
      type(var5),
      sep = '\n')

## ------------------------------------------------------------
## Ejercicio de porcentajes - Calculo de Salario neto y bruto
## ------------------------------------------------------------
salario_mensual = 90000/12
ccss = (10.1/100) * salario_mensual
impuesto = (5/100) * salario_mensual
salario_neto = salario_mensual - ccss - impuesto

print(f'salario bruto mensual: {salario_mensual}',
      f'salario neto: {salario_neto}', sep = '\n')

## Eliminar variables
del var1

## Eliminar todas las variables creadas
#%reset

## -----------------------------
## ESTRUCTURAS DE DATOS BASICAS
## -----------------------------
## --------------------
## Listas [ ] ##
nombres = ['Esteban','Leonardo','José Pablo']  ## list

name_age =  ['Esteban', 20, 'Leonardo' , 30, 'José Pablo', 40] 

## OJO!!!
## Las listas son elementos mutables (modificar la estructura original) 

## Anexar o añadir un elemento a una lista (agregar al final)
nombres.append('Carlos')

name_age = name_age + ['Richard',50] ## univar varias listas

name_age.extend(['Carlos',60]) ## Añadir a una lista

name_age.insert(3,'Gustavo') ## agrega en posición específica (mueve el resto de elementos)


## Borrar Elementos de una lista 
name_age.remove('Gustavo')

## Obtener datos de una lista
print(name_age.index('Leonardo')) ## Buscar un elemento y extraer el index

print(name_age[2:6]) # El ultimo pos no es incluyente, osea el 6 no lo incluye

print(name_age[2:]) # extraer datos por índica

print(name_age[:6]) # extraer datos desde una posición hasta el final


## Crear copia de la lista

name = list(nombres)
print(name)

## Eliminar todos los elementos de una lista
nombres.clear()

copia1 = name_age
 # Si se hace la lista con list = list2  se hacen copias idénticas de la lista y son mutables ambas
name_age.clear()


# ---------------------------
## Lista de listas ##
lista1 = [['perro',10],
          ['gato',8],
          ['pez',0.01]]



## -----------------------------
## Tuplas ( ) ##
# similares a las listas pero no son mutables (una vez creada se queda tal cual)

tupla1 = (30,40,50,60,70) ## tuple
tupla2 = 'A','B','C'

len(tupla1) # usar funciones con las tuplas

print('A' in tupla2) # Consultar si un elemento está en tupla

# Si se desea modificar es mejor cambiar la tupla a lista

lista2 = list(tupla2) # Transformar la tupla a lista para ser modificada
lista2.append('D')

tupla2 = tuple(lista2)
# Las tuplas se usan mucho en algoritmos de Machine Learning



## --------------------------
## Diccionarios { } ##
## Esta es la gran usada en las páginas web y fuerte de python

cursos = {'python':97,'R':80,'SQL':85,'PBI':70,'MS Excel':100} # dict

cursos.keys()  # Consultar las llaves del dict

cursos['Azure'] = 75 ## agregando una llave - valor a mi dict

cursos['SQL']  # consultar un elemento (python es case sensitive)

# Eliminar una llave con sus valores
del cursos['R']


## Diccionarios de Diccionarios ##
estudiantes = {'Esteban':{'Cursos':['Power BI','MS Excel']},
               'Pablo':{'Cursos':['python','Machine Learning']},
               'Leonardo':{'Cursos':('Esp BI','Tableu')} }


## ----------------------------------------------------------
## DataFrames  | para esto necesitamos pandas  
## ----------------------------------------------------------
import pandas

df = pandas.DataFrame(estudiantes)  ## DataFrame

## Importación de paquetes ##
import os # paquete para trabajar con Sistema Operativo (permite trabajar con el directorio del Sistema Operativo)

from numpy import array # Importar modulos del paquete

import matplotlib.pyplot as plt # Importar submodulos de un paquete (este es de visualización)

import pandas as pb # Paquete para manipulacion de dataframes

import numpy as np # paquetes para trabajar matrices y vectores

import seaborn as sns # paquete para visualizaciones estadísticas


## Ejercicio de estructura de datos ##

#1. Crear una lista con 5 nombres (str) 
#2. Crear una litsa con 5 países (str)
#3. Lista con 5 edades (int)
#4. Lista con 5 salarios (float)
#5. Dictionary con llaves > name, country, age, salary 
# El dictinary debe almacenar las variables previas
#6. Importar el paquete pandas con su alias pd
#7. Convertir el dict a un DataFrame



















