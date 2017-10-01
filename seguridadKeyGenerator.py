def encripter(key,entrada):
    alfabeto = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    mapa = [["X0","X1","X2","X3","X4"],["X0","X1","X2","X3","X4"],["X0","X1","X2","X3","X4"],["X0","X1","X2","X3","X4"],["X0","X1","X2","X3","X4"]]
    x = 0 # index para la matriz
    y = 0 # index para la matriz
    contador = 0; # contador control para la incersion de la llave en el mapa

    entrada = entrada.replace(" ","") # establece la palabra entreda pro el usuario y le quita los espacios
    key = key.replace(" ","") # establece la llave y le quita los espacios

    entradaArr = listToUpper(list(entrada)) # convierte la entrada en un arreglo y todos los elementos a mayusculas
    keyArr = listToUpper(list(key)) # convierte la llave en un arreglo y todos los elementos a mayusculas

    keyMax = len(keyArr) # guarda la longitud de la llave

    letRest = []
    cntLetRest = 0
    for letra in alfabeto:
        if letra in keyArr:
            # print("letra en alfabeto")
            "letra en alfabeto"
        else:
            # print("letra no en el alfabeto: " + letra)
            letRest.append(letra)
        cntLetRest+=1
    # print("letras restantes")
    # print (letRest)
    cntInsertLetrasRest = 0;
    # iteramos el mapa para poder insertar la llave en el
    for subLis in mapa:
        for letra in subLis:
            # print (mapa[x][y])
            if(contador <  keyMax):
                mapa[x][y] = keyArr[contador] # inserta la llave en el mapa caracter por caracter
                # print (keyArr[contador])
            else:
                mapa[x][y] = letRest[cntInsertLetrasRest]
                cntInsertLetrasRest+=1
            contador += 1
            y+=1
            pass
        y=0
        x+=1
        pass
    x = 0
    y = 0
    palabraEncriptada = ""

    # obtenemos la cadena encriptada
    for i in range(0,(len(entradaArr))):
        for subLis in mapa:
            if entradaArr[i] in subLis:
                palabraEncriptada += str(subLis.index(entradaArr[i])+1)
                # palabraEncriptada += "."
                palabraEncriptada += str(mapa.index(subLis)+1)
                palabraEncriptada += " "
                # indexLetraBusc +=1
            pass
        pass

    print ("#############################################################")
    print ("############ >>>MAPA<<< #####################################")
    print ("#############################################################")
    print("")
    print ("      1    2    3    4    5")
    print ("  1 " + str(mapa[0]))
    print ("  2 " + str(mapa[1]))
    print ("  3 " + str(mapa[2]))
    print ("  4 " + str(mapa[3]))
    print ("  5 " + str(mapa[4]))
    print("")
    print(">> CLAVE: " + key.upper())
    print(">> PALABRA ORIGINAL: " + entrada.upper())
    # print("palabra encriptada: " + palabraEncriptada )
    return palabraEncriptada



def listToUpper(lista):
    listTam = len(lista)
    cnt = 0
    for item in lista:
        lista[cnt] = lista[cnt].upper()
        cnt+=1
    # print ("lista en mayusculas: ")
    # print (lista)
    return lista

print ("ENCRIPTADOR")
print (">> Ingrese la palabara clave: ")
key = input()
print (">> Ingrese la palabra que desea encriptar: ")
entrada = input()
print(">> PALABRA ENCRIPTADA: " + encripter(key,entrada))
