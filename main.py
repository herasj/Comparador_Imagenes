from crop import recortar
from list_ops import sumar_subl
from list_ops import restar_l
from imgs import cargarImgs
from borders import getborders
from PIL import Image, ImageChops
from string import Template
import numpy as np
import copy

recortar() # Llamar funcion de recortado

imgs=cargarImgs() #Carga todas las imagenes en /src/crop
dim=imgs[0].height; #Altura de las imagenes
target=imgs[0].load()
target_b=getborders(target,dim)

#Ubicar imagenes adyacentes a 0
for x in range(1,9):
    test=imgs[x].load()
    test_b=getborders(test,dim)
    print("Suma de cada diferencia x= ",x)
    resultado = restar_l(target_b,test_b,dim)
    print(sumar_subl(resultado,dim))
    print('')

# print("(Diferencia de bordes) Imagen numero 1")
# print(b)
# print('')
# print("(Diferencia de bordes) Imagen numero 2")
# print(b2)
# print("Suma de cada diferencia (la menor es el borde)")


