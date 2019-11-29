#define TAJNY_PIN 1234
int main(int ac, char **av){
	unsigned int pin;
	printf("%d\n",strlen(av[1]));

	//Sprawdzanie czy pierwszy ciag nie ma '-'
	for(int i = 0; i < strlen(av[1]); i++){
		if(av[1][i] =='-'){
			printf("Atak zablokowany\n");
			exit(1);
		}
	}

	sscanf(av[1], "%d", &pin);


	if (pin == TAJNY_PIN) {
		printf("PIN poprawny\n");
	} else {
		printf("PIN bledny\n");
	}
}