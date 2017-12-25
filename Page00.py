# Variables, Conditions, Comparaisons et Loop

# if c'est l'anglais pour 'si'
# else se traduit pars 'sinon'
# elif est un raccoursisment de else if
# else if se traduit pars 'sinon si'

# Voici une variable
age = 3;

# On peu preque lire le code comme de l'anglais normale
# Si age < 0 dis a l'utilisateur "Tu n'est pas nee"
if(age<0): print("Tu n'est pas nee")
if(age<18): 
	print("Tu n'est pas majeur")
# Ces deux conditions ne s'excluent pas

# L'else if 
if(age>=18): print("Tu peux passer ton permis")
elif (age>=16): 
	print("Tu peux faire la conduite acompagne")
else: 
	print("Tu peux faire du velo")

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
		print x

# Une autre type de varaible est l'array, ou la liste
semaine = ["Lun", "Mar", "Mer","Jeu","Ven","Sam", "Dim"]

# Pour passer attravers une liste on utilise des for loops
for jour in semaine:
	print(":: ",jour," ::")
	if(jour=="Lun" or jour=="Mer"):
		print("Tu Commence avec Francais")
		print("Ensuite t'as Histoire")
	elif(jour=="Sam" or jour=="Dim"): 
		print("Pas cours c'est le Weekend")
		continue
		# un continue est un type de break pour les loops
		# break fini et sorts du loop
		# continue fini cette loop et passe au prochain
		# sans regarder le code qui suis
	else: 
		print("Pas cours ce matin")

	if(jour=="Jeu"):
		print("T'as pas cours cet aprem")
	else:
		print("Maths cet aprem")