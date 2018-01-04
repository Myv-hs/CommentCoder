/*En C++ le programe est dirigee par le:
int main.
Quand on execute, on peu imaginer que l'ordinateur lis ceci*/
int main () {
	
	/* 1 // Varriables

	En C++ comme dans beacoups de langues, on differencie les 
	types de variables.
	Il y a 4 types basiques: 
	entier, decimale, charactere et booleen */

	int entier = -1; // Z
	float decimale = 1.56347; // R

	char charactere = 'A'; // alphabet, ponctuation, etc...
	bool booleen = true; // vrais ou faux
	/*Quelque chose d'important a noter sur les char et les bools
	c'est qu'ils sont des nombres entiers.
	Un bool est une valeur de 0 ou 1, 
	et un char est un nombre 8-bits*/

	/*Ces 4 types sont l'essentiel mais il y a d'autres types et
	on peu affecter les variables de certaines qualites.
	Avant d'aller plus loin, on va parler de deux qualites 
	possitbles */
	const float pi = 3.1415; /*Comme son nom l'indique, une 
	constance ne varie pas. Ceci peux s'applique a tout les
	types de variables*/
	unsigned int nombreNaturelle = 4; /*unsigned est l'anglais
	pour non-sign: R+ 
	Sont utilisation sur les types nombre est evidant, mais on
	peu aussi l'utiliser sur un char */

	/* BONUS // Variables
	(@MPCIE vous pouvez sauter vers la ligne: )
	Habituellement on va pas se soucier de tout les detailles ici,
	le compilateur prendra souvent l'initiative. Mais parfois, on
	veux untiliser un type specifique*/

	signed char byte = -127; /*Comme dit avant, un char est un
	nombre entier 8-bit. Un octet permet de stocker 256 valeurs.
	un unsigned char pourrais avoir une valeur de 0 a 255.
	Si on regarde ici, byte = le minimum d'un signed char qui peu
	aller de [-127,127] ce qui fait 255 valeurs. Le 256eme est
	utilise par le signe.*/

	/*Petit Bonus sur les char et les limites des variables:
	Dans le jeu Civilisation, l'IA de Ghandi devenais un fou
	de guerre nucleaire apres la decouverte de la democratie */

	/*Parfois il nous faut des valeurs plus grand, ou plus precis
	Pour avoir un entier plus grand on peu faire appel au long: */
	long entier32bit = -2147483647;
	unsigned long naturel32bit = 4294967295;
	double decimaleDoublePrecision = ;

	
	char nom[4] = {'M','a','r','c'};
	int matrice[3][3] = {
		{1,3,2},
		{4,5,2},
		{7,4,2}
	};

	bool continuerLoop = true;
	while(continuerLoop) {
		entier = entier+decimale;
		if(entier>7){
			continuerLoop = false;
		}
	}

	for (int i=0; i<10; i++) {

		if (decimale < pi*100) {
			charactere = 'B';
			booleen = !booleen;
			decimale *=2;
		} else if (decimale == pi) {
			nombreNaturelle --;

		} else nombreNaturelle += 3;
	}
}