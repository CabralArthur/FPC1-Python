Juvenal estava sem ter o que fazer em uma sexta-feira imprensada e resolveu criar uma função, porém ele não sabe se ela sempre termina, já que é recursiva. A função é a seguinte:

F(n) = {

1, se n = 1

F(n/2), se n for par

F(3*n+1), se n for ímpar

}

Juvenal definiu outra função: G(n) = quantas chamadas recursivas são necessárias para que F(n) atinja o caso base. Agora, dado dois inteiros A e B, Juvenal quer saber qual o maior valor que a função G assume quando n está no intervalo [A,B]. Formato de Entrada A primeira linha contém T, o número de casos de teste. Cada caso de teste contém dois números, A e B.

Restrições 1 <= T <= 100

1 <= A<=B <= 10^5

Formato de Saída Para cada caso imprima "Caso X: Y", onde X é o número do caso de teste atual e Y é o que Juvenal quer saber. Ex: Caso 1: 20

Caso 2: 125

Caso 3: 89

Caso 4: 174

Exemplos. NÃO HÁ LINHAS EM BRANCO NEM NA ENTRADA NEM NA SAÍDA

Entrada:

4

1 10

100 200

201 210

900 1000

Saída:

Caso 1: 20

Caso 2: 125

Caso 3: 89

Caso 4: 174