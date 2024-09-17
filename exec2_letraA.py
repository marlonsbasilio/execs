def leitura(palavra):

    cont = 0
    for letra in palavra:
        if (letra == 'a' or letra == 'A'):
            print("LETRA A!\n")
            cont+=1
    return cont    

def main():
    
    palavra = input("Digite uma palavra\n")
    
    quant = leitura(palavra)
    
    if (quant > 0):
        print(f"Existem {quant} letras a ou A na palavra {palavra}\n")
    else:
        print(f"Não há nenhuma letra 'a' ou 'A' na palavra {palavra}\n")
    
    
main()