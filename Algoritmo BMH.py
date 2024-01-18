#Un scrpit de busqueda de texto
import os  # Blibioteca para verificar existencia del archivo 

#Funcion de BUSQUEDA

def Busqueda(texto,palabra):
    #Funcion de saltos de letras
    def fracaso(palabra):
        d={}
        for i in range(len(palabra)-1):
            d[palabra[i]]=i
        return d
    #////////////////////////////
    d=fracaso(palabra)
    n=len(palabra)-1 #tope de la palabra
    m=len(texto)-1 #tope del texto
    i=n #indices para texto
    j=n #indices para palabra
    r=[] #lugares de palabra
    while i<=m:
        if texto[i]==palabra[j]:
            i=i-1
            j=j-1
            if j<0:
                r.append(i+1)
                i=i+2*(n+1)
                j=n
                #continue
        elif texto[i] in d: #hasta aqui todo bien
            if j> d[texto[i]]:
                i=i+(n-j)+(j-d[texto[i]])
                j=n
                #continue
            else: #parece implicar j< d[texto[i]]
                i=i+(n-j)+ 1 
                j=n
                #continue
        else:
            i=i+(n-j)+(j+1)
            j=n
            #continue
    return r


#///////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////
archivo=str(input('Nombre del archivo(.txt):'))

if os.path.isfile(f"C:/Users/DELL/Documentos/Clases Maestría/Programación/Tareas/Victor Becerril Proyecto 1.0/{archivo}.txt"):
    with open(f"{archivo}.txt", "r", encoding='utf-8') as f:
        palabra= str(input("Que patron busca en el texto?:"))
        #Leer el archivo linea por linea
        lineas=[] #para contar la linea
        lin=0 #iterador
        rep=[] #para saber cuantas veces
        for linea in f:
            texto=linea
            r=Busqueda(texto,palabra) #aplico la funcion de busqueda
            lin=lin+1
            print(r)
            #Para guardar las lineas en las que aparece el patron
            if len(r)>0:
                lineas.append(lin)
                rep.append(len(r))
                
    #print(lineas)
    #print(rep)
        
    if len(lineas)>0:
        print(f"el patron '{palabra}' se presento:")
        for x in range(len(lineas)):
            print(f"{rep[x]} veces en la linea {lineas[x]}")
    else:
        print("La secuencia no se encuntra en el archivo")

            
else:
    print('El archivo no se encuentra en la carpeta local o no es un archivo .txt')
