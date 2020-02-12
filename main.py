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

imgs=cargarImgs()
temp1=imgs[4].load()
temp2=imgs[7].load()
b=getborders(temp1,166)
b2=getborders(temp2,166)
print("(Diferencia de bordes) Imagen numero 1")
print(b)
print('')
print("(Diferencia de bordes) Imagen numero 2")
print(b2)
print("Suma de cada diferencia (la menor es el borde)")
resultado = restar_l(b,b2,166)
print(sumar_subl(resultado,166))
