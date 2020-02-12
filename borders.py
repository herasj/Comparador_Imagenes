def getborders(img,h):
    bordes=[] #Lista que contiene las demás
    up=[]
    left=[]
    right=[]
    down=[]

    #Bordes
    for x in range (0, h):
        up.append(abs(img[x,0]-img[x,1])) #[X,Y]  Superior
        down.append(abs(img[x,h-1]-img[x,h-2])) #Inferior
        left.append(abs(img[0,x]-img[1,x])) #Izquierda
        right.append(abs(img[h-1,x]-img[h-2,x])) #Derecha
        #Obtiene la diferencia entre los dos pixeles de cada borde

    #Estructura de bordes [[up],[down],[left],[right]]
    bordes.append(up);bordes.append(down);bordes.append(left);bordes.append(right)
    return bordes
