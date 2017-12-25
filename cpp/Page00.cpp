int main () {
	
	int entier = -1;
	float decimale = 1.56347;
	char charactere = 'A';
	bool booleen = true;

	unsigned int nombreNaturelle = 4;
	const float pi = 3.1415;
	
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