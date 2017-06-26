increment= 0 
txt='esto es una practica'
for c in txt:
	if c =='e':
		increment =increment+1

print ('el parrafo', txt,'contiene:',  increment, 'letra "e"')
print (txt.upper())
print ('la frace anterior esta compuesta por:',len (txt),'letras')
print (txt.replace ('o','0'),'sustituimos la letra o por el 0')