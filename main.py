from crop import recortar
from list_ops import sumar_subl
from list_ops import restar_l
from list_ops import menor
from list_ops import mueve
from imgs import cargarImgs
from borders import getborders
from PIL import Image
from string import Template
import copy
import numpy as np

grid=np.array([[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]) #Grid de imagenes a construir
gridlist=[[],[],[]]
ady=[] #[label,up,down,left,right]
targets=[0,1,2,3,4,5,6,7,8] #Lista de objetivos

recortar() # Llamar funcion de recortado

imgs=cargarImgs() #Carga todas las imagenes en /src/crop
dim=imgs[0].height; #Altura de las imagenes

#Ubicar imagenes adyacentes a x
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
            #print('Suma de cada diferencia target = ',str(x),' y= ',str(y),' ',suma)
            if (nro_menor[0]<=1500):
                gridlist=mueve(gridlist,x,y,nro_menor[1])
                print("Asi va la grid")
                print(gridlist)

print("grid final")
print(gridlist)