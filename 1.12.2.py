#1.12.1>>>

def main():
    altura=0.0
    sexo=""
    maior=-1.0
    menor=100.0
    numH=0
    numM=0
    somaM=0.0
    mediaM=0.0
    cont=5


    #exercício respondido com 5 pessoas ao invés de 50
    while cont>0:

        altura=float(input("altura: "))
        sexo=input("sexo (m or f (m ou f minúsculos) ): ")

        if altura>maior:
            maior=altura
        elif altura<menor:
            menor=altura


        if sexo=="f":
            numM+=1
            somaM+=altura
        else:
            numH+=1
        
        cont-=1

    mediaM=somaM/numM 

    print("maior altura: ",maior)
    print("menor altura: ",menor)
    print("media altura das mulheres: ",mediaM)
    print("quantos homens",numH)





    input()
    return 0

main()