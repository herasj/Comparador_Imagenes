from crop import recortar
from list_ops import sumar_subl
from list_ops import restar_l
from list_ops import menor
from list_ops import mueve
from list_ops import centrar
from imgs import cargarImgs
from borders import getborders
from PIL import Image
from string import Template
import copy

gridlist=[[],[],[]]
centro=[]
ady=[] #[label,up,down,left,right]
targets=[0,1,2,3,4,5,6,7,8] #Lista de objetivos

#recortar() # Llamar funcion de recortado

imgs=cargarImgs(False) #Carga todas las imagenes en /src/crop
imgscolor=cargarImgs(True) #Carga las imagenes con colores
dim=imgs[0].height; #Altura de las imagenes

#Buscar el centro
for x in range (0,9):
    if(len(centro)!=5):
        centro.clear()
    else:
        print("Se rompió el for")
        break
    centro.append(copy.deepcopy(x)) #Añadir el nodo a comparar
    target=imgs[x].load()
    target_b=getborders(target,dim)
    ady.clear()
    for y in range(0,9):
        if (y!=x):
            test=imgs[y].load()
            test_b=getborders(test,dim)
            resta = restar_l(target_b,test_b,dim)
            suma=sumar_subl(resta,dim)
            nro_menor=menor(suma)
            if (nro_menor[0]<=1500):
                centro.append([nro_menor[1],y])
 
 
print('El centro es: ',centro)
gridlist=centrar(gridlist,centro)

#Acomodar casillas restantes
for x in range (0,9):
    target=imgs[x].load()
    target_b=getborders(target,dim)
    ady.clear()
    for y in range(0,9):
        if (y!=x):
            test=imgs[y].load()
            test_b=getborders(test,dim)
            resta = restar_l(target_b,test_b,dim)
            suma=sumar_subl(resta,dim)
            nro_menor=menor(suma)
            # print('Suma de cada diferencia target = ',str(x),' y= ',str(y),' ',suma)
            if (nro_menor[0]<=1600):
                gridlist=mueve(gridlist,x,y,nro_menor[1])

#Imprimir resultado
print("grid final")
print(gridlist)

contador=0
for x in range(0,len(gridlist)):
    for y in range(0,len(gridlist)):
        t = Template('./src/orden/$name.jpg') #Path de guardado
        path = t.substitute(name=contador) #Template string
        imgscolor[gridlist[x][y]].save(path) #Guardar ordenados
        contador=contador+1
