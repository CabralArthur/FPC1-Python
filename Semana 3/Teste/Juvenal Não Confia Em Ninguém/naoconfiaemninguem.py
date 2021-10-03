#Função searchShip que receberá a matriz e verificará as coordenadas do tabuleiro
#Chamando a função recursiva novamente, que irá verificar todos as coordenadas
#adjacentes da posição atual definida no tabuleiro
def searchShip(board, coordLine, coordColumn, shipNumber):
    if board[coordLine][coordColumn] == '#':
        board[coordLine][coordColumn] = shipNumber
        ships[shipNumber] += 1
    else:
        return
    #Fazendo verificacao dos demais elementos nos lados adjacentes ao pedaço de navio
    if coordLine-1 >= 0:
        searchShip(board, coordLine-1, coordColumn, shipNumber)
    if coordColumn-1 >= 0:
        searchShip(board, coordLine, coordColumn-1, shipNumber)
    if coordLine+1 < lines:
        searchShip(board, coordLine+1, coordColumn, shipNumber)
    if coordColumn+1 < columns:
        searchShip(board, coordLine, coordColumn+1, shipNumber)

#Recebendo a quantidade de linhas e colunas do tabuleiro
lines, columns = map(int, input().split())

#Tabuleiro
board = [None] * lines

#Adicionando linhas ao tabuleiro
for line in range(lines):
    board[line] = list(input())

ships = []
shipNumber = 0

#Percorrendo o tabuleiro
for i in range(lines):
    for j in range(columns):
        #Verificando ocorrência de navio
        if board[i][j] == '#':
            ships.append(int(0))
            #Chamando função caso ocorra
            searchShip(board, i, j, shipNumber)
            shipNumber += 1

#Quantidade de disparos
numberOfShots = int(input())

#Recebendo as coordenadas dos disparos
for x in range(numberOfShots):
    lineShotCoord, columnShotCoord = map(int, input().split())
    try:
        shotCoord = int(board[lineShotCoord-1][columnShotCoord-1])
        ships[shotCoord] -= 1
    except:
        continue

destroyedShips = 0

#Verificando quantos navios foram destruídos
for ship in ships:
    if ship == 0:
        destroyedShips += 1

print(destroyedShips)