# Loops, Fonctions et Recurcivite

# Il y a deux facon de faire des loops
# while c'est pendant
# le While Loop:
i = 0
while (i<10): # pendant i est moins que 10
	print(i) # afficher i
	i = i+1 # ajouter 1 a i

	if(i==6): # si i=6 passer a 7  
		i=7
# Ce loop compte de 0 a 9 en sautant le 6
# et comme il n'y a jamais une solution unique
# On peu faire pareil avec un for loop
for x in range(0,10):
	if(x!=6):
		print(x)

# Les fonction sont comme les fonctions mathematiques:
def f(x):
	y=3*(x**2)+2

	# une facon d'utiliser c'est commme une calculatrice
	# qui rends une valeur a l'utilisateur (utilisateur qui
	# peu aussi etre une fonction) 
	return y

def factorial (x):
	if(x==0) return 1 # 0! = 1
	return x*factorial(x-1)