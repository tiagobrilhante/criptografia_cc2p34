import random as rd
from math import ceil

import numpy as np
from numpy import random

# input da mensagem
mensagem = input('\033[0;0m Digite a mensagem: ')

# lista de caracteres
# #
print('')
print('-------')
print('----- tabela de caracteres especiais----')
print('╬ = ', ord('╬'))
print('║ = ', ord('║'))
print('╣ = ', ord('╣'))
print('╦ = ', ord('╦'))
print('╚ = ', ord('╚'))
print('╔ = ', ord('╔'))
print('┤ = ', ord('┤'))
print('▙ = ', ord('▙'))
print('▝ = ', ord('▝'))
print('┌ = ', ord('┌'))
print('┴ = ', ord('┴'))
print('│ = ', ord('│'))
print('¬ = ', ord('¬'))
print('¤ = ', ord('¤'))
print('Ð = ', ord('Ð'))
print('█ = ', ord('█'))
print('▄ = ', ord('▄'))
print('▀ = ', ord('▀'))
print('■ = ', ord('■'))
print('░ = ', ord('░'))
print('▒ = ', ord('▒'))
print('▓ = ', ord('▓'))
print('ß = ', ord('ß'))
print('þ = ', ord('þ'))
print('¶ = ', ord('¶'))
print('Þ = ', ord('Þ'))
print('ý = ', ord('ý'))
print('¢ = ', ord('¢'))
print('£ = ', ord('£'))
print('ø = ', ord('ø'))
print('Ø = ', ord('Ø'))
print('® = ', ord('®'))
print('æ = ', ord('æ'))
print('Æ = ', ord('Æ'))
print('× = ', ord('×'))
print('« = ', ord('«'))
print('» = ', ord('»'))
print('------')
for i in range(9700, 9800):
    print('-', chr(i), ',', i)
print('---fim tabela----')
print('-------')

print('')
print('Tabela de conversão simples (mensagem)-----')
print('A = ', ord('A'))
print('B = ', ord('B'))
print('C = ', ord('C'))
print('D = ', ord('D'))
print('E = ', ord('E'))
print('F = ', ord('F'))
print('G = ', ord('G'))
print('H = ', ord('H'))
print('I = ', ord('I'))
print('J = ', ord('J'))
print('K = ', ord('K'))
print('L = ', ord('L'))
print('M = ', ord('M'))
print('N = ', ord('N'))
print('O = ', ord('O'))
print('P = ', ord('P'))
print('Q = ', ord('Q'))
print('R = ', ord('R'))
print('S = ', ord('S'))
print('T = ', ord('T'))
print('U = ', ord('U'))
print('V = ', ord('V'))
print('W = ', ord('W'))
print('X = ', ord('X'))
print('Y = ', ord('Y'))
print('Z = ', ord('Z'))
print('espaco = ', ord(' '))
print('----Fim Tabela -----')
print('----exemplo -----')
print('-----')

# 37 char especiais o relevantKey é um numero de 0 a 9 (ele entra como str tem que converter)

# isso aqui converte int em char (mostra qual é o caracter a usar)
# print(chr(162))
# print(chr(9619))

arrayCaracteresEspeciais = np.array(
    [ord('╬'), ord('║'), ord('╣'), ord('╦'), ord('╚'), ord('╔'), ord('┤'), ord('▙'), ord('▝'), ord('┌'), ord('┴'),
     ord('│'), ord('¬'), ord('¤'), ord('Ð'), ord('█'), ord('▄'), ord('▀'), ord('■'), ord('░'), ord('▒'), ord('▓'),
     ord('ß'), ord('þ'), ord('¶'), ord('Þ'), ord('ý'), ord('¢'), ord('£'), ord('ø'), ord('Ø'), ord('®'), ord('æ'),
     ord('Æ'), ord('×'), ord('«'), ord('»')])
print('arrayCharSpec = ', arrayCaracteresEspeciais)
print('quantidade de char espec = ', len(arrayCaracteresEspeciais))

if ord(mensagem[0]) in arrayCaracteresEspeciais:
    print('é pra descriptografar')
else:
    print('é pra criptografar')

# converto tudo pra maiuscula
mensagem = mensagem.upper()

print('A mensagem enviada é: ', mensagem)
print('a mensagem possui: ', len(mensagem), ' caracteres.')

# se a mensagem fom maior que 100, tenho que usar um valor baseado na quantidade total de caracteres
# tipo a quantidade de caracteres da mensagem /2
# no calculo para menores que 100, nos baseamos na diferença entre a quantidade e o número de referencia mínima
if len(mensagem) < 100:

    if len(mensagem) < 10:
        charAAdicionar = ceil(100 - len(mensagem))
    elif 50 > len(mensagem) >= 10:
        charAAdicionar = 60
    else:
        charAAdicionar = 80
else:
    charAAdicionar = ceil(len(mensagem) / 3)

print('tenho que adicionar: ', charAAdicionar, ' caracteres.')
# aqui eu gero a chave randomica que será a base dos saltos de embaralhamento
randomKey = str(rd.randrange(1000000, 9999999, 7))

