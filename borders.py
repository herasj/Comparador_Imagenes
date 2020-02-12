def getborders(img,h):
    bordes=[] #Lista que contiene las demás
    up=[]
    left=[]
    right=[]
    down=[]

    #Bordes
    for x in range (0, h):
        up.append(abs(img[x,0])) #[X,Y]  Superior -img[x,1]
        down.append(abs(img[x,h-1])) #Inferior -img[x,h-2]
        left.append(abs(img[0,x])) #Izquierda -img[1,x]
        right.append(abs(img[h-1,x])) #Derecha -img[h-2,x]
        #Obtiene la diferencia entre los pixeles de cada borde

    #Estructura de bordes [[up],[down],[left],[right]]
    bordes.append(up);bordes.append(down);bordes.append(left);bordes.append(right)
    return bordes
