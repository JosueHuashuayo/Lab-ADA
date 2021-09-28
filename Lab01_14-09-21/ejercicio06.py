#Ejercicio 06
def enmarcadoVariable(string, marco):
  #Enmarca un texto segun el numero de marco colocado recibiendo asi dos parametros 
    borde = (len(string) + 2 + marco * 2) * "x" + "\n"
    espacio = "x" + (len(string) + marco * 2) * " " + "x\n"
    altura = espacio * marco
    texto = "x" + marco * " " + string + marco * " " + "x\n"
    print(borde + altura + texto + altura + borde)


palabra = "Programacion Lineal"
marco = 9
enmarcadoVariable(palabra, marco)
