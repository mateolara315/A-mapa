import numpy as np

#//////////////////////////////Empezar búsqueda////////////////////////////////

#matriz como string que representa las conecciones y pesos:
adjMat = np.genfromtxt('adyacencia_grafo_dirigido_con_pesos.tsv', delimiter=
                       "\t", skip_header=1, filling_values=1, dtype=str)
# Lista con el nombre de todos los nodos:
nodes = adjMat[:, 0]  
 # borra la primera columna con nombres:
adjMat = np.delete(adjMat, 0, axis=1) 
# matris de conecciones y pesos con int:
adjMat = adjMat.astype(int) 
#Se añade un valor muy garnde a los ceros de la matrix de conecciones y pesos:
adjMat[adjMat == 0] = 10e5 
#array de heuristicas:
h = np.array([73, 9, 19, 54, 4, 57, 85, 59, 10e5, 0, 10e5, 10e5])

# Estado inicial A:
f_state = nodes[9]
i_state = nodes[0] 
state = i_state
memory = []
print('INICIO:')
print('           ',np.array(['g(n), h(n), n, ruta']))
while True:     
    
#    print(state)
    if state == i_state:
        for i in range(len(nodes)-1):
            a = str(int(adjMat[0,i+1]))
            b = str(nodes[i+1])
            c = str(int(h[i+1]))
            ruta = i_state+str(nodes[i+1])
            #print(a+'*'+c+'*'+b+'*'+ruta)
            memory = np.append(memory, a+'*'+c+'*'+b+'*'+ruta)
        #print(g)
        #f = g + h
    fin = 100000000
    for i in range(len(memory)-1):#este bloque se encarga de detectar
        #cual es el mejor noda para ser expandido
        win = memory[i].split("*")
        gn = int(win[0])
        hn = int(win[1])
        t = gn + hn
        if t<fin:
            fin = t
            expan = win 
            save = i
    memory = np.delete(memory,save)
    print('expandido: ',expan)        
    pos_letra = np.where(nodes == expan[2])  

    if state == 'para':
        if (expan[2] == f_state):
            #print(memory)
            break
        
    for i in range(len(nodes)-1):#este bloque se encarga de expandir el
        #nodo que fue elegido en el paso anteriro 
            if i != pos_letra[0]:
                a = str(int(adjMat[pos_letra,i])+int(expan[0]))
                b = str(nodes[i])
                #c = str(int(h[i])+int(expan[0]))
                c = str(int(h[i]))
                ruta = str(expan[3] + nodes[i])
                #print(a+'*'+c+'*'+b+'*'+ruta)
                memory = np.append(memory, a+'*'+c+'*'+b+'*'+ruta)
                
    #print('en memoria: ',memory)  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!          
    state = 'para'  

print("\nValidación de heurística:\nLa heurística elegida fue diseñada para salir del nodo A y llegar al nodo J usando Dijkstra, para el caso en el que se planee ir del nodo A a J la heurística siempre será admisible, ya que esta nunca sobrestima el costo de alcanzar la meta porque siempre proporciona el valor real de llegar a ella, por otro lado la heurística es también consistente, ya que el valor de g(n)+h(n) a lo largo de las expansiones (camino) es no decreciente, esto se puede ver en como se espade el espacio de búsqueda en cada iteración, ver que g(n)+h(n) suman siempre 73, cabe resaltar que toda heurística consistente es también admisible.")
    
       

