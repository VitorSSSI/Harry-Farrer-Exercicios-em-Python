def main():
    nome=""
    preçocompra=0.0
    preçovenda=0.0
    lucro=0.0
    menor10=0
    entre10e20=0
    maior20=0


    nome=input("Nome da mercadoria: ")
    preçocompra=float(input("Preço de compra: "))
    preçovenda=float(input("Preço de revenda: "))
    while preçocompra>0:
        lucro=(preçovenda-preçocompra)/(preçocompra/100)

        if lucro<10:
            menor10+=1
        elif lucro>=10 and lucro<=20:
            entre10e20+=1
        elif lucro>20:
            maior20+=1

        print("\n %s: \nPreço de compra = %.1f \nPreço de venda = %.1f \nLucro = %.1f "%(nome,preçocompra,preçovenda,lucro))

        nome=input("\n\nNome da mercadoria: ")
        preçocompra=float(input("Preço de compra: "))
        preçovenda=float(input("Preço de revenda: "))
    
    print("\n\nTabela de lucro:\nLucro<10: %d\nLucro entre 10 e 20: %d\nLucro>20: %d "%(menor10,entre10e20,maior20))
    
    input()
    return 0

main()