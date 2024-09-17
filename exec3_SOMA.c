
#include <stdlib.h>
#include <stdio.h>

int main(){
    
    int INDICE = 12;
    int SOMA = 0;
    int K = 1;
    int cont = 0;
    
    while (K < INDICE){
        printf ("\nITERACAO: %d\n", cont);
        K = K + 1;
        printf ("VALOR DE K: %d\n", K);
        
        SOMA = SOMA + K;
        
        printf ("VALOR DE SOMA: %d\n", SOMA);
        cont++;
    }
    
    printf("\nVALOR DA SOMA FINAL: %d\n",SOMA);
    
    return 0;
}