print('Chave randômica gerada pelo sistema: ', randomKey)

relevantKey = randomKey[6]
# o número de relevancia inicial é o último dígito
print('relevant key = ', relevantKey)

# tenho que ver a partir da relevantKey se é par ou impar
# usando a relevantKey, tenho que dizer quais são os char válidos e quais são os fakes
# além disso tenho que dentre os fakes nomear os que são os abre e fecha chaves para sequencias inválidadas de strings
# além disso tenho que dentre os válidos nomear os que são os abre e fecha chaves para validação da mensagem criptografada
# se é par, index par - verdadeiro
# se não, index impar verdadeiro

arrayCaracPar = np.array([])
arrayCaracImpar = np.array([])

for z in range(37):
    if (z % 2 == 0):
        arrayCaracPar = np.append(arrayCaracPar, arrayCaracteresEspeciais[z])
    else:
        arrayCaracImpar = np.append(arrayCaracImpar, arrayCaracteresEspeciais[z])
print('---------')
print('arraypar: ', arrayCaracPar)
print('---------')
print('arrayimpar: ', arrayCaracImpar)

# dessa forma, se a relevant key for par os caracteres válidos são pares
# se for impar, os caracteres válidos são impar
print(
    'Dessa forma, se a relevant key for par os caracteres válidos são pares se for impar, os caracteres válidos são impar')
arrayCaracValido = np.array([])
arrayCaracFake = np.array([])

if (int(relevantKey) % 2 == 0):
    arrayCaracValido = arrayCaracPar
    arrayCaracFake = arrayCaracImpar
else:
    arrayCaracValido = arrayCaracImpar
    arrayCaracFake = arrayCaracPar
print('---------')
print('caracteres validos: ', arrayCaracValido)
print('---------')
print('caracteres invalidos: ', arrayCaracFake)
print('---------')

# agora que eu sei os válidos e inválidos
# devo definir quais dos válidos são considerados abertura e fechamento de mensagem para validação
# deverão ser escolhidos 6 como abridores e fechadores e o resto passa a ser base de chave para o embaralhamento
# a base para a escolha será a relevant key. o index comeca a partir dela

print('agora eu inicio separando dentre os válidos e invalidos, 6 caracteres para assumirem funções especiais')
arrayValidador = np.array([])
arrayAnulador = np.array([])

for u in range(int(relevantKey) + 2, int(relevantKey) + 8):
    arrayValidador = np.append(arrayValidador, arrayCaracValido[u])
    arrayAnulador = np.append(arrayAnulador, arrayCaracFake[u])

print('array Validador', arrayValidador)
print('array Anulador', arrayAnulador)
print('-------')
print('tenho que ter o cuidado de remover da lista de carateres inválidos, esses 6 especiais que foram definidos')
arrayCaracFakeFinal = np.array([])
for cf in arrayCaracFake:
    if cf not in arrayAnulador:
        arrayCaracFakeFinal = np.append(arrayCaracFakeFinal, cf)
print('desta forma, o arrayCaracFakeFinal, passará a ser: ', arrayCaracFakeFinal)
print('-------')


# agora eu sei quais são os validadores de chave e os anuladores
# em resumo temos o seguinte
# os validadores devem estar no início e no final da frase
# pode ser qualquer um desses

# os anuladores são usados para dificultar a descriptografação
# em resumo, tudo o que estiver entre esses caracteres deve ser descartado

# o primeiro caracter é um dos validadores... o segundo caracter é a chave relevante (alterada por uma tabela de correlação) a partir daí, usaremos a cadeia
# de caracteres válidos para disseminar o restante dos numeros que compoem o unixtime

def ajustaChaveRelevante(chaveRelevante):
    chaveRelevante = str(chaveRelevante)
    if chaveRelevante == '1':
        return 'A'
    elif chaveRelevante == '2':
        return 'B'
    elif chaveRelevante == '3':
        return 'C'
    elif chaveRelevante == '4':
        return 'D'
    elif chaveRelevante == '5':
        return 'E'
    elif chaveRelevante == '6':
        return 'F'
    elif chaveRelevante == '7':
        return 'G'
    elif chaveRelevante == '8':
        return 'H'
    elif chaveRelevante == '9':
        return 'I'
    else:
        return 'J'


print('relevant Key Original: ', relevantKey)
print('chaveRelevante ocultada: ', ajustaChaveRelevante(relevantKey))

# desta feita temos que o primeiro caracter é um dos validadores , o segundo caracter vai ser uma letra, que é convertida a partir
# da relevant key

# o resto aagora vai funcionar da seguinte forma
# eu tenho o tamanho da mensagem no len, e sei quantos caracteres eu preciso usar para ajustar a mensagem
# a var charAAdicionar fala isso
print('char a adicionar: ', charAAdicionar)

# a ideia é criar umacadeia de 6 digitos para embaralhar o randomKey restante
print('randomKey: ', randomKey)


# tudo se baseia nos caracteres em ascii o index da unx key, excluido-se o ultimo, já que ele é a relevantKey

