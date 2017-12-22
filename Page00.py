# Variables, Conditions, Comparaisons et Loop

# if c'est l'anglais pour 'si'
# else se traduit pars 'sinon'
# elif se traduit pars 'sinon si'

age = 18;

if(age<0): print("Tu n'est pas nee")
if(age<18): print("Tu n'est pas majeur")

if(age>=18): print("Tu peux passer ton permis")
elif (age>=16): print("Tu peux faire la conduite acompagne")
else: print("Tu peux faire du velo")





i = 0
while (i<10):
	print(i)
	i = i+1

	if(i==6):
		i=7