#Função recursiva F, funcionamento de acordo com enunciado
def functionF(currentValue, recursiveCalls):
    if currentValue == 1:
        recursiveCalls += 1
        return recursiveCalls
    elif currentValue % 2 == 0:
        recursiveCalls += 1
        return functionF( currentValue / 2, recursiveCalls)
    else:
        recursiveCalls += 1
        return functionF(3 * currentValue +1, recursiveCalls)

#Função G, que retorna a quantidade de chamadas recursivas
def functionG(A,B):
    #Quantidade de chamadas recursivas
    recursiveCalls = 0
    #Valor máximo que será comparado
    maxValue = 0
    for i in range(A,B+1):
        #Quantidade de chamadas atual
        currentValue = functionF(i, recursiveCalls)
        if currentValue > maxValue:
            maxValue = currentValue
        currentValue = 0
    return maxValue

#Receber quantidade de casos teste
quantityOfCases = int(input())

for i in range(quantityOfCases):
    #Definindo valores A e B
    A,B = [int(x) for x in input().split()]
    
    recursiveQuantityValue = functionG(A,B)

    print(f'Caso {i+1}: {recursiveQuantityValue}')