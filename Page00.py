# Variables, operations, Conditions et Comparaisons


# Voici deux variables
nom = 'Maxwell'
age = 12;
 
# Et deja nous avons notre premier signe operatoire
# le '=' est utilise pour associer un valeur a une
# variable.
# Pour parler d'egalite entre deux variable, ou entre
# une variable et une valeur simple, on utilise le
# double egal: '=='.

# Les autres operations sont simple a comprendre:
somme = 2+2
differance = 2-2
produit = 2*2
quotient = 2/2

# On peu faire des suites d'operations et utiliser les
# parentheses, comme ici la moyenne de 4 notes sur 20.
moyenne = (15+9.5+13+5)/4


# On peu presque lire le code comme de l'anglais normale
# avec un tout petit peu de vocabulaire

# print est une fonction qui affiche a l'ecran, on pourrais le 
# paraphraser ici avec "dis a l'utilisateur"
print("Bonjour",nom)
# "Dis a l'utilisateur: Bonjour (nom)"

# if c'est l'anglais pour 'si'
# else se traduit pars 'sinon'
# elif est un raccoursisment de else if (specifique au langage)
# else if se traduit pars 'sinon si'

# Si age est egale a 3
if(age==12):
	# dis a l'utilisateur "Tu a 3 ans" 
	print("Tu a 12 ans")

	# comme vous pouvez voir il y a une marge ici
	# ceci ve dire qu'on est dans le if
	# le code qui suis ne executera que si l'age == 12

	# dans 10 ans
	anneesFutur = 10
	# age serra egale a: son age actuelle + les anneesFutur
	age = age+anneesFutur
	# dis a l'utilisateur: 
	#"Dans (le temps defini) ans tu aurra (l'age calcule)"
	print("Dans",anneesFutur,"ans tu aurra:",age)



# On utilisera souvent les resultats de comparaisons comme
# conditions. Comme audessu, on compare l'age a 3 ans, pour 
# trouver une egalite. Si ils sont egaux, on execute ce que
# la condition demande.

# Regadons commant des conditions interagissent:

if(age<18): print("Tu n'est pas majeur")

# si age < 18 il ne peu pas etre >= a 18
# alors la ligne 58 et ligne 64 s'excluent
# par le resultat de leur comparaison

if(age>=18): print("Tu est majeur")

# mais si on a plus de 18 ans cela n'exclut pas d'avoir plus
# de 21 ans

if(age>21): print("Tu peux aussi boire aux Etats Unis")


# Rajoutons le else, on peu refaire les lignes 58 et 64
# Avec une seul comparaison
if(age<18): print("Ecoute tes parents")
else: print("Sois responsable")


# Finalement avec l'else if
# On verifie d'abord notre premier if
if(age>=18): print("Tu peux passer ton permis")
# Si la condition n'est pas verifie, on peu regarder une autre
elif (age>=16): print("Tu peux faire la conduite acompagne")

# La seconde condition n'exclu pas la premiere par la comparaison
# mais avec le else une seule des deux va etre utilise
# lance ce script et regarde ce qui sorts dans la console,
# puis change la varaible age