#Importando todas as letras minúsculas do alfabeto
from string import ascii_lowercase

#Função unravelSentence, que receberá as letras com as regras da permutação, bem como a frase criptografada
def unravelSentence(permutationLetters: list, encryptedPhrase: list) -> str:
    #Fazendo print da string final unindo as letras
    print("".join(ascii_lowercase[permutationLetters.index(letter)] for letter in encryptedPhrase))

while True:
    try:
        #Primeiro input, letras de permutação
        permutationLetters = list(input())
        #Frase criptografada à ser desvendada
        encryptedPhrase = list(input())
        #Chamada da função
        unravelSentence(permutationLetters, encryptedPhrase)
    except EOFError or ValueError:
        break