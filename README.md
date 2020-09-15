# Frecuencia-Cardiaca-Maxima
Modelado de una ecuación de estimación de la FCmax

# Biomechanics e Inteligencia Artificial   
# Crear modelo FCmax y frecuencia cardiaca en reposo
*Buap, México. Facultad de Cultura Física*
*Enrique Ricardo Pablo Buendia Lozada <buendiaenr1@gmail.com>*

## BIOMECHANICSHR.PY      Control Cardio       [Biomecánica Deportiva / Fisiología Deportiva]
Es una app para apyo a personas que son entrenadores, personas que prescriben actividades físicas, entre otras. 
**El objetivo** es tener una ecuación de regresión múltiple para calcular la Frecuencia Cardiaca Máxima *(FCM)* 
para grupos de personas o de una sola persona, segundo tener una ecuación de regresión múltiple que estima la
Frecuencia Cardiaca de Reposo *(FCR)* , todo de tal manera que se puedan usar las estimaciones personales para
la ecuación de *Karvonen* y conocer la intencidad de la carga en latidos por minuto *(lpm)*.

## Requisitos
Tener en la misma carpeta de la aplicacion los siguientes archivos CSV
- automaticoFCM
- automaticoFCR
- cortes
- esfuerzo26022019c
- reposo26022019c
- Install:

** import pandas as pd
** from pandas import DataFrame
** from sklearn import linear_model
** from sklearn.linear_model import LinearRegression
** import statsmodels.formula.api as sm
** import numpy as np
** import tkinter as tk
** from tkinter import ttk,RAISED
** from tkinter import Label,Button,Text,END,INSERT,Scrollbar,RIGHT,Y,DISABLED,messagebox
** import matplotlib
** from matplotlib import style
** matplotlib.use('TkAgg')
** from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
** from matplotlib.figure import Figure
** from matplotlib import pyplot as plt
** from sklearn.cluster import KMeans
** from sklearn import metrics
** from sklearn.model_selection import train_test_split

Estos archivos los consulta la app para construir las ecuaciones correspondientes.

## Crear ecuaciones automáticamente
Temas incluidos en https://www.udemy.com/course/machinelearning/ (Kirill Eremenko) antes de usar esta aplicación.
- Preparar la información para el análisis
- Regresión lineal múltiple
- Automatizar la selección de variables independientes Backward elimination and Call Ordinary Least Square

Por lo que puede ignorar las ecuaciones propuestas por esta aplicación y usar su nueva formula para trabajar
fuera de esta aplicación, por lo que esta aplicación tendría significado solo como didáctica en la educación.

## Gráfica mostrar puntos de corte
Los Clusters in Machine Learning se usaron para identificar los cúmulos de mediciones de FCR,
consultar https://revistadigital.inesem.es/biosanitario/pulsaciones/ (Julia pérez amigo 13/03/2017).
esto es una propuesta que el usuario puede modificar de acuerdo a sus necesidades, los colores de los clusters
identifican muy bien donde existen las regularidades de las mediciones (archivo reposo26022019.csv ), de acuerdo a 
https://revistadigital.inesem.es/biosanitario/pulsaciones/ (Julia pérez amigo 13/03/2017) deben estar a 40 - 60 lpm, y 
para el caso de de las FCM las ecuaciones mostradas en la tabla II de https://www.medigraphic.com/pdfs/cardio/h-2016/h164b.pdf 
(Javier Pereira-Rodríguez et all 2016) no corresponden con las mediciones de FCM de alumnos en diversos deportes
mostradas en el archivo esfuerzo26022019.csv (alumnos universitarios de edades 22.86-+2.4)

Temas incluidos en https://www.udemy.com/course/machinelearning/ (Kirill Eremenko) antes de usar esta aplicación.
- Preparar la información para el análisis
- Cluster

## Cambios de puntos de corte para FCR
De acuerdo con lo mostrado en el punto anterior aquí se pueden modificar los puntos de corte
para las ecuaciones propuestas con las variables mostradas, esto no se apliacrá directamente,
solo serán válidas hasta salir de la aplicación y volver a entrar.

## Formula de Karvonen
Usa las ecuaciones propuestas en el inicio de la app, debe ingresar los nuevos valores a estiar
para el caso específico, y finalmente la intensidad deseada por el usuario, todo esto se relaciona con
la información proporcionada por https://youtu.be/UzRZDDMoD_M 


