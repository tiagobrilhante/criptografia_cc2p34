import random as rd
from math import ceil

import numpy as np
from numpy import random

# input da mensagem
mensagem = input('\033[0;0m Digite a mensagem: ')

# para demonstração usaremos os seguintes caracteres
# por regra, devemos ter no mínimo 2 caracteres cujos últimos digitos in [0,1,2,3,4,5,6,7,8,9]
arrayCaracteresEspeciais = np.array(
    [ord('╬'), ord('║'), ord('╣'), ord('╦'), ord('╚'), ord('╔'), ord('┤'), ord('▙'), ord('▝'), ord('┌'), ord('┴'),
     ord('│'), ord('¬'), ord('¤'), ord('Ð'), ord('█'), ord('▄'), ord('▀'), ord('■'), ord('░'), ord('▒'), ord('▓'),
     ord('ß'), ord('þ'), ord('¶'), ord('Þ'), ord('ý'), ord('¢'), ord('£'), ord('ø'), ord('Ø'), ord('®'), ord('æ'),
     ord('Æ'), ord('×'), ord('«'), ord('»')])

if ord(mensagem[0]) in arrayCaracteresEspeciais:
    print('Iniciando descriptografia.')

    relevantKeyOfuscada = mensagem[1]

    print('relevantKeyOfuscada: ', relevantKeyOfuscada)


    def desofuscaRelevantKey(chaveRelevanteOfuscada):
        if chaveRelevanteOfuscada == 'A':
            return 1
        elif chaveRelevanteOfuscada == 'B':
            return 2
        elif chaveRelevanteOfuscada == 'C':
            return 3
        elif chaveRelevanteOfuscada == 'D':
            return 4
        elif chaveRelevanteOfuscada == 'E':
            return 5
        elif chaveRelevanteOfuscada == 'F':
            return 6
        elif chaveRelevanteOfuscada == 'G':
            return 7
        elif chaveRelevanteOfuscada == 'H':
            return 8
        elif chaveRelevanteOfuscada == 'I':
            return 9
        else:
            return 0


    relevantKey = desofuscaRelevantKey(relevantKeyOfuscada)
    print('relevantKey: ', relevantKey)

    # agora eu defino quais são os caracteres validos e inválidos (pode melhorar isso criando uma função específica)

    # inicio o divisor de pares e impares
    arrayCaracPar = np.array([])
    arrayCaracImpar = np.array([])

    for z in range(37):
        if (z % 2 == 0):
            arrayCaracPar = np.append(arrayCaracPar, arrayCaracteresEspeciais[z])
        else:
            arrayCaracImpar = np.append(arrayCaracImpar, arrayCaracteresEspeciais[z])

    # Se a relevant key for par os caracteres válidos são pares
    # se for impar, os caracteres válidos são impar
    arrayCaracValido = np.array([])
    arrayCaracFake = np.array([])

    if (int(relevantKey) % 2 == 0):
        arrayCaracValido = arrayCaracPar
        arrayCaracFake = arrayCaracImpar
    else:
        arrayCaracValido = arrayCaracImpar
        arrayCaracFake = arrayCaracPar

    # agora que eu sei os válidos e inválidos
    # devo definir quais dos válidos são considerados abertura e fechamento de mensagem para validação
    # deverão ser escolhidos 6 como abridores e fechadores e o resto passa a ser base de chave para o embaralhamento
    # a base para a escolha será a relevant key. o index comeca a partir dela
    arrayValidador = np.array([])
    arrayAnulador = np.array([])

    for u in range(int(relevantKey) + 2, int(relevantKey) + 8):
        arrayValidador = np.append(arrayValidador, arrayCaracValido[u])
        arrayAnulador = np.append(arrayAnulador, arrayCaracFake[u])



    # devo remover da array de invalidos os caracteres anuladores
    arrayCaracFakeFinal = np.array([])
    for cf in arrayCaracFake:
        if cf not in arrayAnulador:
            arrayCaracFakeFinal = np.append(arrayCaracFakeFinal, cf)

    print('--------')
    tempArrayVal = ''
    print('arrayCaracValido: ', arrayCaracValido)
    for a in arrayCaracValido:
        tempArrayVal += chr(int(a))
    print('arr val: ', tempArrayVal)
    print('--------')
    print('--------')
    tempArrayInval = ''
    print('arrayCaracFake: ', arrayCaracFake)
    for a in arrayCaracFake:
        tempArrayInval += chr(int(a))
    print('arr inval: ', tempArrayInval)
    print('--------')

    print('--------')
    tempArrayValida = ''
    print('arrayValidador: ', arrayValidador)
    for a in arrayValidador:
        tempArrayValida += chr(int(a))
    print('arr valida: ', tempArrayValida)
    print('--------')

    print('--------')
    tempArrayAnula = ''
    print('arrayAnulador: ', arrayAnulador)
    for a in arrayAnulador:
        tempArrayAnula += chr(int(a))
    print('arr anula: ', tempArrayAnula)
    print('--------')

    if ord(mensagem[0]) in arrayValidador:
        print('Mensagem válida, prosseguindo...')

        # vou remover da string, a chave de aberture e chave de fechamento
        # chave de abertura = mensagem[0] e mensagem[1]
        # determinar o tamanho total da string:

        print('chave de abertura: ', mensagem[0] + mensagem[1])
        print('chave de fechamento: ', mensagem[len(mensagem) - 1])

        achadorDoFim = ''
        for i in range(len(mensagem) - 2, -1, -1):
            if ord(mensagem[i]) not in arrayValidador:
                achadorDoFim = achadorDoFim + mensagem[i]
            else:
                break

        preparadoNumChar = ''
        for i in range(len(achadorDoFim) - 1, -1, -1):
            preparadoNumChar += achadorDoFim[i]

        # o achador do fim detemina o numero de caracteres da mensagem pcp
        print('achador do fim: ', achadorDoFim)
        print('achador do fim arrumado: ', preparadoNumChar)

        numCharMsgFinal = ''
        for n in preparadoNumChar:
            numCharMsgFinal += str(desofuscaRelevantKey(n))

        numCharMsgFinal = int(numCharMsgFinal)
        print('numero de caracteres da mensagem: ', numCharMsgFinal)

        # agora eu posso começar a retirar as coisas da mensagem

        # aqui eu removo os char de abertura
        mensagemtemp = ''
        for ff in range(2, len(mensagem) - 1):
            mensagemtemp += mensagem[ff]

        print('mensagem sem abertura: ', mensagemtemp)

        # ajustando o final
        posicaodoschar = 0
        for i in range(0, len(mensagemtemp)):
            if ord(mensagemtemp[i]) in arrayValidador:
                posicaodoschar = i

        print('posicao char ', posicaodoschar)

        mensagemSemFimEInicio = ''
        for i in range(0, posicaodoschar):
            mensagemSemFimEInicio += mensagemtemp[i]

        print('mensagem sem fim e inicio', mensagemSemFimEInicio)

        # agora eu posso começar a remover os caracteres inválidos

        mensagemSemCaracInvalidos = ''
        qtdcharblocofake = 0
        arraydeposbloco = []
        contadorIndex = 0
        for i in mensagemSemFimEInicio:
            if ord(i) not in arrayCaracFakeFinal:
                mensagemSemCaracInvalidos += i


        print('----- até aqui OK -----')
        print('mensagem sem caract invalidos: ', mensagemSemCaracInvalidos)
        print('----- até aqui OK -----')

        # vou buscar agora os caracteres do bloco anulador
        for i in mensagemSemCaracInvalidos:
            if ord(i) in arrayAnulador:
                qtdcharblocofake += 1
                arraydeposbloco.append(contadorIndex)
            contadorIndex += 1

        print('quantidade de blocos anuladores: ', qtdcharblocofake / 2)
        print('array das posicoes: ', arraydeposbloco)

        arraycompleta = []
        guardadorIndex = 0
        numeroconveniencia = 0

        # separando a array em 2 (index pares e impares)
        arrayBlocosPar = np.array([])
        arrayBlocosImpar = np.array([])

        for z in range(len(arraydeposbloco)):
            if (z % 2 == 0):
                arrayBlocosPar = np.append(arrayBlocosPar, arraydeposbloco[z])
            else:
                arrayBlocosImpar = np.append(arrayBlocosImpar, arraydeposbloco[z])

        for y in range(len(arrayBlocosPar)):
            novorange = arrayBlocosImpar[y] - arrayBlocosPar[y]
            for d in range(int(novorange) + 1):
                arraycompleta.append(int(arrayBlocosPar[y] + d))

        print('arraycompleta: ', arraycompleta)
        print('array par: ', arrayBlocosPar)
        print('array impar: ', arrayBlocosImpar)

        mensagemSemBlocosInvalidos = ''

        for a in range(len(mensagemSemCaracInvalidos)):
            if a not in arraycompleta:
                mensagemSemBlocosInvalidos += mensagemSemCaracInvalidos[a]

        print('mensagem sem caract invalidos: ', mensagemSemCaracInvalidos)
        print('mensagem sem blocos: ', mensagemSemBlocosInvalidos)

        arrayBrutaRemoveValida = []
        arrayChaveRandom = ''
        arrayListaIntervalos = []

        for f in range(len(mensagemSemBlocosInvalidos)):
            if ord(mensagemSemBlocosInvalidos[f]) in arrayCaracValido:
                print('char original: ', mensagemSemBlocosInvalidos[f])
                print('charConvertido: ', ord(mensagemSemBlocosInvalidos[f]))
                rawRand = str(ord(mensagemSemBlocosInvalidos[f]))
                print('pedacoRandom: ', rawRand[len(rawRand) - 1])
                arrayChaveRandom += str(rawRand[len(rawRand) - 1])
                print('posicao no array: ', f)
                arrayListaIntervalos.append(int(f))
                arrayListaIntervalos.append(int(f) + 1 + int(rawRand[len(rawRand) - 1]))

        arrayChaveRandom = arrayChaveRandom + str(relevantKey)
        print('---------')
        print('chave Randomica: ', arrayChaveRandom)
        print('chave Randomica: ', arrayChaveRandom)
        print('---------')
        print('arrayListaIntervalos: ', arrayListaIntervalos)

        #tenho que remover agora as chaves de autenticação....

        # separando a array em 2 (index pares e impares)
        arrayBlocosParVal = np.array([])
        arrayBlocosImparVal = np.array([])
        arrayCompletaValidadores = []

        for z in range(len(arrayListaIntervalos)):
            if (z % 2 == 0):
                arrayBlocosParVal = np.append(arrayBlocosParVal, arrayListaIntervalos[z])
            else:
                arrayBlocosImparVal = np.append(arrayBlocosImparVal, arrayListaIntervalos[z])

        for y in range(len(arrayBlocosParVal)):
            novorange = arrayBlocosImparVal[y] - arrayBlocosParVal[y]
            for d in range(int(novorange) + 1):
                arrayCompletaValidadores.append(int(arrayBlocosParVal[y] + d))

        print('arrayCompletaValidadores: ', arrayCompletaValidadores)
        #agora eu posso remover a cadeia de validção

        mensagemSemBlocosValidadores = ''

        for a in range(len(mensagemSemBlocosInvalidos)):
            if a not in arrayCompletaValidadores:
                mensagemSemBlocosValidadores += mensagemSemBlocosInvalidos[a]

        print('mensagem pronta para descripto: ', mensagemSemBlocosValidadores)
        #converto para ascii

        arrayPraDescripto = []
        for w in mensagemSemBlocosValidadores:
            arrayPraDescripto.append(ord(w))

        print('array para descripto', arrayPraDescripto)

        alternadorDeSinal = 0
        counter = 0
        arrayDescriptoPronta = []
        for x in arrayPraDescripto:
            if (len(arrayPraDescripto) < 7):
                if alternadorDeSinal % 2 == 0:
                    arrayDescriptoPronta.append(x - int(arrayChaveRandom[counter]))
                else:
                    arrayDescriptoPronta.append(x + int(arrayChaveRandom[counter]))
                counter +=1
                alternadorDeSinal += 1
            else:
                if alternadorDeSinal % 2 == 0:
                    arrayDescriptoPronta.append(x - int(arrayChaveRandom[counter]))
                else:
                    arrayDescriptoPronta.append(x + int(arrayChaveRandom[counter]))
                counter += 1
                alternadorDeSinal += 1
                if counter == 7:
                    counter = 0
                    alternadorDeSinal = 0


        print(arrayDescriptoPronta)

        mensagemDescriptografada = ''
        for r in arrayDescriptoPronta:
            mensagemDescriptografada += chr(int(r))

        print('mensagem descriptografada: ', mensagemDescriptografada)



    else:
        print('mensagem inválida')
        print('Descriptografia Interrompida')