# essa função recebe um digito da randomKey e entrega qual será o escolhido para ajustar o embaralhamento
def retornadorEspecial(indexRK):
    arrayCaracValidoUsavel = np.array([])
    # significa que o função deve buscar dentro da array de char válidos, qual tem o final 0 e escolher um
    for i in arrayCaracValido.astype(int):
        charI = str(i)
        lastIdigit = charI[len(str(i)) - 1]
        if int(indexRK) == int(lastIdigit):
            arrayCaracValidoUsavel = np.append(arrayCaracValidoUsavel, i)

    return np.random.choice(arrayCaracValidoUsavel.astype(int), 1)


# lembrando que o caractere respectivo a randomkey estará distante o mesmo numero do cacarter especial
# por exemplo se a um digito da randomKey for o 6 e a relevantKey for 4
# existem essas possibilidades : [216]
# nota que a conversão desse int-ASCII = Ø
# por ter o final 6, usamos um caracter especial que o último digito é 6
# logo, 6 caracteres apos o Ø na mensagem vai ter um numero convertido em letra, que será o digito randomKey
# exemplo AGVFEGHDØUGFC$AGGGGG observe que o 6 caracter após o Ø e a letra A
# o sistema então desconverte o caracter A para um número( que no caso vai ser 1)
# assim achamos um dígito da randomkey!

print('teste de exemplo')
print(retornadorEspecial(6))
print('type: ', type(retornadorEspecial(6)))
print(chr(int(retornadorEspecial(6))))
print('teste de exemplo')

# agora vou inciar a montagem simples da array que vai espalhar a unix key
arrayRKChar = np.array([])
for k in randomKey:
    castChave = int(k)
    castChar = int(retornadorEspecial(k)[0])

    arrayRKChar = np.append(arrayRKChar, [castChave, castChar]).astype(int)

print('arrayRKChar: ', arrayRKChar)

# exemplo de output arrayRKChar:  [   4 9484    3 9553    8  198    8  248    5 9625    7 9617    3 9553]
# isso mostra toda a cadeia de convesão de caracteres, sendo que os dois ultimos index devem ser removidos
# primeiro grupo- index: 0 e 1
# segundo grupo- index: 2 e 3
# terceiro grupo- index: 4 e 5
# quarto grupo- index: 6 e 7
# quinto grupo- index: 8 e 9
# sexto grupo- index: 10 e 11

print('arrayRKChar0: ', arrayRKChar[0])
print('arrayRKChar1: ', arrayRKChar[1])
print('arrayRKChar2: ', arrayRKChar[2])
print('arrayRKChar3: ', arrayRKChar[3])
print('arrayRKChar4: ', arrayRKChar[4])
print('arrayRKChar5: ', arrayRKChar[5])
print('arrayRKChar6: ', arrayRKChar[6])
print('arrayRKChar7: ', arrayRKChar[7])
print('arrayRKChar8: ', arrayRKChar[8])
print('arrayRKChar9: ', arrayRKChar[9])
print('arrayRKChar10: ', arrayRKChar[10])
print('arrayRKChar11: ', arrayRKChar[11])

# ou seja
print('lembrando que a randomKey = ', randomKey)
print(arrayRKChar[0], ' digitos após o caracter: ', chr(arrayRKChar[1]), ' vai ter a letra: ',
      ajustaChaveRelevante(arrayRKChar[0]), ' que nada mais é do que o: ', arrayRKChar[0], ' convertido!')
print(arrayRKChar[2], ' digitos após o caracter: ', chr(arrayRKChar[3]), ' vai ter a letra: ',
      ajustaChaveRelevante(arrayRKChar[2]), ' que nada mais é do que o: ', arrayRKChar[2], ' convertido!')
print(arrayRKChar[4], ' digitos após o caracter: ', chr(arrayRKChar[5]), ' vai ter a letra: ',
      ajustaChaveRelevante(arrayRKChar[4]), ' que nada mais é do que o: ', arrayRKChar[4], ' convertido!')
print(arrayRKChar[6], ' digitos após o caracter: ', chr(arrayRKChar[7]), ' vai ter a letra: ',
      ajustaChaveRelevante(arrayRKChar[6]), ' que nada mais é do que o: ', arrayRKChar[6], ' convertido!')
print(arrayRKChar[8], ' digitos após o caracter: ', chr(arrayRKChar[9]), ' vai ter a letra: ',
      ajustaChaveRelevante(arrayRKChar[8]), ' que nada mais é do que o: ', arrayRKChar[8], ' convertido!')
print(arrayRKChar[10], ' digitos após o caracter: ', chr(arrayRKChar[11]), ' vai ter a letra: ',
      ajustaChaveRelevante(arrayRKChar[10]), ' que nada mais é do que o: ', arrayRKChar[10], ' convertido!')

print('vamos fazer o teste de conversão simples do que já temos até agora:')
print('mensagem =', mensagem)
print('temos a randomKey: ', randomKey)
print('convertendo a cadeida de caracteres da msg em ascii-int, temos:')

