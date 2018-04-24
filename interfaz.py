#Interfaz para el proyecto #1- Relaciones

from tkinter import *
import time
import tkinter.messagebox  ##para la ventana de decision
from tkinter import simpledialog as sdg
from turtle import *
import re #Sirve para que se extraigan solo los numeros de la cadena
from gcd import *
from tc import *
from inv  import *
	
	##Funcion Reloj
time1 =''
def reloj ():  ##Solo es un reloj de adorno
	global time1
	time2 = time.strftime ('%H:%M:%S')
	if time2 != time1:
		time1 = time2
		clock.configure (text=time2)
	clock.after(500,reloj)
	
	
##Funcion para el boton de salida
def salirPrograma():
	respuesta = tkinter.messagebox.askyesno("Saliendo del programa...","Esta seguro que desea salir del programa?")
	if(respuesta==True):
			ventanaPrincipal.quit()

	

##Funcion para  las ventanas
def mostrarVentana(ventana):
	try:
		ventana.deiconify()
		
	except ventana:
		ventana.deiconify()
		print("Abrio ventana")




"""Funcion para los tres programas"""		
def NoNumeroNegativos():
	tkinter.messagebox.showinfo(title= "Parece que hubo un problema :/", message= "Razon: No se permiten  numeros nagativos. Intentelo nuevamente. ")


	
##########################################################--------------------VENTANA "MCD" (programa1)--------------------------------##########################################################
def imprimirMCD(a,b,resultado):
	tkinter.messagebox.showinfo(title= "Parece que todo va bien! :)", message= "El MCD de "+str(a)+" y "+str(b)+" es: "+str(resultado)+"\n  gcd("+str(a)+","+str(b)+")"+"= "+str(resultado))
		

def numerosParaMCD():
	elemento1=  sdg.askinteger('Maximo Comun Divisor', '-*Escriba el primer numero ENTERO para obtener su MCD*-: ')
	elemento2 =  sdg.askinteger('Maximo Comun Divisor', '-*Escriba el segundo numero ENTERO para obtener su MCD*-: ')
	if((elemento1>= 0 and elemento2>=0) or (elemento1== 0 and elemento2>=0) or (elemento1>= 0 and elemento2==0)):
		if((elemento1== 0 and elemento2==0) or (elemento1== 0 and elemento2!=0) or (elemento1!= 0 and elemento2==0)):
			tkinter.messagebox.showinfo(title= "PARECE QUE ALGO NO VA BIEN! :/", message= "LOS NUMEROS DEBEN SER DIFERENTES DE CERO! :/. INTENTELO NUEVAMENTE :D")
		
		if((elemento1!= None and elemento2!=None) and (elemento1!= 0 and elemento2!=0)):
			resultado = funcionGCD(elemento1, elemento2)
			tkinter.messagebox.showinfo(title= "Muchas gracias!", message= "Los numeros fueron insertados con exito. Procesando...")
			imprimirMCD(elemento1,elemento2,resultado)
		elif((elemento1== None and elemento2==None) or (elemento1== None and elemento2!=None) or (elemento1!= None and elemento2==None)):
			tkinter.messagebox.showinfo(title= "Fallo! :)", message= "Al parecer omitió alguno de los numeros :/. HAGALO NUEVAMENTE :D")
	else:
		NoNumeroNegativos()

##########################################################--------------------VENTANA INVERSO UNICO (PROGRAMA 3)--------------------------------##########################################################

def inversoUnicoFunc():
	num=  sdg.askinteger('Inverso Unico', '-*Escriba el numero*-: ')
	mod =  sdg.askinteger('Inverso Unico', '-*Escriba el modulo*-: ')
	if((num>= 0 and mod>=0) or (num== 0 and mod>=0) or (num>= 0 and mod==0)):
		if((num== 0 and mod==0) or (num== 0 and mod!=0) or (num!= 0 and mod==0)):
			tkinter.messagebox.showinfo(title= "PARECE QUE ALGO NO VA BIEN! :/", message= "LOS NUMEROS DEBEN SER DIFERENTES DE CERO! :/. INTENTELO NUEVAMENTE :D")
		if((num!= None and mod!=None) and (num!= 0 and mod!=0)):
			invRes = inverso(num,mod)
			tkinter.messagebox.showinfo(title= "Muchas gracias!", message= "Los numeros fueron insertados con exito. Procesando...")
			tkinter.messagebox.showinfo(title= "Parece que todo va bien! :)", message= "El INVERSO UNICO del numero "+str(num)+" con modulo "+str(mod)+" es: "+str(invRes)+"\n  Inv("+str(num)+","+str(mod)+")"+"= "+str(invRes))
		elif((num== None and mod==None) or (num== None and mod!=None) or (num!= None and mod==None)):
			tkinter.messagebox.showinfo(title= "El algoritmo no pudo ejecutarse :(! :)", message= "Al parecer omitió alguno de los numeros :/. HAGALO NUEVAMENTE :D")
	else: 
		NoNumeroNegativos()
	


