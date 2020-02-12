from crop import recortar
from PIL import Image, ImageChops
from string import Template
import numpy as np
#Funcion de carga
def cargarImgs():
    imgs=[]
    for x in range(0,9):
        t = Template('./src/crop/$name.jpg') #Path de carga
        path = t.substitute(name=x) #Template string
        imgs.append(Image.open(path).convert("L"))
    return imgs

def mostrar(img1,img2,h):
    b1=[]
    b2=[]

    for x in range (0, h):
        b1.append(img1[h-1,x]) #[X,Y]

    for y in range (0, h):
        b2.append(img2[0,y]) #[X,Y]
    resta=[]
    for z in range(0,len(b1)):
        resta.append(abs(b1[z]-b2[z]))
    
    print("Borde 1")
    print(b1)
    print("Borde 2")
    print(b2)
    print("Resta de bordes")
    print(resta)

def getborders(img,h):
    bordes=[] #Lista que contiene las demás
    up=[]
    left=[]
    right=[]
    down=[]

    #Bordes
    for x in range (0, h):
        up.append(img[x,0]) #[X,Y]  Superior
        down.append(img[x,h-1]) #Inferior
        left.append(img[0,x]) #Izquierda
        right.append(img[h-1,x]) #Derecha

    #Estructura de bordes [[up],[down],[left],[right]]
    bordes.append(up);bordes.append(down);bordes.append(left);bordes.append(right)
    return bordes
recortar() # Llamar funcion de recortado

imgs=cargarImgs()
tempi=imgs[0].load()
b=getborders(tempi,166)
print(b)

# diff = ImageChops.difference(img1, img2)

# diferencia = diff.getbox()
# print (diferencia)
