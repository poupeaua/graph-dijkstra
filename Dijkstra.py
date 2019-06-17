from queue import PriorityQueue

#La cola de prioridad es una estructura de datos a la que podemos insertarle elementos,
#obtener el elemento de mayor prioridad (con una definicion de prioridad asignada) y
#eliminar elementos de forma eficiente.

#Fijamos el infinito
Infinity=2**30

#nodoI es donde parte y grafo es una lista de listas de
#pares. grafo[0] es una lista de los arcos que "salen" del nodo 0. La lista
#se ve de la siguiente forma: Digamos que 0 esta conectado con 1 con peso 2
#y con 2 con peso 5. Entonces grafo[0]=[(1, 2), (2, 5)]
def dijkstra(nodoI, grafo):

    #Creamos la cola de prioridad que entregara el menor elemento
    #La usaremos para obtener el nodo a distancia menor no visitado
    C=PriorityQueue()

    #Dist sera la lista de distancias de nodoI a todos los demas
    #Inicializa en infinito
    Dist=[]
    for i in range(0, len(grafo)):
        Dist+=[Infinity]

    #Rev es la lista de booleanos que nos dira si ya hemos revisado un nodo
    Rev=[]
    for i in range(0, len(grafo)):
        Rev+=[False]

    #Debemos especificar Dist[nodoI]=0 pues la distancia inicial
    Dist[nodoI]=0

    #nodoI es el primer elemento posible a revisar y tiene distancia
    #0.
    C.put((0, nodoI))

    while not C.empty():
        #Obtenemos el nodo no visitado a menor distancia y lo eliminamos
        par=C.get()

        #nodo es el nombre del nodo donde estamos parados
        nodo=par[1]

        #d es la distancia de nodoI a nodo
        d=par[0]

        #Si nodo ya esta revisado no debemos procesarlo
        if Rev[nodo]:
            continue

        #Lo marcamos como revisado
        Rev[nodo]=True

        #Revisamos todos los arcos que salen de nodo
        for par in grafo[nodo]:
            nodo2=par[0]
            distancia=par[1]
            if distancia+d<Dist[nodo2]:
                Dist[nodo2]=distancia+d
                C.put((distancia+d, nodo2))
    return Dist

#El grafo usado aqui es: los numeros entre parentesis son el peso del arco
#0->(9)1
#0->(3)2
#2->(3)3
#3->(1)4
#4->(1)1
# print(dijkstra(0, [[(1, 9), (2, 3)],
#                    [],
#                    [(3, 3)],
#                    [(4, 1)],
#                    [(1, 1)]]))
