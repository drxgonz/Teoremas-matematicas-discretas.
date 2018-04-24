import tkinter.messagebox  ##para la ventana de decision
from tkinter import simpledialog as sdg


def tc(a, b):
	i=0
	d=[]
	k=1
	
	while True:
		try:
			if ((a[i]*k)%b[i])==1:
				d.append(k)
				i+=1
				if len(d)>0:
					k=1
				if len(d)==len(a):
					break
			else:
				k+=1
		except:
			print("Numeros sin sentido!")
			tkinter.messagebox.showinfo(title= "Algo va mal... :(", message= "ERROR CON LOS NUMEROS INSERTADOS! :(")
			break
	return d


def e(num1,num2):
	if num2 == 0:
		return num1
	return e(num2, num1 % num2)

def mainTeoremaChino(lista):

	print("Entro a TC",lista)
	global p
	num=0
	mod=0
	mult=1
	aux=[]
	c=[]
	f=[]
	p=[]

	for x in range(1, len(lista), 2):
		mult=mult*lista[x]
		aux.append(lista[x])

	if len(aux)==1:
		p.append(1)
	else:
		for i in range(0, len(aux)):
			for j in range(0, len(aux)):
				if aux[i]!=aux[j]:
					p.append(e(aux[i], aux[j]))
					#print(p)

	if len(p)==0:
		p=0
	else:
		for k in p:
			if k==1:
				p=1
			else:
				p=0
				break

	if p==1:
	
		for y in range(0, len(lista), 2):
			f.append(lista[y])

		for z in range(1, len(lista), 2):
			c.append(mult/lista[z])

		d=tc(c, aux)
		suma=0
		mod=0


		for w in range(0, len(c)):
			suma=suma+(d[w]*c[w]*f[w])
		mod=suma%mult

	elif(p!=1):
		tkinter.messagebox.showinfo(title= "Algo va mal... :(", message= "No son primos relativos!. Intentelo nuevamente :D")
		print("No son primos relativos")
		mod = str("-")
		mult = str("-")

	print("Solucion particular: ", mod)
	print("Solucion general: ", "x= ", mod,"+", mult,"k")
	return [["solucion Particular: ", str(mod)],["Solucion General", "x= "+str(mod)+"+"+str(mult)+"k"]]
	