vetorASCII = np.array([])
# vetor2 = np.array([10, 3, 4, 11])
# vetor3 = np.array([''])
# contador = 0
for n in mensagem:
    print(n)
    print(ord(n))
    vetorASCII = np.append(vetorASCII, int(ord(n)))
    # vetor3 = np.append(vetor3, contador)
    # contador += 1

print('vetor ascii ', vetorASCII.astype(int))
print('temos uma situação aqui... o tamanho da palavra é: ', len(vetorASCII))
print('e o tamanho da chaveRandom é: ', len(randomKey))

# vale ressaltar que temos que nos preparar para a quantidade de caracteres da mensagem
# dentro das chaves de validação usando o ultimo caracter (o validador) e o penultimo (indice de index de tamanho)
# exemplo:    ║HFDGHSFGSGHYYYTSDG¶ABCÆ
# sabemos que o último e o primeiro caracteres são especiais pois são os validadores iniciais de mensagem
# nesse caso temos o ║ como primeiro e
# Æ como o último
# imaginemos que eles são realmente os corretos de acordo com a relevant key
# podemos observar que o penultimo caracter especial é o ¶
# imaginemos que ele tb é um dos validadores de mensagem
# essa string ¶ABCÆ contem a quantidade de caracteres da mensagem (numeros convertidos em letras)
# dessa forma sabemos que a mensagem tem 123 caracteres
# nesse caso, não precisamos excluir digitos do randomKey
# o problema por exemplo, seria se essa string fosse ¶EÆ
# nesse caso sabemos que a mensagem teria 5 caracteres, o que é menos do que os 7 caracteres do randomKey
# desta feita, para efeitos de conversão da mensagem, usariamos apenas os 5 primeiros digitos do randomKey
# se a randomKey fosse 1234567
# usariamos apenas 12345 e descartaríamos o 6 e 7

vetorConvertido = np.array([])

# iniciando a hipotese de mensagens com menos de 7 caracteres
if (len(mensagem) < 7):
    print('nessa situação vamos descartar os numeros da randomKey que não vão ser usados')
    # lembrar de alternar soma e subtração
    alternadorSinal = 0
    for r in range(len(mensagem)):
        print('nesse laço a randomKey é : ', randomKey[r], ' e a posicão do vetor ASCII é: ', int(vetorASCII[r]))
        # para criptografar
        if (alternadorSinal % 2 == 0):
            print('aqui estou somando: ', int(vetorASCII[r]), ' com ', int(randomKey[r]), ' o que dá: ',
                  int(vetorASCII[r]) + int(randomKey[r]))
            vetorConvertido = np.append(vetorConvertido, int(vetorASCII[r]) + int(randomKey[r]))
        else:
            print('aqui estou subtraindo: ', int(vetorASCII[r]), ' com ', int(randomKey[r]), ' o que dá: ',
                  int(vetorASCII[r]) - int(randomKey[r]))
            vetorConvertido = np.append(vetorConvertido, int(vetorASCII[r]) - int(randomKey[r]))
        alternadorSinal += 1
        print('----')

# iniciando a hipootese de mensagens com mais de 7 caracteres
# nesse caso haverá ciclo de repetições dentro da randomKey
# tem que lembrar que para a criptografia, sempre se soma o indice 0
# para descriptografia sempre se subtrai
else:
    print('podemos usar todos os digitos da randomKey')
    alternadorSinal = 0
    posicaoIndex = 0
    for r in range(len(mensagem)):
        if posicaoIndex != 6:
            # nesse caso eu entro no loop (lembrando que a randomKey tem 7 digitos)
            # para criprografia eu começo somando
            if (alternadorSinal % 2 == 0):
                print('aqui estou somando: ', int(vetorASCII[r]), ' com ', int(randomKey[posicaoIndex]), ' o que dá: ',
                      int(vetorASCII[r]) + int(randomKey[posicaoIndex]))
                vetorConvertido = np.append(vetorConvertido, int(vetorASCII[r]) + int(randomKey[posicaoIndex]))
            else:
                print('aqui estou subtraindo: ', int(vetorASCII[r]), ' com ', int(randomKey[posicaoIndex]),
                      ' o que dá: ',
                      int(vetorASCII[r]) - int(randomKey[posicaoIndex]))
                vetorConvertido = np.append(vetorConvertido, int(vetorASCII[r]) - int(randomKey[posicaoIndex]))
            alternadorSinal += 1
            # tenho que incrementar o index
            posicaoIndex += 1
            print('----')
        else:
            if (alternadorSinal % 2 == 0):
                print('aqui estou somando: ', int(vetorASCII[r]), ' com ', int(randomKey[posicaoIndex]), ' o que dá: ',
                      int(vetorASCII[r]) + int(randomKey[posicaoIndex]))
                vetorConvertido = np.append(vetorConvertido, int(vetorASCII[r]) + int(randomKey[posicaoIndex]))
            else:
                print('aqui estou subtraindo: ', int(vetorASCII[r]), ' com ', int(randomKey[posicaoIndex]),
                      ' o que dá: ',
                      int(vetorASCII[r]) - int(randomKey[posicaoIndex]))
                vetorConvertido = np.append(vetorConvertido, int(vetorASCII[r]) - int(randomKey[posicaoIndex]))
            # tenho que resetar tudo para o reiniciio
            posicaoIndex = 0
            alternadorSinal = 0
            print('----')

