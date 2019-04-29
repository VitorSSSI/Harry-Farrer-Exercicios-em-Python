#1.12.1>>>


def main():
    print("Programa para calcular a média de um número indeterminado de idades ")
 

    idade=0
    somaidades=0
    qtdpessoas=0
    average=0.0


    idade=int(input("\nDigite uma idade (A última deve ser  0): "))

    while idade!=0:
        somaidades+=idade
        qtdpessoas+=1
        idade=int(input("\nDigite outra: "))
    
    media=somaidades/qtdpessoas
    print("A média é: %.1f "%(media))
        
    
    return 0

main()