else:
    print('Iniciando criptografia.')
    # converto tudo pra maiuscula
    mensagem = mensagem.upper()

    # ajustando quantidades a adicionar (char para ofuscamento)
    if len(mensagem) < 100:

        if len(mensagem) < 10:
            charAAdicionar = ceil(100 - len(mensagem))
        elif 50 > len(mensagem) >= 10:
            charAAdicionar = 60
        else:
            charAAdicionar = 80
    else:
        charAAdicionar = ceil(len(mensagem) / 3)

    # aqui eu gero a chave randomica que será a base dos saltos de embaralhamento
    randomKey = str(rd.randrange(1000000, 9999999, 7))
    print('random Key', randomKey)
    # a chave relevante é o último digito da random key
    relevantKey = randomKey[6]

    # inicio o divisor de pares e impares
    arrayCaracPar = np.array([])
    arrayCaracImpar = np.array([])

    for z in range(37):
        if (z % 2 == 0):
            arrayCaracPar = np.append(arrayCaracPar, arrayCaracteresEspeciais[z])
        else:
            arrayCaracImpar = np.append(arrayCaracImpar, arrayCaracteresEspeciais[z])

    # Se a relevant key for par os caracteres válidos são pares
    # se for impar, os caracteres válidos são impar
    arrayCaracValido = np.array([])
    arrayCaracFake = np.array([])

    if (int(relevantKey) % 2 == 0):
        arrayCaracValido = arrayCaracPar
        arrayCaracFake = arrayCaracImpar
    else:
        arrayCaracValido = arrayCaracImpar
        arrayCaracFake = arrayCaracPar

    # agora que eu sei os válidos e inválidos
    # devo definir quais dos válidos são considerados abertura e fechamento de mensagem para validação
    # deverão ser escolhidos 6 como abridores e fechadores e o resto passa a ser base de chave para o embaralhamento
    # a base para a escolha será a relevant key. o index comeca a partir dela
    arrayValidador = np.array([])
    arrayAnulador = np.array([])

    for u in range(int(relevantKey) + 2, int(relevantKey) + 8):
        arrayValidador = np.append(arrayValidador, arrayCaracValido[u])
        arrayAnulador = np.append(arrayAnulador, arrayCaracFake[u])

    # devo remover da array de invalidos os caracteres anuladores
    arrayCaracFakeFinal = np.array([])
    for cf in arrayCaracFake:
        if cf not in arrayAnulador:
            arrayCaracFakeFinal = np.append(arrayCaracFakeFinal, cf)

    tempVal = ''
    print('------')
    print('arrayCaracValido', arrayCaracValido)
    for i in arrayCaracValido:
        tempVal += chr(int(i))
    print('tempval: ', tempVal)
    print('------')

    print('------')

    tempFake = ''
    print('arrayCaracFake', arrayCaracFake)
    for i in arrayCaracFake:
        tempFake += chr(int(i))
    print('tempFake: ', tempFake)

    print('------')
    print('------')
    tempValidador = ''
    print('arrayValidador', arrayValidador)
    for i in arrayValidador:
        tempValidador += chr(int(i))
    print('tempValidador: ', tempValidador)

    print('------')
    tempAnulador = ''
    print('arrayAnulador: ', arrayAnulador)
    for i in arrayAnulador:
        tempAnulador += chr(int(i))
    print('tempAnulador: ', tempAnulador)

    print('------')

    # agora eu sei quais são os validadores de chave e os anuladores
    # em resumo temos o seguinte
    # os validadores devem estar no início e no final da frase
    # pode ser qualquer um desses

    # os anuladores são usados para dificultar a descriptografação
    # em resumo, tudo o que estiver entre esses caracteres deve ser descartado

    # o primeiro caracter da mensagem é o validador de abertura... o segundo caracter é a chave relevante (alterada por uma tabela de correlação)
    # a partir daí, usaremos a cadeia de caracteres válidos para disseminar o restante dos numeros que compoem a randomkey

    # função para ofuscar digitos importantes para validação
    # essa é uma versão de demonstração
    # para a versão final usar aleatoriedade e array
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


    # o resto agora vai funcionar da seguinte forma
    # eu tenho o tamanho da mensagem no len, e sei quantos caracteres eu preciso usar para ajustar a mensagem
    # a var charAAdicionar fala isso
    # a ideia é criar uma cadeia de 6 digitos para embaralhar o randomKey restante
    # tudo se baseia nos caracteres em ascii o index da randomkey, excluido-se o ultimo, já que ele é a relevantKey

    # essa função recebe um digito da randomKey e entrega qual será o bloco escolhido para enviar o mesmo de forma ofuscada
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

    # agora vou inciar a montagem simples da array que vai espalhar a unix key
    arrayRKChar = np.array([])
    for k in randomKey:
        castChave = int(k)
        castChar = int(retornadorEspecial(k)[0])

        arrayRKChar = np.append(arrayRKChar, [castChave, castChar]).astype(int)

    # exemplo de output arrayRKChar:  [   4 9484    3 9553    8  198    8  248    5 9625    7 9617    3 9553]
    # isso mostra toda a cadeia de convesão de caracteres, sendo que os dois ultimos index devem ser removidos
    # primeiro grupo- index: 0 e 1
    # segundo grupo- index: 2 e 3
    # terceiro grupo- index: 4 e 5
    # quarto grupo- index: 6 e 7
    # quinto grupo- index: 8 e 9
    # sexto grupo- index: 10 e 11

    # declarando a array que vai receber a mensagem convertida em ASCII
    vetorASCII = np.array([])

    # populando a array
    for n in mensagem:
        vetorASCII = np.append(vetorASCII, int(ord(n)))

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

    # iniciando a variável que vai receber a mensagemOriginal em ASCII já convertida
    vetorConvertido = np.array([])

    # uma mensagem pode ter menos de 7 caracteres ou mais igual 7
    # iniciando a hipotese de mensagens com menos de 7 caracteres
    if (len(mensagem) < 7):
        # descarto os numeros excedentes da randomkey
        # lembrar de alternar soma e subtração (na criptografia)
        # lembrar de alternar subtração e soma (na descriptografia)
        alternadorSinal = 0
        for r in range(len(mensagem)):
            # para criptografar
            if (alternadorSinal % 2 == 0):
                vetorConvertido = np.append(vetorConvertido, int(vetorASCII[r]) + int(randomKey[r]))
            else:
                vetorConvertido = np.append(vetorConvertido, int(vetorASCII[r]) - int(randomKey[r]))
            alternadorSinal += 1

    # iniciando a hipotese de mensagens com mais de 7 caracteres
    # nesse caso haverá ciclo de repetições dentro da randomKey
    # tem que lembrar que para a criptografia, sempre se soma o indice 0
    # para descriptografia sempre se subtrai
    else:
        alternadorSinal = 0
        posicaoIndex = 0
        for r in range(len(mensagem)):
            if posicaoIndex != 6:
                # nesse caso eu entro no loop (lembrando que a randomKey tem 7 digitos)
                # para criprografia eu começo somando
                if (alternadorSinal % 2 == 0):
                    vetorConvertido = np.append(vetorConvertido, int(vetorASCII[r]) + int(randomKey[posicaoIndex]))
                else:
                    vetorConvertido = np.append(vetorConvertido, int(vetorASCII[r]) - int(randomKey[posicaoIndex]))
                alternadorSinal += 1
                # tenho que incrementar o index
                posicaoIndex += 1
            else:
                # nesse caso o index será resetado
                if (alternadorSinal % 2 == 0):
                    vetorConvertido = np.append(vetorConvertido, int(vetorASCII[r]) + int(randomKey[posicaoIndex]))
                else:
                    vetorConvertido = np.append(vetorConvertido, int(vetorASCII[r]) - int(randomKey[posicaoIndex]))
                # tenho que resetar tudo para o reiniciio
                posicaoIndex = 0
                alternadorSinal = 0

    # iniciando a variável que vai receber os caracteres já convertidos
    mensagemConvertida = ''

    for g in vetorConvertido.astype(int):
        mensagemConvertida = mensagemConvertida + str(chr(int(g)))

    # tenho que adicionar agora os blocos de informação falsa
    # com base nos char a adicionar
    # blocos são precedidos e secedidos por caracteres anuladores

    if len(mensagem) <= 100:
        numBlocosAdicionar = ceil(charAAdicionar - (charAAdicionar / 2) - (charAAdicionar / 4))
    else:
        numBlocosAdicionar = ceil(len(mensagem) / 10)

    # definindo o char de abertura
    charSpecAbertura = np.random.choice(arrayValidador, 1)
    # definindo o char de fechamento
    charSpecFechamento = np.random.choice(arrayValidador, 1)
    # definindo o char de definição de tamanho de mensagem
    charSpecLimitadorLen = np.random.choice(arrayValidador, 1)

    # criando a cadeia de abertura de mensagem
    cadeiaAbertura = chr(int(charSpecAbertura)) + ajustaChaveRelevante(relevantKey)

    # iniciando a definição de cadeia de fechamento
    tamanhoEmStr = str(len(mensagem))
    cadeiaLenConvertida = ''

    for cadaLetra in tamanhoEmStr:
        cadeiaLenConvertida = cadeiaLenConvertida + str(ajustaChaveRelevante(cadaLetra))

    # ajusto a cadeia de fechamento
    cadeiaFechamento = chr(int(charSpecLimitadorLen)) + str(cadeiaLenConvertida) + chr(int(charSpecFechamento))


    # agora vamos passar a distribuir os caracteres para blocos falsos, caracteres para distribuir a randomKey e caracteres de validação e a própria mensagem em si

    # função para cadeia de autenticação
    def montadorCadeiaAutenticacao(index):
        cadeia = np.random.randint(65, 90, arrayRKChar[index])
        textoCadeia = ''
        for car in cadeia:
            textoCadeia = textoCadeia + chr(car)

        textoCadeia = chr(arrayRKChar[index + 1]) + textoCadeia + ajustaChaveRelevante(arrayRKChar[index])
        return textoCadeia


    # primeiro grupo- index: 0 e 1
    # segundo grupo- index: 2 e 3
    # terceiro grupo- index: 4 e 5
    # quarto grupo- index: 6 e 7
    # quinto grupo- index: 8 e 9
    # sexto grupo- index: 10 e 11

    # montagem dos blocos da randomKey
    bloco1 = montadorCadeiaAutenticacao(0)
    bloco2 = montadorCadeiaAutenticacao(2)
    bloco3 = montadorCadeiaAutenticacao(4)
    bloco4 = montadorCadeiaAutenticacao(6)
    bloco5 = montadorCadeiaAutenticacao(8)
    bloco6 = montadorCadeiaAutenticacao(10)

    print('bloco1: ', bloco1)
    print('bloco2: ', bloco2)
    print('bloco3: ', bloco3)
    print('bloco4: ', bloco4)
    print('bloco5: ', bloco5)
    print('bloco6: ', bloco6)

    # calculo a quantidade de caracteres dentro dos blocos de autenticação que passam a random key
    somaCarAutent = len(bloco1) + len(bloco2) + len(bloco3) + len(bloco4) + len(bloco5) + len(bloco6)

    # ajusto a quantidade de caracteres para adicionar
    charAAdicionar = charAAdicionar - somaCarAutent

    # reduzo tb a qauntidade de blocos a adicionar, já que 6 são os validadores
    numBlocosAdicionar = numBlocosAdicionar - 6

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

    validadorDistr = 1  # limite 6 inicia em 1 e incrementa
    caracteresInvDistr = 0
    blocosInvDistr = 0  # limite = numBlocosAdicionar
    contadorLenBased = 0
    caracteresMsgCripto = 0  # caso dê falso
    mensagemCriptoBase = ''
    lesBlocos = numBlocosAdicionar - blocosInvDistr
    listaValidadores = [bloco1, bloco2, bloco3, bloco4, bloco5, bloco6]


    # cria um bloco de caracteres aleatórios (recebe um tamanho)
    def criadorBlocoInvalido(tamanho):
        return np.random.randint(65, 90, tamanho)


    # pega um caracter anulador aleatório
    def charInvPicker():
        resultado = np.random.choice(arrayAnulador, 1)
        return resultado


    # função que monta a criptografia em si
    def escolhedorInserir():
        global blocosInvDistr
        global caracteresInvDistr
        global validadorDistr
        global caracteresMsgCripto
        global contadorLenBased
        global mensagemCriptoBase
        global charAAdicionar
        global lesBlocos

        # testes básicos
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
            print('Fim dos testes.')
        else:
            if resultado:
                # sabemos que o limite para o 1 vem da quantidade de caracteres limite
                # sabemos que o limite para o 2 vem da quantidade de blocos e caracteres limite
                # sabemos que o limite para o 3 vem da quantidade de blocos validadores (1 a 6)
                # sabemos que o limite para o False vem da quantidade de caracteres da mensagem em si
                arrayPossibilidades = np.array([1, 2, 3])
                escolhido = np.random.choice(arrayPossibilidades, 1)

                if int(escolhido) == 1 and charAAdicionar != 0:
                    # aqui vou colocar um caracter invalido
                    charFake = np.random.choice(arrayCaracFakeFinal, 1)
                    mensagemCriptoBase = mensagemCriptoBase + chr(int(charFake[0]))
                    caracteresInvDistr += 1
                    charAAdicionar -= 1

                elif int(escolhido) == 2 and charAAdicionar != 0:
                    # aqui vou colocar um bloco invalido
                    # primeiro tenho que saber quantos caracteres vão ser usados no bloco

                    if lesBlocos <= 0:
                        qtdcharadd = rd.randint(1, abs(charAAdicionar))
                    else:
                        qtdcharadd = rd.randint(1, abs(ceil(charAAdicionar / lesBlocos)))

                    # agora que eu sei a quantidade de char a add, eu mando pro gerador
                    arrayPraConverter = criadorBlocoInvalido(qtdcharadd)

                    # o retorno é uma array, então vem o for e injeta
                    tempString = ''
                    for xuxu in arrayPraConverter:
                        tempString = tempString + chr(xuxu)

                    # agora eu finalizo a montagem inserindo a abertura e fechamento

                    tempString = chr(int(charInvPicker())) + tempString + chr(int(charInvPicker()))

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

                escolhedorInserir()
            else:
                # nesse caso é falso, então eu manipulo para inserir caracter

                mensagemCriptoBase = mensagemCriptoBase + mensagemConvertida[caracteresMsgCripto]
                caracteresMsgCripto += 1
                escolhedorInserir()


    # chamo a função
    escolhedorInserir()

    print('----------')
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