print('o vetor convertido é: ', vetorConvertido)

mensagemConvertida = ''

for g in vetorConvertido.astype(int):
    mensagemConvertida = mensagemConvertida + str(chr(int(g)))

print('randomKey', randomKey)
print('mensagem original', mensagem)
print('mensagem base convertida', mensagemConvertida)

# tenho que adicionar agora os blocos de informação falsa
# O calculo começa dividindo 100 pelo tamanho da mensagem e depois dividindo por 2
# isso funciona para mensagens com menos de 100 caracteres
# com mais de 100, sempre serão adicionados 5 blocos independente da quantidade

# repensar isso... definir a quantidade de blocos com base nos caracteres e não em um calculo aleatório
print('tamanho da mensagem: ', len(mensagem))

# se o tamanho da msg for menor que 100 tenho que ver a quantidade de caracteres a adicionar e dividir pelo len da msg
# se o tamanho da mensagem for maior que 100 cou usar a quantidade total de char da msg /2

print('charAdicionar: ', charAAdicionar)
print('lenmsg: ', len(mensagem))

if len(mensagem) <= 100:
    numBlocosAdicionar = ceil(charAAdicionar - (charAAdicionar / 2) - (charAAdicionar / 4))
else:
    numBlocosAdicionar = ceil(len(mensagem) / 10)
print('numero de blocos: ', numBlocosAdicionar)
print('isso significa que vou ter que distribuir: ', charAAdicionar, ' caracteres adicionais (sem relevância) em ',
      numBlocosAdicionar, ' blocos.')
print('para fins de embaralhamento, serão contabilizados os caracteres especiais falsos')
print('lembrar dos caracteres que emitem blocos com X quantidades de caracteres escondidos')

print('a abertura e fechamento sera um dos caracteres aqui: ', arrayValidador)
charSpecAbertura = np.random.choice(arrayValidador, 1)
charSpecFechamento = np.random.choice(arrayValidador, 1)
charSpecLimitadorLen = np.random.choice(arrayValidador, 1)
print('escolho então para abrir o: ', charSpecAbertura, ' que no caso é o: ', chr(int(charSpecAbertura)))
print('escolho então pra fechar o: ', charSpecFechamento, ' que no caso é o: ', chr(int(charSpecFechamento)))
cadeiaAbertura = chr(int(charSpecAbertura)) + ajustaChaveRelevante(relevantKey)
print('logo a abertura da mensagem será: ', chr(int(charSpecAbertura)), ' e ', ajustaChaveRelevante(relevantKey), ': ',
      cadeiaAbertura)
print('para o fechamento temos:')
print('o char de limitador de tamanho: ', charSpecLimitadorLen)
print('o char de final de mensagem : ', charSpecFechamento)
print('e entre eles o tamanho da mensagem convertido para letras: ')
print('a mensagem tem: ', len(mensagem), ' caracteres')

# aqui eu faço a conversão
# primeiro transformo o len em str e converto cada index e depois monto de novo
tamanhoEmStr = str(len(mensagem))
cadeiaLenConvertida = ''
for cadaLetra in tamanhoEmStr:
    cadeiaLenConvertida = cadeiaLenConvertida + str(ajustaChaveRelevante(cadaLetra))
print('convertendo isso em letra temos: ', cadeiaLenConvertida)
cadeiaFechamento = chr(int(charSpecLimitadorLen)) + str(cadeiaLenConvertida) + chr(int(charSpecFechamento))
print('por fim, a cadeia de fechamento da mensagem sera: ', cadeiaFechamento)

print('só para exemplo vemos que a mensagem final, até agora está assim: ',
      cadeiaAbertura + mensagemConvertida + cadeiaFechamento)

print('cadeiaAbertura + mensagemConvertida + cadeiaFechamento')
print(
    'agora vamos passar a distribuir os caracteres para blocos falsos, caracteres para distribuir a randomKey e caracteres de validação e a própria mensagem em si')

print(
    'inicialmente sabemos que sempre existirão 7 blocos de validadores. eles são obrigatórios e são removidos logo que a randomkey for identificada')
print('vamos montar esses blocos')
print('bloco 1 - corresnpondente ao index0 da randomKey')

print(arrayRKChar[0], ' digitos após o caracter: ', chr(arrayRKChar[1]), ' vai ter a letra: ',
      ajustaChaveRelevante(arrayRKChar[0]), ' que nada mais é do que o: ', arrayRKChar[0], ' convertido!')
print('para montar esse bloco, devemos seguir essa lógica')
# monto um array do tamanho de digitos e preencho
cadeia1 = np.random.randint(65, 90, arrayRKChar[0] - 1)
print('cadeia1 = ', cadeia1)
textoCadeia1 = ''
for car in cadeia1:
    textoCadeia1 = textoCadeia1 + chr(car)

