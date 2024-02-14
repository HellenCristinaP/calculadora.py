from functools import reduce
import operator

# Avisar que a operação vai acabar se colocar 0:
print('LEMBRANDO QUE: SE COLOCAR 0, ENCERRARÁ A OPERAÇÃO')

#def= integrar um conjunto de códigos que podem ser utilizados várias vezes no programa
#ou seja, ao inves de colocar print e escrever o menu inteiro, podemos armazena-lo em um def
#ai coloca o nome que quiser no def e quando chamar o nome desse def, ele vai exibir o que escreveu
def exibir_menu():
    print("Menu:")
    print("1. somar")
    print("2. subtrair")
    print("3. multiplicação")
    print("4. dividir")

números = []

while True:
    número = int(input("Digite os números para realizar uma operação: "))
    if número == 0:
        break
    números.append(número)

while True:

    exibir_menu()
    opção = input("Digite qual operação ou o número da opção: ")

    if opção == "somar" or opção == '1':
        resultado = sum(números)
        print('Resultado:', resultado)
        break
    elif opção == "subtrair" or opção == '2':
        resultado = reduce(operator.sub, números)
        print('Resultado:', resultado)
        break
    elif opção == "multiplicação" or opção == '3':
        resultado = reduce(operator.mul, números)
        print('Resultado:', resultado)
        break
    elif opção == "dividir" or opção == '4':
        resultado = reduce(operator.truediv, números)
        resultadover = round(resultado, 2)
        print('Resultado:', resultadover)
        break
    else:
        print("Operação inválida")
        continue

#observação, o número 1 no pyhton, significa verdadeiro, então se colocar
#if opção == "somar" or "1"
#ele vai achar que "somar" é verdadeira, e quaisquer números e operações que colocar, vai somar!
