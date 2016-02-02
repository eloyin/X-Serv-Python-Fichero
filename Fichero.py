## Tixer:
# *: read/readline/readlines elementos=linea.split(":")

AuxFile = open ("/etc/passwd","r")  # Archivo -> auxiliar
lineas = AuxFile.readlines()        # Auxiliar -> lista[linea, caracter]

print lineas

it=1
for linea in lineas:
    print "Usuario:",str(it)+":", linea.split(":")[0]  # Primer elemento.
    print "Shell: " + linea.split(":")[-1][:-1]    # Fuera el ultimo caracter.
    it+=1

print "\n" + "Numero de usuarios: " + str(len(lineas))



"""
for lineaAux in lineas:             # Recorre cada linea
    linea = lineaAux.split(":")     # Almacena cada elemento de la linea
                                    # separados por ":"
    print linea
    print linea[0]

print "\n" + str(lineas[0][0])      # lineas[linea, caracter]

AuxFile.close
"""
# print con coma al final, no imprime su \n
# print lineas[0:2]