textoCadeia1 = chr(arrayRKChar[1]) + textoCadeia1 + ajustaChaveRelevante(arrayRKChar[0])
print('textocadeia1 = ', textoCadeia1)

print('-------')
print('-------')
print('-------')
print('-------')


def montadorCadeiaAutenticacao(index):
    print('index: ', index)
    print(arrayRKChar[index], ' digitos após o caracter: ', chr(arrayRKChar[index + 1]), ' vai ter a letra: ',
          ajustaChaveRelevante(arrayRKChar[index]), ' que nada mais é do que o: ', arrayRKChar[index], ' convertido!')
    print('para montar esse bloco, devemos seguir essa lógica')
    cadeia = np.random.randint(65, 90, arrayRKChar[index])
    print('cadeia = ', cadeia)
    textoCadeia = ''
    for car in cadeia:
        textoCadeia = textoCadeia + chr(car)

    textoCadeia = chr(arrayRKChar[index + 1]) + textoCadeia + ajustaChaveRelevante(arrayRKChar[index])
    print('textocadeia = ', textoCadeia)
    return textoCadeia


# primeiro grupo- index: 0 e 1
# segundo grupo- index: 2 e 3
# terceiro grupo- index: 4 e 5
# quarto grupo- index: 6 e 7
# quinto grupo- index: 8 e 9
# sexto grupo- index: 10 e 11
print('lembrando que a randomKey é: ', randomKey)

# logo
print('------ calculador---------')
bloco1 = montadorCadeiaAutenticacao(0)
bloco2 = montadorCadeiaAutenticacao(2)
bloco3 = montadorCadeiaAutenticacao(4)
bloco4 = montadorCadeiaAutenticacao(6)
bloco5 = montadorCadeiaAutenticacao(8)
bloco6 = montadorCadeiaAutenticacao(10)
print('---------fim calculador ---------')

print('-------')
print('a função usando index 0 é: ', bloco1)
print('-------')
print('a função usando index 1 é: ', bloco2)
print('-------')
print('a função usando index 2 é: ', bloco3)
print('-------')
print('a função usando index 3 é: ', bloco4)
print('-------')
print('a função usando index 4 é: ', bloco5)
print('-------')
print('a função usando index 5 é: ', bloco6)
print('-------')

# print(vetorASCII.dtype) 152497-----9
# print('vetor 2', vetor2)
# print(vetor2.dtype)
# print('vetor 3', vetor3)
# print(vetor3.dtype)


print('----------')
print('----------')

print('voltando ao numero de blocos, temos que adicionar: ', numBlocosAdicionar, ' blocos')
print('caracteres a adicionar: ', charAAdicionar, ' car')
print('mas de cara já temos 6 blocos por causa dos blocos validadores')
print('e eles por sua vez já possuem caracteres')
somaCarAutent = len(bloco1) + len(bloco2) + len(bloco3) + len(bloco4) + len(bloco5) + len(bloco6)
print('então vamos reduzir de: ', charAAdicionar, ' a quantia de: ', somaCarAutent,
      '(que é a soma de caracteres dos adicionais de autenticação')
charAAdicionar = charAAdicionar - somaCarAutent
print('teremos que adicionar então agora: ', charAAdicionar)
numBlocosAdicionar = numBlocosAdicionar - 6
print('como temos ja 6 blocos, agora temos que adicionar: ', numBlocosAdicionar)
print('em resumo, temos que adicionar a mensagem ',
      numBlocosAdicionar, ' blocos, distribuindo um total de: ', charAAdicionar, ' caracteres')

# aqui temos uma situação
# podemos usar caracteres inválidos, e blocos definidos nos arrayAnulador, e por fim passar os blocos de autenticação
# a ideia é estabelecer o número máximo de caracteres e ir diminuindo a medida que as chaves vão sendo criadas.
# estabelecer um aleatório que oscile em
# 1 - caracter invalido
# 2 - bloco aleatorio
# 3 - bloco de autenticação (é obrigatório ter todos)
# 4 - caso a resposta for falsa, injeta um caracter da mensagem (tem que contar)
# o que vai gerar uma array contendo tudo que foi criado
# tem que ir diminuindo o numero de blocos , caso seja o bloco (junto com os caracteres)
# ou caso seja sorteado um caracter especial não válido, diminuir só o caracter

print('lembrando que a chave ascii é: ', vetorASCII)
print('mensagem convertida é: ', mensagemConvertida)
print('temos que contar o numero de caracteres, pois eles vão iniciar o processo de loop')
print('o numero de caracteres é: ', len(mensagemConvertida))
print('----------')
print('isso significa qe vamos entrar em um loop de ', len(mensagemConvertida), 'e nesse loop vamos distribuir:')
print('chave de validadores, que são 6')
print('caracteres inválidos')
print('blocos invalidos inválidos')
print('caracteres da mensagem')
print('----------')

