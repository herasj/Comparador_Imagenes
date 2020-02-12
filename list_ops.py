import copy
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