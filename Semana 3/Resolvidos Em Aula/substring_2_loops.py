"""
    Implemente uma função que exibe todas as substrings de uma string.
    Dica: primeiro enumere todos os substrings que começam com o primeiro caractere.
    Existem n deles se o string tem tamanho n.
    Então, enumere as substrings da string após remover o primeiro caractere.
    Exemplo: substrings de rum: r, ru, rum, u, um, m
"""

string = input('Insira aqui a palavra: ')

for i in range(len(string)):
    for j in range(i, len(string)):
        print(f"{string[i : j + 1]}, ", end="")
    print()