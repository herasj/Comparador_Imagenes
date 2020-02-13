def recortar():
    from PIL import Image
    from string import Template
    import math

    size=[] #Inicializar lista

    #Abrir imagen principal
    im = Image.open('./src/img/img.jpg')# Imagen Cuadrada !
    dim = (im.height) #Las dimensiones de la imagen

    #Coordenadas del recorte
    size.append(0)
    size.append(math.floor(dim/3))
    size.append(math.floor(2*dim/3))
    size.append(dim)

    cont=0

    for y in range(0,3):
        for x in range(0,3):
            t = Template('./src/crop/$name.jpg') #Path de guardado
            path = t.substitute(name=cont) #Template string
            up=size[y]#0,166,333
            l=size[x]#166,333,500
            r=l+size[1] #x+w
            dw=up+size[1] #y+h
            recorte = im.crop((l,up,r,dw)) #(x,y,x+w,y+h) coordenadas
            recorte.save(path) #Guardar imagen recortada
            cont=cont+1;