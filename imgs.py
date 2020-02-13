from PIL import Image
from string import Template
#Funcion de carga
def cargarImgs(color):
    imgs=[]
    for x in range(0,9):
        t = Template('./src/crop/$name.jpg') #Path de carga
        path = t.substitute(name=x) #Template string
        if(color==False):
            imgs.append(Image.open(path).convert("L"))
        else:
             imgs.append(Image.open(path))
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