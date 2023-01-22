'''
4. Crie duas funções:
○ A primeira função receberá dois parâmetros e retornará como resultado uma
concatenação de texto colocando uma vírgula entre os dois parâmetros ao
uní-los.
○ A segunda função não receberá parâmetros; será feito a leitura de duas
entradas que o usuário digitar; irá chamar a primeira função passando como
argumento os dois textos lidos; por fim esta segunda função irá imprimir para
o usuário informando qual foi o resultado que se obteve na chamada à
primeira função.
○ Exemplo da primeira entrada: “Olá”. Exemplo da segunda entrada: “Mundo”.
Exemplo da saída do sistema: “Olá,Mundo”.
'''

def concatenacao(texto1, texto2):
    return texto1 + ',' + texto2


def print_return():
    texto1 = str(input('Digite a primeira palavra: '))
    texto2 = str(input('Digite a segunda palavra: '))

    print(concatenacao(texto1, texto2))


print_return()