import copy
import numpy as np

def sumar_subl(l,h): #Sumar los valores de cada sublista
    newl=[]
    temp=0
    for x in range(0,4):
        for y in range(0,h):
            temp=temp+l[x][y]
        newl.append(copy.deepcopy(temp))
        temp=0
    return newl

def restar_l(l1,l2,h): #Restar dos listas de bordes
    lista_resta=[] #Lista que contendrá todas las diferencias
    r_l=[] #Almacena la diferencia entre el derecho de l1 y el izquierdo de l2
    u_d=[] #Almacena la diferencia entre el superior de l1 y el inferior de l2
    d_u=[] #Almacena la diferencia entre el inferior de l1 y el superior de l2
    l_r=[] #Almacena la diferencia entre el izquierdo de l1 y el derecho de l2

    for x in range(0,h):
        r_l.append(abs(l1[3][x]-l2[2][x]))
        u_d.append(abs(l1[0][x]-l2[1][x]))
        d_u.append(abs(l1[1][x]-l2[0][x]))
        l_r.append(abs(l1[2][x]-l2[3][x]))

    #Añadir los datos a la lista principal
    lista_resta.append(copy.deepcopy(r_l));
    lista_resta.append(copy.deepcopy(u_d));
    lista_resta.append(copy.deepcopy(d_u));
    lista_resta.append(copy.deepcopy(l_r));

    r_l.clear();u_d.clear();d_u.clear();l_r.clear(); #Eliminar datos innecesarios

    return lista_resta

def menor(list):
    temp=[99999,-1] #[Menor, posición]
    for x in range(0,len(list)):
        if(list[x]<temp[0]):
            temp[0]=list[x]
            temp[1]=x
    return temp

def mueve(grid,n1,n2,mov): 
    #Si el mov es 0, n2 queda a la derecha de n1
    #Si el mov es 1, n2 queda arriba de n1
    #Si el mov es 2, n2 queda debajo de n1
    #Si el mov es 3, n2 queda a la izquierda de n1
    esta1=esta(grid,n1)
    esta2=esta(grid,n2)

    if mov==0: # n1->n2
        if((esta1[0]!=-1) and (esta2[0]==-1)): #Si está n1 pero n2 no
            grid[esta1[0]].insert(esta1[1]+1,n2) #Se inserta n2 al lado de n1
        elif ((esta1[0]==-1) and (esta2[0]!=-1)):#Si està n2 pero no n1
            grid[esta2[0]].insert(esta2[1],n1) #Se inserta n1 a la izq de n2
        elif ((esta1[0]==-1) and (esta2[0]==-1)):#No esta n1 y n2
            #Se intenta añadir n1 y n2 al grid vacio
            if(len(grid[0])<=1):
                grid[0].append(n1);grid[0].append(n2) 
            elif(len(grid[1])<=1):
                grid[1].append(n1);grid[1].append(n2)
            elif(len(grid[2])<=1):
                grid[2].append(n1);grid[2].append(n2)
            else:
                print("ERROR: No hay espacio en el grid para n1= ",n1," y n2= ",n2, "con mov= ",mov)
                print(grid)
    elif mov==1: #n2 arriba de n1
        if((esta1[0]!=-1) and (esta2[0]==-1)): #Si está n1 pero n2 no
            grid[esta1[0]-1].insert(esta1[1],n2) #Se inserta n2 arriba de n1
        elif ((esta1[0]==-1) and (esta2[0]!=-1)):#Si està n2 pero no n1
            grid[esta2[0]+1].insert(esta2[1],n1) #Se inserta n1 debajo de n2
        elif ((esta1[0]==-1) and (esta2[0]==-1)):#No esta n1 y n2
            #Se intenta añadir n1 y n2 al grid vacio
            if((len(grid[0])<=2)and (len(grid[1])<=2)):
                grid[0].append(n2);grid[1].append(n1) 
            elif((len(grid[1])<=2)and (len(grid[2])<=2)):
                grid[1].append(n2);grid[2].append(n1)
            else:
                print("ERROR: No hay espacio en el grid para n1= ",n1," y n2= ",n2, "con mov= ",mov)
                print(grid)
    elif mov==2:#n2 debajo de n1
        if((esta1[0]!=-1) and (esta2[0]==-1)): #Si está n1 pero n2 no
            grid[esta1[0]+1].insert(esta1[1],n2) #Se inserta n2 debajo de n1
        elif ((esta1[0]==-1) and (esta2[0]!=-1)):#Si està n2 pero no n1
            grid[esta2[0]-1].insert(esta2[1],n1) #Se inserta n1 arriba de n2
        elif ((esta1[0]==-1) and (esta2[0]==-1)):#No esta n1 y n2
            #Se intenta añadir n1 y n2 al grid vacio
            if((len(grid[0])<=2)and (len(grid[1])<=2)):
                grid[0].append(n1);grid[1].append(n2) 
            elif((len(grid[1])<=2)and (len(grid[2])<=2)):
                grid[1].append(n1);grid[2].append(n2)
            else:
                print("ERROR: No hay espacio en el grid para n1= ",n1," y n2= ",n2, "con mov= ",mov)
                print(grid)
    else: #n2 izq de n1
        if((esta1[0]!=-1) and (esta2[0]==-1)): #Si está n1 pero n2 no
            grid[esta1[0]].insert(esta1[1],n2) #Se inserta n2 a la izq de n1
        elif ((esta1[0]==-1) and (esta2[0]!=-1)):#Si està n2 pero no n1
            grid[esta2[0]].insert(esta2[1]+1,n1) #Se inserta n1 a la der de n2
        elif ((esta1[0]==-1) and (esta2[0]==-1)):#No esta n1 y n2
            #Se intenta añadir n1 y n2 al grid vacio
            if(len(grid[0])<=1):
                grid[0].append(n1);grid[0].append(n2) 
            elif(len(grid[1])<=1):
                grid[1].append(n1);grid[1].append(n2)
            elif(len(grid[2])<=1):
                grid[2].append(n1);grid[2].append(n2)
            else:
                print("ERROR: No hay espacio en el grid para n1= ",n1," y n2= ",n2, "con mov= ",mov)
                print(grid)
    return grid

def esta (grid,n):
    res=[-1,-1]
    if((len(grid[0])==0) and (len(grid[1])==0) and (len(grid[2])==0)): 
        return res

    for x in range(0,len(grid)):
        if(len(grid[x])!=0):
            for y in range(0,len(grid[x])):
                if(grid[x][y]==n):
                    res[0]=x
                    res[1]=y

    return res
def centrar (grid,centro):
    #Si el mov es 0, n2 queda a la derecha de n1
    #Si el mov es 1, n2 queda arriba de n1
    #Si el mov es 2, n2 queda debajo de n1
    #Si el mov es 3, n2 queda a la izquierda de n1
    grid[1].append(centro[0])
    for x in range(1,5):
        if(centro[x][0]==0):
            grid[1].append(centro[x][1])
        elif (centro[x][0]==1):
            grid[0].insert(1,centro[x][1])
        elif (centro[x][0]==2):
            grid[2].insert(1,centro[x][1])
        elif (centro[x][0]==3):
            grid[1].insert(0,centro[x][1])
    print("Asi quedó la grid")
    print(grid)
    return grid