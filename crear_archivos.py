import sys
import io
 
for i in list(range(101, 120)):
    nombre = str(i) + ".txt" # paso el valor de la lista a cadena, me parece más legible
    archivo=open('g:/carpeta_nueva/' + nombre,'w')
    archivo.close()