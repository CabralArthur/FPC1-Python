def handleNumbersList(numsList: list, initialValues: tuple) -> list:
    '''
    Retorna apenas os maiores valores lista selecionada

    -> numsList: lista selecionada
    -> initialValues: (tam_lista, Elementos que serão tirados)
    '''

    #Atribuindo às variáveis os valores inseridos
    size = initialValues[0]
    quantityDeletedNumbers = initialValues[1]

    #Variáveis que representam as posições dos números no array
    currentListPosition = 0
    nextListPosition = 1

    while len(numsList) > (size - quantityDeletedNumbers):
        if nextListPosition < len(numsList):
            #Comparação do tamanho entre números
            if numsList[currentListPosition] < numsList[nextListPosition]:

                del numsList[currentListPosition]

                currentListPosition = 0
                nextListPosition = 1

            else:
                currentListPosition = nextListPosition
                nextListPosition = nextListPosition + 1
        else:

            del numsList[currentListPosition]

            currentListPosition -= 1
    #Retornando array do saldo
    return numsList

while True:
    try:
        #Inserindo valores iniciais, A e B
        initialValues = tuple(map(int,input().split()))

        #Inserindo valor numérico (string) da conta
        numsList = list(input())

        #Convertendo de string numérica para inteiro utilizando list comprehension
        numsList = [int(num) for num in numsList if num.isnumeric()]

        # Chamando a função para retornar a lista com os valores finais
        numsList = handleNumbersList(numsList, initialValues)

        # Printando os valores
        for num in numsList:
            print(num, end='')
        print()

    except EOFError or ValueError:
        break