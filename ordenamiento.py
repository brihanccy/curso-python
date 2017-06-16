def ordenamiento(a):
    for i in range(len (a)):
    	for r in range(len (a)-1, i, -1):
    		if (a[r]< a [r-1]):
    			s(a, r, r-1)
def s(a, r, e):
	a[r], a[e]= a[r], a[e]
contador= int (input('diga la cantidad de numeros a ordenar:'))
sort_numero=[]
for i in range (contador ):
    sort_numero.append(int (input('numero:')))
ordenamiento(sort_numero)
print('los numeros ordenados son:')
print(sort_numero)
print('estos son los numeros ordenados pares:')
for e in range (len(sort_numero)):
    if (sort_numero [e])%2==0:
        sort_numero.sort()

        print (sort_numero [e])
print ('estos son los numero0s ordenados impares:')

for h in range (len(sort_numero)):
    if (sort_numero [h])%2!=0:
        sort_numero.sort()

        print (sort_numero [e])