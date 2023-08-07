def numIzq(j,inputargf):
    num1 = ""
    posInicial = 0
    salirBucle = False
    cont1 = j - 1
    while ((inputargf[cont1].isnumeric() == True or inputargf[cont1] == "." or inputargf[cont1] == "-") and salirBucle == False):
        posInicial = cont1
        if (inputargf[cont1] == "-"):
            salirBucle = True
        cont1 = cont1 - 1
    for izq in range(posInicial, j):
        num1 = num1 + inputargf[izq]
    return [num1,posInicial]

def numDer(j,inputargf):
    num2 = ""
    posFinal = 0
    cont2 = j + 1
    if (inputargf[j + 1] == "-"):
        negativoInicial = True
    else:
        negativoInicial = False
    while (inputargf[cont2].isnumeric() == True or inputargf[cont2] == "." or negativoInicial == True):
        negativoInicial = False
        posFinal = cont2
        cont2 = cont2 + 1
    for der in range(j + 1, posFinal + 1):
        num2 = num2 + inputargf[der]
    return [num2,posFinal]

def numIzqEsp(j,inputargf):
    num1 = ""
    entrarBucle = True
    salirBucle = False
    revisarCaracter = True
    posInicial = 0
    cont1 = j - 1
    if (j - 1 == 0):
        entrarBucle = False
        posInicial = j - 1
    if (entrarBucle == True):
        while ((inputargf[cont1].isnumeric() == True or inputargf[cont1] == "." or inputargf[cont1] == "-") and salirBucle == False):
            posInicial = cont1
            if (inputargf[cont1] == "-"):
                salirBucle = True
                revisarCaracter = False
            cont1 = cont1 - 1
            if (cont1 == 0 and revisarCaracter == True):
                salirBucle = True
                posInicial = cont1
    for izq in range(posInicial, j):
        num1 = num1 + inputargf[izq]
    return [num1,posInicial]

def numDerEsp(j,inputargf):
    num2 = ""
    entrarBucle = True
    salirBucle = False
    posFinal = 0
    cont2 = j + 1
    if (inputargf[j + 1] == "-"):
        negativoInicial = True
    else:
        negativoInicial = False
    if (j + 1 == len(inputargf) - 1):
        entrarBucle = False
        posFinal = j + 1
    if (entrarBucle == True):
        while ((inputargf[cont2].isnumeric() == True or inputargf[cont2] == "." or negativoInicial == True) and salirBucle == False):
            negativoInicial = False
            posFinal = cont2
            cont2 = cont2 + 1
            if (cont2 == len(inputargf) - 1):
                salirBucle = True
                posFinal = cont2
    for der in range(j + 1, posFinal + 1):
        num2 = num2 + inputargf[der]
    return [num2,posFinal]

