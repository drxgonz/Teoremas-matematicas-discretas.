def factoresprimos(n):
	i=2
	factores=[]
	while i*i<=n:
		if n%i:
			i+=1
		else:
			n//=i
			factores.append(i)
	if n>1:
		factores.append(n)
		return factores

def ocurrencias(lista):
	n=[]
	rep=[]
	fin=[]
	ceros=[]
	aux=[]
	p=lista[len(lista)-1]
	primos=[2]+[x for x in range(3, p+1, 2) if not [y for y in range(3, int(x**0.5)+1, 2) if (float(x)/y).is_integer()]]
	for x in lista:
		if x not in n:
			n.append(x)
			rep.append(lista.count(x))
	for i in range(len(n)):
		fin.append(n[i]**rep[i])
	for k in range(len(primos)-len(fin)):
		ceros.append(1)
	fin+=ceros
	j=0
	for k in range(0, len(fin)):
		a=fin[j]
		if a%primos[k]:
			aux.append(1)
		else:
			aux.append(fin[j])
			j+=1
	return aux

def gcd(x, y):
	m=1
	if len(x)>len(y):
		for i in range(len(x)-len(y)):
			y.append(1)
	else:
		for j in range(len(y)-len(x)):
			x.append(1)
	for k in range(0, len(x)):
		if x[k]<y[k]:
			m=m*x[k]
		else:
			m=m*y[k]
	return m



def funcionGCD(num1, num2):
	if num1==1 or num2==1:
		res=1
	else:

		lista1 = factoresprimos(num1)
		lista2 = factoresprimos(num2)

		l1 = ocurrencias(lista1)
		l2 = ocurrencias(lista2)
		res = gcd(l1,l2)

	#print("gcd: ", gcd(l1,l2))
	return res