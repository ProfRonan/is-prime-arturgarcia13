numInt = int(input("Digite o numero que deseja descobrir se é primo ou não:\n"))

if numInt <= 0 :
  print("Número inválido")

else:
    i = 2
    div = 0
    # coleta os divisores do numero
    while i <= (numInt**0.5) :
        if numInt % i == 0 and numInt != (numInt**0.5):
            div += 1
            if div >= 2:
                break
        i += 1
    # número é primo
    if div > 0 or numInt == 1:
        print("Não primo")
    # testa se o número não é primo
    elif div == 0:
        print("Primo")
