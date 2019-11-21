#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char** argv) {
	char haslo[8];
	if(argc < 2){
		printf("Podaj hasło\n");
		exit(1);
	}
	memcpy(haslo, argv[1], 8);
	if (strncmp(haslo, "Tajne", 8) == 0)
		printf("TAK\n");	
	else
		printf("NIE\n");
	return 0;
}
