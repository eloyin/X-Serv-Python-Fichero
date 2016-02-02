AuxFile = open ("/etc/passwd","r")
PaswdL = AuxFile.read()  # *: read/readline/readlines elementos=linea.split(":")
AuxFile.close

AuxFile = open ("a.txt","w")
AuxFile.write(PaswdL[1])
AuxFile.close

#print PaswdL[0:100]

## Tixer:

AuxFile = open ("/etc/passwd","r")
lineas = AuxFile.readlines()

for linea in lineas:
    lista = linea.split(":")
 #   print lista

print lineas[0]

AuxFile.close

# print con coma al final, no imprime su \n