##########################################################--------------------CONFIG. PANTALLA PRINCIPAL--------------------------------##########################################################
##Configuracion pantalla
ventanaPrincipal=Tk()
ventanaPrincipal.title("PROYECTO #2. ")
ventanaPrincipal.attributes("-alpha", 0.87) #Esto sirve para transparentar ventanas
ventanaPrincipal.geometry("850x500+200+200")  ##Tamanio y la posicion donde va aparecer
ventanaPrincipal.config(bg='black')
imagenFondo = PhotoImage(file= "fond.png")
labelFondo = Label(ventanaPrincipal, image = imagenFondo).place(x=-300,y=-50)
ventanaPrincipal.maxsize(height=1400, width=800)
encabezado1 = Label(ventanaPrincipal, text = "BIENVENIDO AL PROYECTO #2.- ", font=('Consolas', 23), bg="black",  fg="yellow").place(x=60,y=400)
encabezado1 = Label(ventanaPrincipal, text = "Usted puede:", font=('arial', 14), bg="black",  fg="red").place(x=50,y=90)
botonInformacion=Button(ventanaPrincipal, text="Información \n del programa", bg = "green", fg="white",height=4, width=15, command = lambda: mostrarVentana(ventanaInformacion)).place(x=89,y=140)
botonRelaciones=Button(ventanaPrincipal, text="*-*MCD de dos \nnumeros*-*", bg = "black", fg="white",height=4, width=15, command = lambda:numerosParaMCD()).place(x=15,y=250)
botonRelaciones=Button(ventanaPrincipal, text="Inverso 'unico'", bg = "black", fg="white",height=4, width=15, command = lambda:inversoUnicoFunc()).place(x=205,y=250)
botonRelaciones=Button(ventanaPrincipal, text="Teorema Chino del \nResiduo", bg = "black", fg="white",height=4, width=15, command = lambda:mostrarVentana(ventanaTeoremaChino)).place(x=390,y=250)
botonSalir=Button(ventanaPrincipal, text="Salir de \n la aplicacion", bg = "blue", fg="white",height=4, width=15, command=lambda: salirPrograma()).place(x=300,y=140)

	

##Creando ventanas para los botones
#Instanciando ventanas
ventanaInformacion = Toplevel(ventanaPrincipal)
ventanaInformacion.withdraw()
ventanaTeoremaChino = Toplevel(ventanaPrincipal)
ventanaTeoremaChino.withdraw()


	##Reloj
clock = Label(ventanaPrincipal, font=('Consolas', 18), bg="Black", fg="yellow")
#clock.pack()
clock.place (x=640, y=450)
reloj ()








##########################################################--------------------VENTANA "INFORMACION DEL PROGRAMA"--------------------------------##########################################################
ventanaInformacion.geometry("400x220+380+350")
ventanaInformacion.config(bg="black")
ventanaInformacion.maxsize(height=420, width=400)
ventanaInformacion.attributes("-alpha", 0.78) #Esto sirve para transparentar ventanas
l1 = Label(ventanaInformacion, image = imagenFondo).place(x=-15,y=-20)
version = Label(ventanaInformacion,text="Version del programa: 1.4.0").place(x=130,y=155)

	#Nombres de nosotros
