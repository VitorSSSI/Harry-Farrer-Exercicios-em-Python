def main():
    populaçãoA=90000000.0
    populaçãoB=200000000.0
    anos=0
    while populaçãoA<populaçãoB:
        populaçãoA=((populaçãoA/100)*3)+populaçãoA
        populaçãoB=((populaçãoB/100)*1.5)+populaçãoB
        anos+=1
    print("Serão necessários %d anos"%(anos))
    input()



    return 0

main()