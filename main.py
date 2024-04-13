#Projeto da calculadora

import gc

print("==============================================CALCULADORA=============================================")

def calculando():
    print("Para somar aperte [1]")
    print("Para subtrair aperte [2]")
    print("Para multiplicar aperte [3]")
    print("Para dividir aperte [4]")
    print("Para obter a radiciação aperte [5] (apenas o primeiro valor será armazenado)")
    print("Para obter a potenciação aperte [6] (o primeiro valor vai ser a base e o segundo o expoente)")
    print("=======================================================================================================")

    calculo = int(input("O que você deseja fazer?"))

    a = int(input("Qual o seu primeiro número?"))

    if calculo != 5:
        b = int(input("Qual o seu segundo número?"))

    if calculo == 1:
        resultado = a+b

    elif calculo == 2:
        resultado = a-b

    elif calculo == 3:
        resultado = a*b

    elif calculo == 4:
        resultado = a/b

    elif calculo == 5:
        resultado = a**0.5

    else:
        resultado = a**b

    print("=======================================================================================================")
    print(f"O resultado foi: {resultado!r}")
    print("=======================================================================================================")

while True:
    calculando()
    continuar_calculando = str(input("Para continuar calculando aperte [c] ou se quiser parar aperte [x]"))
    print("=======================================================================================================")
    if continuar_calculando == "x":
        print("Obrigado por usar a calculadora, até a próxima!")
        break