unamLabel = Label(ventanaInformacion,text="Universidad Nacional Autonoma de Mexico", font=('Consolas', 14), bg="black", fg="yellow").place(x=0,y=-4)
fiLabel =   Label(ventanaInformacion,text="       Facultad de Ingenieria  ", font=('Consolas', 14), bg="black", fg="yellow").place(x=0,y=21)
fiLabel = Label(ventanaInformacion,text="*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-", font=('Consolas', 14), bg="black", fg="blue").place(x=0,y=50)
nombre1 = Label(ventanaInformacion,text="Desarrolladores:" , font=('Consolas', 14), bg="Black", fg="white").place(x=30,y=80)
nombre1 = Label(ventanaInformacion,text="***Lemuz Fuentes Omar Alejandro", font=('Consolas', 11), bg="Black", fg="white").place(x=30,y=100)
nombre2 = Label(ventanaInformacion,text="***Ramirez Castillo Miguel Angel", font=('Consolas', 11), bg="Black", fg="white").place(x=30,y=120)
		
		

		
		
		

		
		



##########################################################--------------------VENTANA Teorema Chino (PROGRAMA 2)--------------------------------##########################################################
def obtenerMyN(iteracion):
	elem1 =  sdg.askinteger('Teorema chino del residuo', '-*[m MOD n]...Escriba el valor de m'+str(iteracion)+': ')
	elem2 =  sdg.askinteger('Teorema chino del residuo', '-*[m MOD n]...Escriba el valor de n'+str(iteracion)+': ')
	return[elem1,elem2]

def capturarDatos():
	global listaTeoremaChino, copiaLista
	listaTeoremaChino = []
	solucionTchino = []
	banderasNegativos = [] #Se coloca un 0 si no es negativo, 1 si encuentra negativo
	cantidad = int(spinBoxValor.get())
	lbl1 = Label(ventanaTeoremaChino,text=str(copiaLista[0][0])+"   MOD   "+str(copiaLista[0][1]), font=('Consolas', 11), bg="Black", fg="white").place(x=80,y=65)
	lbl2 = Label(ventanaTeoremaChino,text=str(copiaLista[1][0])+"   MOD   "+str(copiaLista[1][1]), font=('Consolas', 11), bg="Black", fg="white").place(x=80,y=85)
	lbl3 = Label(ventanaTeoremaChino,text=str(copiaLista[2][0])+"   MOD   "+str(copiaLista[2][1]), font=('Consolas', 11), bg="Black", fg="white").place(x=80,y=105)
	lbl4 = Label(ventanaTeoremaChino,text=str(copiaLista[3][0])+"   MOD   "+str(copiaLista[3][1]), font=('Consolas', 11), bg="Black", fg="white").place(x=80,y=125)
	lblSolPar = Label(ventanaTeoremaChino,text=str("-                                                                     "), font=('Consolas', 11), bg="Black", fg="white").place(x=250,y=175)
	lblSolGral = Label(ventanaTeoremaChino,text=str("-                                                                     "), font=('Consolas', 11), bg="Black", fg="white").place(x=220,y=195)
	print(spinBoxValor.get())
	
	for i in range(0, cantidad):
		x = obtenerMyN(i+1)
		listaTeoremaChino.append(x[0])
		listaTeoremaChino.append(x[1])
	
	for  i in range(0,cantidad):
		if (str(listaTeoremaChino[i])==str(0) or str(listaTeoremaChino[i])<str(0)):
			banderasNegativos.append(1)
		else:
			banderasNegativos.append(0)
			
	if 1 not in banderasNegativos:
		if None in listaTeoremaChino:
			tkinter.messagebox.showinfo(title= "PARECE QUE ALGO NO VA BIEN! :/", message= "Al parecer omitió alguno de los numeros :/. HAGALO NUEVAMENTE :D")
			listaTeoremaChino = []
		elif(None not in listaTeoremaChino):
			print(listaTeoremaChino)
			solucionTchino = mainTeoremaChino(listaTeoremaChino)
			if(cantidad<4):
				for i in range(cantidad*2,9):
					listaTeoremaChino.append("-")
			lbl1 = Label(ventanaTeoremaChino,text=str(listaTeoremaChino[0])+"   MOD   "+str(listaTeoremaChino[1]), font=('Consolas', 11), bg="Black", fg="white").place(x=80,y=65)
			lbl2 = Label(ventanaTeoremaChino,text=str(listaTeoremaChino[2])+"   MOD   "+str(listaTeoremaChino[3]), font=('Consolas', 11), bg="Black", fg="white").place(x=80,y=85)
			lbl3 = Label(ventanaTeoremaChino,text=str(listaTeoremaChino[4])+"   MOD   "+str(listaTeoremaChino[5]), font=('Consolas', 11), bg="Black", fg="white").place(x=80,y=105)
			lbl4 = Label(ventanaTeoremaChino,text=str(listaTeoremaChino[6])+"   MOD   "+str(listaTeoremaChino[7]), font=('Consolas', 11), bg="Black", fg="white").place(x=80,y=125)
			lblSolPar = Label(ventanaTeoremaChino,text=str(solucionTchino[0][1]), font=('Consolas', 11), bg="Black", fg="white").place(x=250,y=175)
			lblSolGral = Label(ventanaTeoremaChino,text=str(solucionTchino[1][1]), font=('Consolas', 11), bg="Black", fg="white").place(x=220,y=195)
			solucionTchino = []
			listaTeoremaChino = []
	else:
		tkinter.messagebox.showinfo(title= "Parece que hubo un problema :/", message= "Razon: No se permiten  numeros nagativos ni cero. Intentelo nuevamente. ")
	
		