validadorDistr = 1  # limite 6 inicia em 1 e incrementa
caracteresInvDistr = 0
blocosInvDistr = 0  # limite = numBlocosAdicionar
contadorLenBased = 0
caracteresMsgCripto = 0  # caso dê falso
mensagemCriptoBase = ''
lesBlocos = numBlocosAdicionar - blocosInvDistr
listaValidadores = [bloco1, bloco2, bloco3, bloco4, bloco5, bloco6]


def criadorBlocoInvalido(tamanho):
    return np.random.randint(65, 90, tamanho)


def charInvPicker():
    resultado = np.random.choice(arrayAnulador, 1)
    return resultado


def escolhedorVF():
    arrayVF = np.array([True, False])
    resultado = np.random.choice(arrayVF, 1)
    print('v ou f = ', resultado)
    return resultado


def escolhedorInserir():
    global blocosInvDistr
    global caracteresInvDistr
    global validadorDistr
    global caracteresMsgCripto
    global contadorLenBased
    global mensagemCriptoBase
    global charAAdicionar
    global lesBlocos
    print('entrei---')
    print('caracteresMsgCripto: ', caracteresMsgCripto)
    print('lenmsgconvert: ', len(mensagemConvertida))
    print('char a adicionar: ', charAAdicionar)
    print('validador ditr: ', validadorDistr)
    print('sai---')

    if caracteresMsgCripto == len(mensagemConvertida) and charAAdicionar != 0 and validadorDistr <= 7:
        # aqui a ideia é que quando eu distribuir todos os caracteres da mensagem convertida, só vamos ter true
        arrayVF = np.array([True])
    elif caracteresMsgCripto <= len(mensagemConvertida) and charAAdicionar == 0 and validadorDistr == 7:
        arrayVF = np.array([False])
    else:
        # aqui pode dar true ou false
        arrayVF = np.array([True, False])
    resultado = np.random.choice(arrayVF, 1)

    # situação = obrigado injetar todas as cadeias de validação e todos os char da msg
    # eu paro quando não tiver nenhum char a adicionar e quando já tiver adicionado tudo

    if charAAdicionar == 0 and (caracteresMsgCripto == len(mensagemConvertida)) and validadorDistr == 7:
        print('cheguei ao fim')
    else:
        if resultado:
            # sabemos que o limite para o 1 vem da quantidade de caracteres limite
            # sabemos que o limite para o 2 vem da quantidade de blocos e caracteres limite
            # sabemos que o limite para o 3 vem da quantidade de blocos validadores (1 a 6)
            # sabemos que o limite para o False vem da quantidade de caracteres da mensagem em si
            arrayPossibilidades = np.array([1, 2, 3])
            escolhido = np.random.choice(arrayPossibilidades, 1)
            print('---')
            print('opção escolhida: ', escolhido)
            print('---')

            if int(escolhido) == 1 and charAAdicionar != 0:
                # aqui vou colocar um caracter invalido
                charFake = np.random.choice(arrayCaracFakeFinal, 1)
                mensagemCriptoBase = mensagemCriptoBase + chr(int(charFake[0]))
                caracteresInvDistr += 1
                charAAdicionar -= 1

            elif int(escolhido) == 2 and charAAdicionar != 0:
                # aqui vou colocar um bloco invalido
                # primeiro tenho que saber quantos caracteres vão ser usados no bloco
                print('charAAdicionar: ', charAAdicionar)
                print('lesBlocos: ', lesBlocos)

                if lesBlocos <= 0:
                    qtdcharadd = rd.randint(1, abs(charAAdicionar))
                else:
                    qtdcharadd = rd.randint(1, abs(ceil(charAAdicionar / lesBlocos)))

                print('random selected: ', qtdcharadd)
                # agora que eu sei a quantidade de char a add, eu mando pro gerador
                arrayPraConverter = criadorBlocoInvalido(qtdcharadd)
                print('array pra add: ', arrayPraConverter)

                # o retorno é uma array, então vem o for e injeta
                tempString = ''
                for xuxu in arrayPraConverter:
                    tempString = tempString + chr(xuxu)

                print('tempString: ', tempString)
                # agora eu finalizo a montagem inserindo a abertura e fechamento

                tempString = chr(int(charInvPicker())) + tempString + chr(int(charInvPicker()))

                print('tempStringfinal: ', tempString)

                mensagemCriptoBase = mensagemCriptoBase + tempString

                blocosInvDistr += 1
                charAAdicionar -= qtdcharadd
                lesBlocos = numBlocosAdicionar - blocosInvDistr

            elif int(escolhido) == 3 and validadorDistr != 7:
                # nesse caso temos que distribuir 6 blocos ao longo da mensagem
                # tenho que checar a condição
                # se validadorDistr > 6 não faz nada
                # aqui vou inserir um bloco de validação

                if validadorDistr <= 6:
                    mensagemCriptoBase = mensagemCriptoBase + listaValidadores[validadorDistr - 1]
                    validadorDistr += 1
                else:
                    print('não distribui nada')
            escolhedorInserir()
        else:
            # nesse caso é falso, então eu manipulo para inserir caracter
            print('escolhido: [4]')
            print('caracteresmsgcripto: ', caracteresMsgCripto)
            mensagemCriptoBase = mensagemCriptoBase + mensagemConvertida[caracteresMsgCripto]
            caracteresMsgCripto += 1
            escolhedorInserir()


