#((exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...)

def fibonatti(number):
    
    print (number)
    if (number == 0):
        return True
    else:
        soma1 = 0
        soma2 = 1
        
        
        while (soma2 <= number):
            if (soma2 == number):
                return True
            aux = soma2
            soma2 = soma2 + soma1
            soma1 = aux
            
        return False
        
def main():
    
    number = int(input("Digite um valor para o numero: \n"))
    
    if (fibonatti(number)):
        print("Este número não pertence a sequencia de Fibonatti")
    else:
        print("Não pertence a sequencia de Fibonatti")
        
main()