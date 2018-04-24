#print("ingresa el numero y su modulo para calcular su inverso 'unico'")
#num= int(input())
#mod = int(input())


def inverso(a, b):
	d=[]
	if a==0 or b==0:
		print("Introduzca un valor distinto de 0 para a y/o b.")
	if b==1:
		d=0
		return d
	elif a==1:
		d=1
		return d
	for i in range(1, b-1):
		if ((a*i)%b)==1:
			d=i
			return d
		else:
			pass
	if len(d)<1:
		print("No existe inverso unico para el entero introducido.")

#print("Inverso 'unico: ", inverso(num,mod))