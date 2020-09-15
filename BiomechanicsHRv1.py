# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 11:59:01 2019

@author: Enrique Buendia
"""

# 
import pandas as pd
from pandas import DataFrame
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
import statsmodels.formula.api as sm
import numpy as np
import tkinter as tk
from tkinter import ttk,RAISED
from tkinter import Label,Button,Text,END,INSERT,Scrollbar,RIGHT,Y,DISABLED,messagebox
import matplotlib
from matplotlib import style
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from sklearn import metrics
from sklearn.model_selection import train_test_split



LARGE_FONT= ("Verdana", 12)
Short_Font= ("Curier",7)


class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "BUAP Control Cardio      Enrique Buendia buendiaenr1@gmail.com")
                
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree, PageForth):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):
    

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        
        label = tk.Label(self, text="Ecuaciones de Estimación", font=LARGE_FONT,bg='azure')
        label.pack(pady=10,padx=10)

        ttk.Style().configure("TButton", padding=6, relief="flat",   background="#ccc")
       

        button = ttk.Button(self, text="Cambios de puntos de corte para FCR",
                            command=lambda: controller.show_frame(PageOne))
        button.pack()

        button2 = ttk.Button(self, text="Fórmula de Karvonen",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()

        button3 = ttk.Button(self, text="Gráfica mostrar puntos de corte",
                            command=lambda: controller.show_frame(PageThree))
        button3.pack()

        button4 = ttk.Button(self,text="Crear ecuaciones automáticamente",
                            command=lambda: controller.show_frame(PageForth))
        button4.pack()

        #FCM
        df = pd.read_csv(r"esfuerzo26022019c.csv")
        #print(df.head())
        # datos para FCM frecuencia cardiaca máxima
        Yr=[]
        Yr=df['fcm']
        Xr=df[['edad','peso','est']]
        # with sklearn FCM
        regr = linear_model.LinearRegression()
        regr.fit(Xr, Yr)
        print('FCM\nIntercept: \n', regr.intercept_)
        print('Coefficients: \n', regr.coef_)
        # with statsmodels
        #Xr = sm.add_constant(Xr) # adding a constant
        #model = sm.OLS(Yr, Xr).fit()
        #predictions = model.predict(X)

        # con SKLEARN
        X_train, X_test, y_train, y_test = train_test_split(Xr, Yr, test_size=0.2, random_state=0)
        regressor = LinearRegression()
        regressor.fit(X_train, y_train)
        y_pred = regressor.predict(X_test)
        cad2='Mean Absolute Error:'+str( metrics.mean_absolute_error(y_test, y_pred))
        cad3='Mean Squared Error:'+str(metrics.mean_squared_error(y_test, y_pred))
        cad4='Root Mean Squared Error:'+str(np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
        self.t =tk.Text(self, width=80, height=5)
        self.t.config(font=('courier',8,'normal'),bg='skyblue')
        #self.t.insert(INSERT,model.summary())
        self.t.insert(INSERT,'FCM\n'+cad2+'\n'+cad3+'\n'+cad4)
        self.t.pack()
       
        
        

        cad='FCM estimada :'
        label1 = tk.Label(self, text=cad, font=LARGE_FONT,bg='azure')
        label1.pack(pady=20,padx=10)
        cad = 'FCM='+str(float(regr.intercept_))+' + ('+str(regr.coef_[0])+' * edad)\n + ('+str(regr.coef_[1])+' * peso) + ('+str(regr.coef_[2])+' * estatura)'
        label1 = tk.Label(self, text=cad)
        label1.pack(pady=20,padx=10)

    
        #####******** FCR

        # alumnos Fcr = 63.90132 -peso*0.03835 +estatura*0.33048 -edad*0.08913- 
        # fcreposo1*0.01935 + 
        # fcreposo2*0.01005 - fcreposo3*0.03952 + fcreposo4*0.01659
        ddff=pd.read_csv(r"cortes.csv")
        corteinferior=ddff.iat[0,0]
        cortesuperior=ddff.iat[0,1]
        
        dff = pd.read_csv(r"reposo26022019c.csv")
        dfi=dff.loc[dff['fcr'] >= corteinferior] ## selecciona todos los de la lista
        df2=dfi.loc[dfi['fcr'] <= cortesuperior] ## selecciona todos los de la lista

        Y2=df2['fcr']
        X2=df2[['pesoa','estaturaa','edada','fcc1','fcc2','fcc3','fcc4']]

        # usando sklearn
        X_train, X_test, y_train, y_test = train_test_split(X2, Y2, test_size=0.2, random_state=0)
        regressor = LinearRegression()
        regressor.fit(X_train, y_train)
        y_pred = regressor.predict(X_test)
        cad2='Mean Absolute Error:'+str( metrics.mean_absolute_error(y_test, y_pred))
        cad3='Mean Squared Error:'+str(metrics.mean_squared_error(y_test, y_pred))
        cad4='Root Mean Squared Error:'+str(np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
        
        #model2 = sm.OLS(Y2, X2).fit()
        #predictions = model.predict(X)
        self.t =tk.Text(self, width=80, height=5)
        self.t.config(font=('courier',8,'normal'),bg='skyblue')
        self.t.insert(INSERT,'FCR\n'+cad2+'\n'+cad3+'\n'+cad4)
        self.t.pack()

        # with sklearn FCR
        regr2 = linear_model.LinearRegression()
        regr2.fit(X2,Y2)
        cad='FCR estimada :'
        label1 = tk.Label(self, text=cad, font=LARGE_FONT,bg='azure')
        label1.pack(pady=20,padx=10)
        cad = 'FCR='+str(float(regr2.intercept_))+' + ('+str(regr2.coef_[0])+' * peso)\n + ('+str(regr2.coef_[1])+' * estatura) + ('+str(regr2.coef_[2])+' * edad) + ('+str(regr2.coef_[3])+' * fcreposo1)\n + ('+str(regr2.coef_[4])+' * fcreposo2) + ('+str(regr2.coef_[5])+' * fcreposo3) + ('+str(regr2.coef_[6])+' * fcreposo4)'
        label1 = tk.Label(self, text=cad)
        label1.pack(pady=20,padx=10)

        ddff=pd.read_csv(r"cortes.csv")
        corteinferior= ddff.iat[0,0]
        cortesuperior= ddff.iat[0,1]


        #root=tk.Tk()
        #root.config(width=800,height=400)
        #root.wm_title('FCR Puntos de corte?')
        cad='FCR estimada\n Federaciòn Argentina de Cardiologìa cortes en 40 y 60\n Para personas bien entrenadas'
        # New_edad label and input box
        label3=Label(self,text=cad)
        label3.pack(pady=10,padx=10)
        cad='Corte inferior en '+str(corteinferior)+':'
        label2 = Label(self, text=cad)
        label2.pack()
        cad='Corte superior en '+str(cortesuperior)+':'
        label4 = Label(self, text=cad)
        label4.pack()
        
        entry=tk.IntVar()
        entry2=tk.IntVar()
        #sbmitbtn=Button(self,text='Leer nuevos datos de corte en  FCR')
        #sbmitbtn.pack()
        entry=ttk.Entry(self) # crea la cja de texto
        entry.insert(0,str(corteinferior))
        entry.config(state="disable")
        entry.pack()
        corteinferiornuevo=corteinferior
        
        
        entry2=ttk.Entry(self) # crea la cja de texto
        entry2.insert(0,str(cortesuperior))
        entry2.config(state="disable")
        entry2.pack()
        cortesuperiornuevo=cortesuperior
        

        dff = pd.read_csv(r"reposo26022019c.csv")
        dfi=dff.loc[dff['fcr'] >= corteinferiornuevo] ## selecciona todos los de la lista
        df2=dfi.loc[dfi['fcr'] <= cortesuperiornuevo] ## selecciona todos los de la lista

        Y2=df2['fcr']
        X2=df2[['pesoa','estaturaa','edada','fcc1','fcc2','fcc3','fcc4']]


        # with sklearn FCR
        regr2 = linear_model.LinearRegression()
        regr2.fit(X2,Y2)
        cad='FCR estimada [nuevos puntos de corte]:'
        label1 = tk.Label(self, text=cad, font=LARGE_FONT,bg='azure')
        label1.pack()
        cad = 'FCR='+str(float(regr2.intercept_))+' + ('+str(regr2.coef_[0])+' * peso)\n + ('+str(regr2.coef_[1])+' * estatura) + ('+str(regr2.coef_[2])+' * edad) + ('+str(regr2.coef_[3])+' * fcreposo1)\n + ('+str(regr2.coef_[4])+' * fcreposo2) + ('+str(regr2.coef_[5])+' * fcreposo3) + ('+str(regr2.coef_[6])+' * fcreposo4)'
        label1 = tk.Label(self, text=cad)
        label1.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def recalcular(entry,entry2):
            
            
            
            entry.config(state='normal')
            entry2.config(state='normal')

            try:
                corteinferiornuevo=int(entry.get())
                cortesuperiornuevo=int(entry2.get())
                if cortesuperiornuevo >=180 or corteinferiornuevo <= 0:
                    messagebox.showerror(message="Revisar parámetros ...",title="Error")
                    raise SystemExit
            except ValueError:
                messagebox.showerror(message="Falta o no es correcta la información ....", title="Error")
                raise SystemExit
            ### leer lo que hay y actualizar cortes
            ddff=pd.read_csv(r"cortes.csv")
            ddff.iat[0,0]=corteinferiornuevo
            ddff.iat[0,1]=cortesuperiornuevo
            ddff.to_csv('cortes.csv', sep=',', encoding='utf-8', index=False)

            corteinferior=corteinferiornuevo
            cortesuperior=cortesuperiornuevo

            #corteinferiornuevo=int(entry.get())
            #cortesuperiornuevo=int(entry2.get())
            dff = pd.read_csv(r"reposo26022019c.csv")
            dfi=dff.loc[dff['fcr'] >= corteinferior] ## selecciona todos los de la lista
            df2=dfi.loc[dfi['fcr'] <= cortesuperior] ## selecciona todos los de la lista

            Y2=df2['fcr']
            X2=df2[['pesoa','estaturaa','edada','fcc1','fcc2','fcc3','fcc4']]


            # with sklearn FCR
            regr2 = linear_model.LinearRegression()
            regr2.fit(X2,Y2)
            cad='FCR estimada [nuevos puntos de corte]:'
            label1 = tk.Label(self, text=cad, font=LARGE_FONT,bg='azure')
            label1.pack(pady=10,padx=10)
            cad = 'FCR='+str(float(regr2.intercept_))+' + ('+str(regr2.coef_[0])+' * peso)\n + ('+str(regr2.coef_[1])+' * estatura) + ('+str(regr2.coef_[2])+' * edad) + ('+str(regr2.coef_[3])+' * fcreposo1)\n + ('+str(regr2.coef_[4])+' * fcreposo2) + ('+str(regr2.coef_[5])+' * fcreposo3) + ('+str(regr2.coef_[6])+' * fcreposo4)'
            label1 = tk.Label(self, text=cad,bg='linen')
            label1.pack(pady=10,padx=10)
            # usando sklearn
            X_train, X_test, y_train, y_test = train_test_split(X2, Y2, test_size=0.2, random_state=0)
            regressor = LinearRegression()
            regressor.fit(X_train, y_train)
            y_pred = regressor.predict(X_test)
            cad='FCR estimada [nuevos puntos de corte] usando Machine Learning [SkLearn]:'
            label2 = tk.Label(self, text=cad, font=LARGE_FONT,bg='azure')
            label2.pack(pady=10,padx=10)
            cad = 'FCR='+str(float(regressor.intercept_))+' + ('+str(regressor.coef_[0])+' * peso)\n + ('+str(regressor.coef_[1])+' * estatura) + ('+str(regressor.coef_[2])+' * edad) + ('+str(regressor.coef_[3])+' * fcreposo1)\n + ('+str(regressor.coef_[4])+' * fcreposo2) + ('+str(regressor.coef_[5])+' * fcreposo3) + ('+str(regressor.coef_[6])+' * fcreposo4)'
            label2 = tk.Label(self, text=cad,bg='linen')
            label2.pack(pady=10,padx=10)

        
        #tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Cambio de puntos de corte para FCR", font=LARGE_FONT,bg='azure')
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Inicio",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Fórmula de Karvonen",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()


        #root=tk.Tk()
        #root.config(width=800,height=400)
        #root.wm_title('FCR Puntos de corte?')
        cad='FCR estimada\n Federaciòn Argentina de Cardiologìa cortes en 40 y 60\n Para personas bien entrenadas'
        # New_edad label and input box
        label3=Label(self,text=cad,bg='azure')
        label3.pack(pady=10,padx=10)
        label2 = Label(self, text='Corte inferior en 48: ')
        label2.pack()
        label4 = Label(self, text='Corte superior en 66: ')
        label4.pack()
        
        entry=tk.IntVar()
        entry2=tk.IntVar()
        
        sbmitbtn=ttk.Button(self,text='Leer nuevos datos de corte en  FCR', command=lambda: recalcular(entry,entry2))
        sbmitbtn.pack()
        entry=ttk.Entry(self) # crea la cja de texto
        entry.pack()
        
        
        entry2=ttk.Entry(self) # crea la cja de texto
        entry2.pack()



class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        def recalcular2(entry1,entry2,entry3,entry4,entry5,entry6,entry7,entry8):
            
            ## maxHR
            df = pd.read_csv(r"esfuerzo26022019c.csv")
            Yr=[]
            Yr=df['fcm']
            Xr=df[['edad','peso','est']]
            X_train, X_test, y_train, y_test = train_test_split(Xr, Yr, test_size=0.2, random_state=0)
            
            regr = linear_model.LinearRegression()
            regr.fit(Xr, Yr)
            cad = 'FCM='+str(float(regr.intercept_))+' + ('+str(regr.coef_[0])+' * edad)\n + ('+str(regr.coef_[1])+' * peso) + ('+str(regr.coef_[2])+' * estatura)'
            label1 = tk.Label(self, text=cad)
            label1.pack(pady=20,padx=10)

            ### leer lo que hay y actualizar cortes
            ddff=pd.read_csv(r"cortes.csv")
            corteinferior=ddff.iat[0,0]
            cortesuperior=ddff.iat[0,1]
            

            dff = pd.read_csv(r"reposo26022019c.csv")
            dfi=dff.loc[dff['fcr'] >= corteinferior] ## selecciona todos los de la lista
            df2=dfi.loc[dfi['fcr'] <= cortesuperior] ## selecciona todos los de la lista

            Y2=df2['fcr']
            X2=df2[['pesoa','estaturaa','edada','fcc1','fcc2','fcc3','fcc4']]


            # with sklearn FCR
            regr2 = linear_model.LinearRegression()
            regr2.fit(X2,Y2)
            
            cad = 'FCR='+str(float(regr2.intercept_))+' + ('+str(regr2.coef_[0])+' * peso)\n + ('+str(regr2.coef_[1])+' * estatura) + ('+str(regr2.coef_[2])+' * edad) + ('+str(regr2.coef_[3])+' * fcreposo1)\n + ('+str(regr2.coef_[4])+' * fcreposo2) + ('+str(regr2.coef_[5])+' * fcreposo3) + ('+str(regr2.coef_[6])+' * fcreposo4)'
            label1 = tk.Label(self, text=cad,bg='linen')
            label1.pack(pady=10,padx=10)
            # usando sklearn
            X_train, X_test, y_train, y_test = train_test_split(X2, Y2, test_size=0.2, random_state=0)
            regressor = LinearRegression()
            regressor.fit(X_train, y_train)
            #y_pred = regressor.predict(X_test)
            #print("X_test en predict : ",X_test)
            cad='FCR estimada [nuevos puntos de corte] usando Machine Learning [SkLearn]:'
            label2 = tk.Label(self, text=cad, font=LARGE_FONT,bg='azure')
            label2.pack(pady=10,padx=10)
            cad = 'FCR='+str(float(regressor.intercept_))+' + ('+str(regressor.coef_[0])+' * peso)\n + ('+str(regressor.coef_[1])+' * estatura) + ('+str(regressor.coef_[2])+' * edad) + ('+str(regressor.coef_[3])+' * fcreposo1)\n + ('+str(regressor.coef_[4])+' * fcreposo2) + ('+str(regressor.coef_[5])+' * fcreposo3) + ('+str(regressor.coef_[6])+' * fcreposo4)'
            label2 = tk.Label(self, text=cad,bg='linen')
            label2.pack(pady=10,padx=10)



            try:
                edad=float(entry1.get())
                peso=float(entry2.get())
                estatura=float(entry3.get())
                fcr1=float(entry4.get())
                fcr2=float(entry5.get())
                fcr3=float(entry6.get())
                fcr4=float(entry7.get())
                pinten=float(entry8.get())

                if edad <=0. or peso <=0. or estatura <=0. :
                    messagebox.showerror(message="Revisar parámetros ...",title="Error")
                    raise SystemExit
            except ValueError:
                messagebox.showerror(message="Falta o no es correcta la información ....", title="Error")
                raise SystemExit
            
            ##### Estimar FCM
            
            xnew1=[[edad,peso,estatura]]
            print("xnew1 :",xnew1)
            y_pred1=regr.predict(xnew1)
            print("X=%s, Estima=%s" % (xnew1[0], y_pred1[0]))
            cad5="FCM estimada"
            label2 = tk.Label(self,text=cad5,bg='wheat')
            label2.pack()
            label2 = tk.Label(self,text=str(y_pred1[0]),bg='wheat')
            label2.pack()

            ##### Estimar FCR

            xnew1=[[peso,estatura,edad,fcr1,fcr2,fcr3,fcr4]]
            print("xnew1 :",xnew1)
            y_pred2=regr2.predict(xnew1)
            print("X=%s, Estima=%s" % (xnew1[0], y_pred2[0]))
            cad5="FCR estimada"
            label2 = tk.Label(self,text=cad5,bg='wheat')
            label2.pack()
            label2 = tk.Label(self,text=str(y_pred2[0]),bg='wheat')
            label2.pack()


            ###### Karvonen
            Karvonen=(y_pred1[0]-y_pred2[0])*pinten/100+y_pred2[0]
            cad5="Karvonen [lpm]"
            label2 = tk.Label(self,text=cad5,bg='wheat')
            label2.pack()
            label2 = tk.Label(self,text=str(Karvonen),bg='wheat')
            label2.pack()

            kar1=(y_pred1[0]-y_pred2[0])*0.10+y_pred2[0]
            kar2=(y_pred1[0]-y_pred2[0])*0.20+y_pred2[0]
            kar3=(y_pred1[0]-y_pred2[0])*0.30+y_pred2[0]
            kar4=(y_pred1[0]-y_pred2[0])*0.40+y_pred2[0]
            kar5=(y_pred1[0]-y_pred2[0])*0.50+y_pred2[0]
            kar6=(y_pred1[0]-y_pred2[0])*0.60+y_pred2[0]
            kar7=(y_pred1[0]-y_pred2[0])*0.70+y_pred2[0]
            kar8=(y_pred1[0]-y_pred2[0])*0.80+y_pred2[0]
            kar9=(y_pred1[0]-y_pred2[0])*0.90+y_pred2[0]
            kar10=(y_pred1[0]-y_pred2[0])*1+y_pred2[0]

            cad5="Karvonen 10% "+str(kar1)+"\n"+"Karvonen 20% "+str(kar2)+"\n"+"Karvonen 30% "+str(kar3)+"\n"+"Karvonen 40% "+str(kar4)+"\n"+"Karvonen 50% "+str(kar5)+"\n"+"Karvonen 60% "+str(kar6)+"\n"+"Karvonen 70% "+str(kar7)+"\n"+"Karvonen 80% "+str(kar8)+"\n"+"Karvonen 90% "+str(kar9)+"\n"+"Karvonen 100% "+str(kar10)+"\n"

            messagebox.showinfo("Karvonen sumario ",cad5)



           



        label = tk.Label(self, text="Cálculo de la Intensidad de la Carga usando frecuencia cardiaca", font=LARGE_FONT,bg='azure')
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Inicio",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Leer y Estimar Frecuencia cardiaca para la intensidad deseada",
                            command=lambda: recalcular2(entry1,entry2,entry3,entry4,entry5,entry6,entry7,entry8))
        button2.pack()

        label1 = Label(self, text='De acuerdo a formula de Karvonen ',bg='azure')
        label1.pack()
        

        cad5="Edad [años]"
        label2 = tk.Label(self,text=cad5,bg='wheat')
        label2.pack()
        entry1=ttk.Entry(self) # crea la cja de texto
        entry1.pack()
        cad5="Peso [kg]"
        label2 = tk.Label(self,text=cad5,bg='wheat')
        label2.pack()
        entry2=ttk.Entry(self) # crea la cja de texto
        entry2.pack()
        cad5="Estatura [m]"
        label2 = tk.Label(self,text=cad5,bg='wheat')
        label2.pack()
        entry3=ttk.Entry(self) # crea la cja de texto
        entry3.pack()

        cad5="Frecuencia cardiaca en reposo 1 [Todas 10s en carótida *6, en hora fija, sentado]:"
        label2 = tk.Label(self,text=cad5,bg='lavender')
        label2.pack()
        entry4=ttk.Entry(self) # crea la cja de texto
        entry4.pack()
        cad5="Frecuencia cardiaca en reposo 2 [20 minutos después, 10s en carótida *6]:"
        label2 = tk.Label(self,text=cad5,bg='lavender')
        label2.pack()
        entry5=ttk.Entry(self) # crea la cja de texto
        entry5.pack()
        cad5="Frecuencia cardiaca en reposo 3 [20 minutos después, 10s en carótida *6]:"
        label2 = tk.Label(self,text=cad5,bg='lavender')
        label2.pack()
        entry6=ttk.Entry(self) # crea la cja de texto
        entry6.pack()
        cad5="Frecuencia cardiaca en reposo 4 [20 minutos después, 10s en carótida *6]:"
        label2 = tk.Label(self,text=cad5,bg='lavender')
        label2.pack()
        entry7=ttk.Entry(self) # crea la cja de texto
        entry7.pack()

        cad5="% de intencidad requerido :"
        label2 = tk.Label(self,text=cad5,bg='orange')
        label2.pack()
        entry8=ttk.Entry(self) # crea la cja de texto
        entry8.pack()





class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Puntos de Corte para FCR", font=LARGE_FONT,bg='azure')
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Inicio",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        f =Figure(figsize=(5,5), dpi=100)
        #a = f.add_subplot(111)
        a =f.add_subplot(111)
        #a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])

        #FCR Clusters separar la información a puntos de corte 48 - 66
        df2 = pd.read_csv(r"reposo26022019c.csv")
        # clusters de FCR
        
        
        y3 = pd.DataFrame(df2[['fcr']])
    

        ## cluster *************************************************
        
        #print(result)
        kmeans = KMeans(n_clusters=4,init='k-means++',random_state=0,max_iter=100).fit(y3)
        #print(kmeans.labels_)
        print(kmeans.cluster_centers_)
       

        ## ****************************************************************

        #a.plot(x,y3)
        
        #a.plot(y3,'o',markersize=2)
        
        y_kmeans=kmeans.fit_predict(y3)
        a.plot(kmeans.cluster_centers_[:, 0],'*', c='red')
        a.plot(y3[y_kmeans ==0],'o',c='red',label='Cluster 1',markersize=2)
        a.plot(y3[y_kmeans ==1],'o',c='magenta',label='Cluster 2',markersize=2)
        a.plot(y3[y_kmeans ==2],'o',c='green',label='Cluster 3',markersize=2)
        a.plot(y3[y_kmeans ==3],'o',c='orange',label='Cluster 4',markersize=2)

        ddff=pd.read_csv(r"cortes.csv")
        corteinferior=ddff.iat[0,0]
        cortesuperior=ddff.iat[0,1]

        a.axhline(corteinferior,color='g',linestyle =':',linewidth=1)
        a.axhline(cortesuperior,color='r',linestyle =':',linewidth=1)
        a.title.set_text('FCR >'+' Corte inf:'+str(corteinferior)+' Corte sup:'+str(cortesuperior))

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

class PageForth(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)   
        ### Condiciones
        ### 1> verificar que todas las variables sean cuantitativas
        ### 2> que todas las variables hayan pasado por el proceso de pre tratamiento de información y validación
        ### 3> la primera columna simpre es la variable dependiente
        
        def backwardElimination(x, SL,nn,y,ii):
            numVars = len(x[0])
            temp = np.zeros((nn,ii)).astype(int)
            for i in range(0, numVars):
                regressor_OLS = sm.OLS(y, x).fit()
                maxVar = max(regressor_OLS.pvalues)
                adjR_before = regressor_OLS.rsquared_adj.astype(float)
                if maxVar > SL:
                    for j in range(0, numVars - i):
                        if (regressor_OLS.pvalues[j].astype(float) == maxVar):
                            temp[:,j] = x[:, j]
                            x = np.delete(x, j, 1)
                            tmp_regressor = sm.OLS(y, x).fit()
                            adjR_after = tmp_regressor.rsquared_adj.astype(float)
                            if (adjR_before >= adjR_after):
                                x_rollback = np.hstack((x, temp[:,[0,j]]))
                                x_rollback = np.delete(x_rollback, j, 1)
                                #print (regressor_OLS.summary())
                                cad=str(regressor_OLS.summary())
                                label1 = tk.Label(self, text=cad, font=Short_Font,bg='azure')
                                label1.pack()
                                cad=str(regressor_OLS.params)+'\np_values:'+str(regressor_OLS.pvalues)
                                label1 = tk.Label(self, text=cad,font=Short_Font,bg='orange')
                                label1.pack()
                                return x_rollback
                            else:
                                continue
            regressor_OLS.summary()
            return x

        


        label = tk.Label(self, text="Automatizar", font=LARGE_FONT,bg='azure')
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Inicio",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()     
    
        df = pd.read_csv(r"automaticoFCM.csv")
        yy=df.iloc[0:,0]    ### automáticamente la primera columna será y
        xx=df.iloc[0:,1:]   ### automáticamente el resto de colunas serán las xs
        nn=len(yy)
        #print("yy ",yy)
        #print("xx ",xx)
        #X_train, X_test, y_train, y_test = train_test_split(xx, yy, test_size=0.2, random_state=0)
        #regressor = LinearRegression()
        #regressor.fit(X_train, y_train)
        #y_pred = regressor.predict(X_test)

        #cad2='Mean Absolute Error:'+str( metrics.mean_absolute_error(y_test, y_pred))
        #cad3='Mean Squared Error:'+str(metrics.mean_squared_error(y_test, y_pred))
        #cad4='Root Mean Squared Error:'+str(np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
        #self.t =tk.Text(self, width=80, height=5)
        #self.t.config(font=('courier',8,'normal'),bg='skyblue')
        ##self.t.insert(INSERT,model.summary())
        #self.t.insert(INSERT,'FCM\n'+cad2+'\n'+cad3+'\n'+cad4)
        #self.t.pack()
        cad5=str(list(df))
        #cad='FCM estimada :'
        #label1 = tk.Label(self, text=cad, font=LARGE_FONT,bg='azure')
        #label1.pack(pady=10,padx=10)
        #cad = 'Intersección: '+str(float(regressor.intercept_))+'\n\nCoeficientes : '+str(regressor.coef_)+'\n\nVariables del archivo CSV :'+cad5
        cad="Eliminación de las Variables menos importantes [Backward Elimination]\nArchivo AutomaticoFCM.csv     FCM: \nVariables iniciales : "+cad5
        label1 = tk.Label(self, text=cad)
        label1.pack(pady=10,padx=10)

        X = np.append(arr = np.ones((nn, 1)).astype(int), values = xx, axis = 1)
        SL = 0.05       # nivel de significancia
        varsindep=list(xx)
        nx=[]
        ii=0
        for i in varsindep:
            nx.append(ii)
            ii=ii+1
        
        #X_opt = X[:, [0, 1, 2, 3, 4, 5]]
        #print(">> \n",X_opt)
        X_opt = X[:, nx]
        #print(">> \n",X_opt)
        X_Modeled = backwardElimination(X_opt, SL,nn,yy,ii)
        #cad=str(X_Modeled)
        #label1 = tk.Label(self, text=cad, font=Short_Font,bg='azure')
        #label1.pack()

        df = pd.read_csv(r"automaticoFCR.csv")
        yy=df.iloc[0:,0]    ### automáticamente la primera columna será y
        xx=df.iloc[0:,1:]   ### automáticamente el resto de colunas serán las xs
        nn=len(yy)
        cad5=str(list(df))
        cad="Eliminación de las Variables menos importantes [Backward Elimination]\nArchivo AutomaticoFCR.csv     FCR: \nVariables iniciales : "+cad5
        label1 = tk.Label(self, text=cad)
        label1.pack(pady=10,padx=10)

        X = np.append(arr = np.ones((nn, 1)).astype(int), values = xx, axis = 1)
        ##SL = 0.05   
        varsindep=list(xx)
        nx=[]
        ii=0
        for i in varsindep:
            nx.append(ii)
            ii=ii+1
        
        #X_opt = X[:, [0, 1, 2, 3, 4, 5]]
        X_opt = X[:, nx]
        X_Modeled = backwardElimination(X_opt, SL,nn,yy,ii)






app = SeaofBTCapp()
app.mainloop()