# primeor passo inicio o loop
# tenho que ver qual a informação vai entrar
# se verdadeiro, tenho que escolher entre 1, 2, 3
# se falso, injeto um caracter da mensagem
# após isso tenho que alterar o contador, para que recalcule o range e passe para o próximo loop
# os testes são recursivos dentro do loop
# e só quando dá falso sai, mas tenho que verificar as diversas variáveis para que elas entrem....


print('----------')
print('----------')
print('----------')
print(charAAdicionar)

escolhedorInserir()

print('mensagemConvert: ', mensagemConvertida)
print('len mensagemConvert: ', len(mensagemConvertida))
print('validadorDistr: ', validadorDistr)
print('caracteresInvDistr: ', caracteresInvDistr)
print('blocosInvDistr: ', blocosInvDistr)
print('contadorLenBased: ', contadorLenBased)
print('caracteresMsgCripto: ', caracteresMsgCripto)
print('mensagemCriptoBaso: ', mensagemCriptoBase)
print('listaValidadores: ', listaValidadores)
print('tamanho Base: ', len(mensagemCriptoBase))

print('----------')
print('----------')
print('----------')

# o resultado final é

print('Resultado final: ', cadeiaAbertura + mensagemCriptoBase + cadeiaFechamento)

novaArray = []
for x in vetorASCII:
    novaArray.append(int(x))

print('nova ', novaArray)

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([10, 20, 30, 40])

# no axis provided, array elements will be flattened
arr_flat = np.append(arr1, arr2)

print(arr_flat)  # [ 1  2  3  4 10 20 30 40]

xi = random.rand()

print(xi)

# O resultado será uma lista com seis números aleatórios, entre 0 e 100.
xa = random.randint(100, size=(6))

# o resultado será uma lista com a quantidade de números informada.
print(xa)

xo = random.rand(10)

print(xo)

tu = random.choice([2, 4, 6, 9, 12])

print(tu)

# devo converter toda a mensagem em uppercase (pra facilitar minha vida)
# preciso contar a quantidade de caracteres que tem a mensagem
# base mínima = 100 - len(mensagem)
# o resultado será o tamanho da mensagem criptografada
# caso o número seja negativo, não sera necessário inserir caracteres a mais para completar a mensagem
# o segundo caracter vai definir aonde está o início da lógica para obter chave de unixtime
# a chave de unix time usando 7 digitos a partir do segundo
# exemplo - 16273488 -> a chave unix é 6273488
# definição de caracteres fantasmas e válidos
# base o numero de pesquisa unix vamos descobrir a logica de caracteres válidos
# existem 38 caracteres especiais possiveis de serem utilizados, mas o segundo numero vai ajustar quais deles são fantasmas e quais deles são válidos
# o caracter válido deverá ser convertido em ascii (int) e o último digito dele será onde está o unixtime
# exemplo caracter ¢ - transformando para int temos 162 --- logo o segundo caracter após o caracter especial válido vai ter um digito do unix time....
# no caso da chave unix time ser 6273488
# teriamos uma frase do tipo = $gsdnv&srt¢h6htyj%hgjf - vemos o caracter ¢ e dois caracteres depois o 6 que é o primeiro numero da chave unix
# uma vez recuperado o unix time nos seus 7 dígitos, todos os caracteres especiais são descartados junto com os numeros unix
# os numeros unix formarão uma array [6,2,7,3,4,8,8]
# todos os caracteres normais serão convertidos em uma tabela de A a Z + espaços + letras especiais a essa tabela será arbitrado um numero inteiro para cada letra
# exemplo a = 1, b = 2, c = 3 .... A=254, B=255 (case sensitive)
# os numeros no array unixtime representam subidas e descidas nessa tabela de conversão
# exemplo na tabela a=1, mas o array unixtime tem no index 0 , o numero 6, logo eu somarei 6 ao 1 e usarei o correspondete ao numero 7 para substituit a letra a

# a =1, b=2, c=3, d=4, e=5, f=6, g=7

# logo se a palavra for por exemplo abestado, no início do ciclo de conversão, a primeira letra "a" será substituída por g, ficando gbestado

# seguindo a lógica, a array de unixtime apresenta o index 1 = ao numero 2, então eu tenho que subrair na tabela base 2

# exemplo
# ô = 342, Ô = 343, a=1, b=2, c=3 ....

# nesse caso o b de abestado cai 2 int da tabela, que faria com que
# gbestado, virasse gÔestado...

# e por aí vai
# como o array tem 7 números, o ciclo de sobe desce ficaria:
# index 0 - sobe, index 1 - desce, index 2 - sobe, index 3 - desce, e por aí vai...
# sempre alternando
# lembrando que o espaço entre letras tb seria convetido de acordo com a tabela base.