par = []
loop = 0
par0 = -1
par1 = -1
sustituto1 = ""
sustituto2 = ""
multYdiv = 1
sumYres = 1
editable = 1
borrarNeg = False
cicloN = 0
numPar = 0
operadores = 1
numFinalNegativo = 0
# inputarg = "11+2/7.5-100*4/1.22*(1-1/-2)/2*(-31.22-5/(1+3.1))"
# inputarg = "1/2-0.5-(1-2),1+(3.5/2),1,2+1"
# inputarg = "1-2*(1/-5)"
inputarg = "1+(5/2.01-(1-7.111111))"
inputarg = input("Dime que quieres calcular: ")
inputargf = inputarg
while (operadores >= 1 and numFinalNegativo == 0):
    operadores = 0
    editable = 1
    multYdiv = 1
    sumYres = 1
    for i in range(len(inputargf)):
        if (cicloN == 0):
            if (inputarg[i] == "("):
                numPar = numPar + 1
        if (editable == 1):
            if (inputargf[i] == "(" or inputargf[i] == "*" or inputargf[i] == "/" or inputargf[i] == "+" or inputargf[i] == "-" or inputargf[i] == ")"):
                operadores = operadores + 1
            if (inputargf[i] == "("):
                par0 = i
            elif (inputargf[i] == ")"):
                par1 = i
        if (par0 != -1 and par1 != -1 and editable == 1):
            while (multYdiv >=1):
                multYdiv = 0
                sustituto1 = ""
                par1nuevoEncontrado = False
                for j in range(par0 + 1, par1):
                    if (inputargf[j] == ")"):
                        par1 = j
                        par1nuevoEncontrado = True
                    if (inputargf[j] == "*" and multYdiv == 0):
                        num1 = numIzq(j,inputargf)
                        num2 = numDer(j,inputargf)
                        sustituto1 = float(num1[0]) * float(num2[0])
                        multYdiv = multYdiv + 1
                        # print(sustituto1)
                    elif (inputargf[j] == "/" and multYdiv == 0):
                        num1 = numIzq(j,inputargf)
                        num2 = numDer(j,inputargf)
                        sustituto1 = float(num1[0]) / float(num2[0])
                        multYdiv = multYdiv + 1
                        # print(sustituto1)

                # if (multYdiv >=1):
                #     if (float(sustituto1) >= 0):
                #         adicionSuma = "+"
                #     else:
                #         adicionSuma = ""
                if (sustituto1 != ""):
                    if (num1[0][0] == "-" and float(num1[0]) == 0):
                        ceroNegativo = True
                    else:
                        ceroNegativo = False
                    if (float(num1[0]) >= 0 and float(num2[0]) < 0 and ceroNegativo == False and num1[1] != par0 + 1):
                        inputargf = inputargf[0:num1[1]] + str(sustituto1) + inputargf[num2[1] + 1:len(inputargf)]
                        inputargf = list(inputargf)
                        inputargf.pop(num1[1] - 1)
                        inputargf = "".join(inputargf)
                    elif (float(num1[0]) <= 0 and float(num2[0]) < 0 and num1[1] != par0 + 1):
                        sustituto1 = "+" + str(sustituto1)
                        inputargf = inputargf[0:num1[1]] + str(sustituto1) + inputargf[num2[1] + 1:len(inputargf)]
                    else:
                        inputargf = inputargf[0:num1[1]] + str(sustituto1) + inputargf[num2[1] + 1:len(inputargf)]
                loop = par0
                while (par1nuevoEncontrado == False):
                    if (inputargf[loop] == ")"):
                        par1 = loop
                        par1nuevoEncontrado = True
                    loop = loop + 1
            while (sumYres >= 1):
                sumYres = 0
                sustituto2 = ""
                contador = 1
                par1nuevoEncontrado = False
                for k in range(par0 + 1, par1):
                    if (inputargf[k] == ")"):
                        par1 = k
                        par1nuevoEncontrado = True
                    if (inputargf[k] == "+" and sumYres == 0):
                        num1 = numIzq(k,inputargf)
                        num2 = numDer(k,inputargf)
                        sustituto2 = float(num1[0]) + float(num2[0])
                        sumYres = sumYres + 1
                        # print(sustituto2)
                    elif (inputargf[k] == "-" and sumYres == 0 and contador > 1):
                        num1 = numIzq(k,inputargf)
                        num2 = numDer(k,inputargf)
                        sustituto2 = float(num1[0]) - float(num2[0])
                        sumYres = sumYres + 1
                        # print(sustituto2)
                    contador = contador + 1
                # if (sumYres >= 1):
                #     if (float(sustituto2) >= 0):
                #         adicionSuma = "+"
                #     else:
                #         adicionSuma = ""
                if (sustituto2 != ""):
                    inputargf = inputargf[0:num1[1]] + str(sustituto2) + inputargf[num2[1] + 1:len(inputargf)]
                loop = par0
                while (par1nuevoEncontrado == False):
                    if (inputargf[loop] == ")"):
                        par1 = loop
                        par1nuevoEncontrado = True
                    loop = loop + 1
            inputargf= list(inputargf)
            if (inputargf[par0 + 1] == "-" and inputargf[par0 - 1] != inputargf[len(inputargf) - 1]):
                if (inputargf[par0 - 1] == "-"):
                    inputargf[par0 - 1] = "+"
                    borrarNeg = True
                elif (inputargf[par0 - 1] == "+"):
                    inputargf[par0 - 1] = "-"
                    borrarNeg = True
            else:
                borrarNeg = False
            inputargf.pop(par1)
            if (borrarNeg == True):
                inputargf.pop(par0 + 1)
            inputargf.pop(par0)
            if (inputargf[0] == "+"):
                inputargf.pop(0)
            inputargf = "".join(inputargf)
            par0 = -1
            par1 = -1
            editable = 0

        if (editable == 1 and cicloN >= numPar and cicloN != 0):
            while (multYdiv >=1):
                multYdiv = 0
                sustituto1 = ""
                for j in range(len(inputargf)):
                    if (inputargf[j] == "*" and multYdiv == 0):
                        num1 = numIzqEsp(j, inputargf)
                        num2 = numDerEsp(j, inputargf)
                        sustituto1 = float(num1[0]) * float(num2[0])
                        # print(sustituto1)
                        multYdiv = multYdiv + 1
                    elif (inputargf[j] == "/" and multYdiv == 0):
                        num1 = numIzqEsp(j, inputargf)
                        num2 = numDerEsp(j, inputargf)
                        sustituto1 = float(num1[0]) / float(num2[0])
                        # print(sustituto1)
                        multYdiv = multYdiv + 1
                if (sustituto1 != ""):
                    if (num1[1] == 0):
                        inputargf = str(sustituto1) + inputargf[num2[1] + 1:len(inputargf)]
                    else:
                        if (num1[0][0] == "-" and float(num1[0]) == 0):
                            ceroNegativo = True
                        else:
                            ceroNegativo = False
                        if (float(num1[0]) >= 0 and float(num2[0]) < 0 and ceroNegativo == False):
                            inputargf = inputargf[0:num1[1]] + str(sustituto1) + inputargf[num2[1] + 1:len(inputargf)]
                            inputargf = list(inputargf)
                            inputargf.pop(num1[1] - 1)
                            inputargf = "".join(inputargf)
                        elif (float(num1[0]) <= 0 and float(num2[0]) < 0):
                            sustituto1 = "+" + str(sustituto1)
                            inputargf = inputargf[0:num1[1]] + str(sustituto1) + inputargf[num2[1] + 1:len(inputargf)]
                        else:
                            inputargf = inputargf[0:num1[1]] + str(sustituto1) + inputargf[num2[1] + 1:len(inputargf)]
            while (sumYres >= 1):
                sumYres = 0
                sustituto2 = ""
                contador = 1
                for k in range(len(inputargf)):
                    if (inputargf[k] == "+" and sumYres == 0):
                        num1 = numIzqEsp(k, inputargf)
                        num2 = numDerEsp(k, inputargf)
                        sustituto2 = float(num1[0]) + float(num2[0])
                        # print(sustituto2)
                        sumYres = sumYres + 1
                    elif (inputargf[k] == "-" and sumYres == 0 and contador > 1):
                        num1 = numIzqEsp(k, inputargf)
                        num2 = numDerEsp(k, inputargf)
                        sustituto2 = float(num1[0]) - float(num2[0])
                        # print(sustituto2)
                        sumYres = sumYres + 1
                    contador = contador + 1
                if (sustituto2 != ""):
                    if (num1[1] == 0):
                        inputargf = str(sustituto2) + inputargf[num2[1] + 1:len(inputargf)]
                    else:
                        inputargf = inputargf[0:num1[1]] + str(sustituto2) + inputargf[num2[1] + 1:len(inputargf)]
            editable = 0
    if (operadores == 1 and inputargf[0] == "-"):
        numFinalNegativo = 1
        operadores = 0
    cicloN = cicloN + 1
print(inputargf)
# print(-1+3*(2*-6))