listaTeoremaChino = [["-","-"],["-","-"],["-","-"],["-","-"]] #Lista que se le mandara al algoritmo del teorema Chino
copiaLista = listaTeoremaChino
spinBoxValor = IntVar()
ventanaTeoremaChino.title("PROGRAMA 2. TEOREMA CHINO DEL RESIDUO")
ventanaTeoremaChino.attributes("-alpha", 0.91) 
ventanaTeoremaChino.geometry("3600x2500+300+200") 
ventanaTeoremaChino.config(bg='black')
ventanaTeoremaChino.maxsize(height=275, width=620)
imagenFondo2 = PhotoImage(file= "fondoT.png")
labelFondo = Label(ventanaTeoremaChino, image = imagenFondo2).place(x=-300,y=-50)

lbl = Label(ventanaTeoremaChino,text="Elija con cuantos numeros va a trabajar: ", font=('Consolas', 11), bg="Black", fg="white").place(x=5,y=10)
spBox = Spinbox(ventanaTeoremaChino,wrap=True,textvariable= spinBoxValor, width=2, from_=1,to=4).place(x=365, y= 10)
botonObtenerInformacion=Button(ventanaTeoremaChino, text="Estoy listo!", bg = "black", fg="red", command=lambda: capturarDatos()).place(x=465,y=10)
lbl = Label(ventanaTeoremaChino,text="Resumen de los valores introducidos: ", font=('Consolas', 11), bg="Black", fg="green").place(x=5,y=40)
lbl1 = Label(ventanaTeoremaChino,text=str(listaTeoremaChino[0][0])+"   MOD   "+str(listaTeoremaChino[0][1]), font=('Consolas', 11), bg="Black", fg="white").place(x=80,y=65)
lbl2 = Label(ventanaTeoremaChino,text=str(listaTeoremaChino[1][0])+"   MOD   "+str(listaTeoremaChino[1][1]), font=('Consolas', 11), bg="Black", fg="white").place(x=80,y=85)
lbl3 = Label(ventanaTeoremaChino,text=str(listaTeoremaChino[2][0])+"   MOD   "+str(listaTeoremaChino[2][1]), font=('Consolas', 11), bg="Black", fg="white").place(x=80,y=105)
lbl4 = Label(ventanaTeoremaChino,text=str(listaTeoremaChino[3][0])+"   MOD   "+str(listaTeoremaChino[3][1]), font=('Consolas', 11), bg="Black", fg="white").place(x=80,y=125)
lbl = Label(ventanaTeoremaChino,text="=============================RESULTADOS============================= ", font=('Consolas', 11), bg="Black", fg="yellow").place(x=5,y=150)
lblSolParticular = Label(ventanaTeoremaChino,text="La solucion particular es: ", font=('Consolas', 11), bg="Black", fg="yellow").place(x=11,y=175)
lblSolPar = Label(ventanaTeoremaChino,text=str(listaTeoremaChino[3][0]), font=('Consolas', 11), bg="Black", fg="white").place(x=250,y=175)
lblSolGeneral = Label(ventanaTeoremaChino,text="La solucion general es: ", font=('Consolas', 11), bg="Black", fg="yellow").place(x=11,y=195)
lblSolGral = Label(ventanaTeoremaChino,text=str(listaTeoremaChino[3][0]), font=('Consolas', 11), bg="Black", fg="white").place(x=220,y=195)






 
ventanaPrincipal.mainloop() #proceso principal hacia la ventana