numInt = int(input("Digite o numero que deseja descobrir se é primo ou não:\n"))

if numInt <= 0 :
  print("Número inválido")

else:
    numerosControle = [2, 3, 4, 5, 6, 7, 8, 9]
    i = 0
    div = 0
    # coleta os divisores do numero
    while i < 8 :
        if numInt % numerosControle[i] == 0:
            div += 1
        i += 1
    # número é primo
    if div > 1 or numInt == 1:
        print("Não primo")
    # testa se o número não é primo
    elif div == 1 or div == 0:
        print("Primo")
