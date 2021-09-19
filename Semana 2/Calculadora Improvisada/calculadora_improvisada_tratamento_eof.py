#Função soma, que será o resultado de diversas operações de sucessão
def successorFunction(num):
    return num + 1 #Retorna o número +1

#Função soma, que será o resultado de diversas operações de sucessão
def sumFunction(firstNum, secondNum):
    for i in range(secondNum): #O número será somado a quantidade de vezes em que o segundo número for definido
       firstNum = successorFunction(firstNum)
    return firstNum

#Para essa função utilizei a conta 2 x 3 como base
def multiplicationFunction(firstNum,secondNum):
    multResult = 0
    for i in range(secondNum): #A operação de soma ocorrerá 3x
        multResult = sumFunction(multResult,firstNum) #A variável do resultado se somará com o primeiro número da operação a quantidade de vezes do loop
                                                           # 2 vezes, variável inicalmente será 0, então será: 0 -> 2 -> 4 -> 6
    return multResult

#Para essa função, utilizei a conta 2 ** 3 como base
def exponentiationFunction(firstNum, secondNum):
    expoResult = 1 #Do mesmo modo da multiplicação, cria-se uma variável para armazenar o valor final do cálculo
    for i in range(secondNum): #E o loop será definido pelo segundo valor da operação (expoente)
        expoResult = multiplicationFunction(expoResult, firstNum) #O qual será multiplicado uma determinada quantidade de vezes pelo primeiro (nesse caso, o valor 2)
                                                                    #Sendo assim, com o valor inicial 1 (valor mínimo para exponenciações), temos: 1 -> 2 -> 4 -> 8
    return expoResult

#Repetição do código infinitas vezes
while True:
    try:
        #Entrada será separada em string
        operacao = input()
        if operacao:
            operacao = operacao.split()    
            for k, v in enumerate(operacao):
                if v.isnumeric():
                    operacao[k] = int(v)
        #Verificação 
        if operacao[0] == 'Suc':
            print(successorFunction(operacao[1]))
        elif operacao[0] == 'Soma':
            print(sumFunction(operacao[1], operacao[2]))
        elif operacao[0] == 'Mult':
            print(multiplicationFunction(operacao[1], operacao[2]))
        elif operacao[0] == 'Exp':
            print(exponentiationFunction(operacao[1], operacao[2]))
    except EOFError or ValueError:
        break