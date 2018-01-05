# Variables, Pointeurs, et Structure de Donnes

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




# et on peu faire plus que de simples calcules
def alcool_dans_sang (volumeAlc, poidsPers, genrePers):	
	if(genrePers == "H"): coefGenre = 0.7
	elif(genrePers == "F"): coefGenre = 0.6
	coefDiffusion = coefGenre * poidsPers

	return volumeAlc/coefDiffusion


# Une classe est aussi appele un object
# Ici notre classe represente des personnes
# Qui sont Client d'un Bar
class ClientBar:
	# En tent que ClientBar, ils on des valeurs interessantes
	def __init__(self, nom, sexe, kg, alcool, verres):
		self.nom = nom
		self.genre = sexe
		self.poids = kg
		self.alcool = alcool
		self.verres = verres

	# Ceci n'est pas une fonction ordinaire
	# On l'apelle une methode
	def alcool_consome(self):
		if(self.alcool=="Biere"):
			degree = 6
			volume = 250
		elif(self.alcool=="Vin"):
			degree = 12
			volume = 125

		desiteAlcool = 0.8
		return degree * volume * desiteAlcool



# Julie et Marc sont clients du bar
julie = ClientBar("Julie", "F", 47, "Vin", 3)
marc = ClientBar("Marc", "H", 85, "Biere", 6)

print("Julie a bu", julie.verres, "verres de", julie.alcool)
print("Marc a bu", marc.verres, "verres de", marc.alcool)

alcoTest_julie = alcool_dans_sang(julie.alcool_consome(),julie.poids, julie.genre)
alcoTest_marc = alcool_dans_sang(marc.alcool_consome(),marc.poids, marc.genre)

if(alcoTest_marc>0.5 and alcoTest_julie>0.5): print("Marc et Julie doivent prendre un Taxi")
else: print("Marc et Julie peuvent rentrer eux meme")