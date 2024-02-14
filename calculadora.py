from functools import reduce
import operator
import sys

# Avisar que a operação vai acabar se colocar 0:
print('LEMBRANDO QUE: SE QUISER ENCERRAR A OPERAÇÃO, DIGITE "fim"')

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
    número = input("Digite os números para realizar uma operação: ")

    #se o usuário digitar fim, FIM ou 0 e não tiver nenhum número na lista, o programa encerra
    if número == 'fim' or número == 'FIM'  or número == '0' and len(números) == 0:
        print('Não da para fazer a operação sem números')
        sys.exit()
    #se o usuário digitar fim, FIM ou 0 e tiver números na lista, o programa encerra
    elif número == 'fim' or número == 'FIM'  or número == '0':
        break
    #se o usuário digitar letras ou caracteres que seja diferente de números, o programa avisa que é para digitar apenas números
    elif número.isdigit() == False:
        print('Digite apenas números')
        continue
    #se o usuário digitar números, o programa armazena na lista, como um número inteiro
    número = int(número)
    números.append(número)

erro = 0

while True:

    #chama o def exibir_menu, ou seja, mostrar o menu
    exibir_menu()
    opção = input("Digite qual operação ou o número da opção: ")

    #se o usuário digitar somar ou 1, o programa soma os números da lista
    if opção == "somar" or opção == '1':
        resultado = sum(números)
        print('Resultado:', resultado)
        break
    #se o usuário digitar subtrair ou 2, o programa subtrai os números da lista 
    elif opção == "subtrair" or opção == '2':
        resultado = reduce(operator.sub, números)
        print('Resultado:', resultado)
        break
    #se o usuário digitar multiplicação ou 3, o programa multiplica os números da lista
    elif opção == "multiplicação" or opção == '3':
        resultado = reduce(operator.mul, números)
        print('Resultado:', resultado)
        break
    #se o usuário digitar dividir ou 4, o programa divide os números da lista e coloca somente 2 casas decimais
    elif opção == "dividir" or opção == '4':
        resultado = reduce(operator.truediv, números)
        resultadover = round(resultado, 2)
        print('Resultado:', resultadover)
        break
    else:
        #se o usuário digitar qualquer coisa que não seja as opções do menu, adiciona 1 ao erro e se chegar a 3, encerra a operação
        erro += 1
        if erro == 3:
            print('Desculpa, mas vou ter que encerrar a operação')
            sys.exit()
        print("Operação inválida")
        continue

#um dos aperfeiçoamento, colocar um input para que o usuário digite apenas números
