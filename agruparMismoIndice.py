inputLists = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
outputLists = []
index = 0

for i in range(len(inputLists[0])):
    outputLists.append([])
    '''
    Aquí, range(len(inputLists[0])) obtiene la cantidad de elementos de la primera lista dentro de inputLists 
	El bucle agrega una lista vacía [] a outputLists en cada iteración. Como hay 3 elementos en cada sublista, 
    se agregarán 3 listas vacías a outputLists.
    
    '''
    for j in range(len(inputLists)):
        outputLists[index].append(inputLists[j][ index])
        '''
        •	Este bucle anidado recorre cada lista interna de inputLists. Aquí, range(len(inputLists)) es 3, ya que inputLists tiene 3 sublistas.
	    •	La línea inputLists[j][index] selecciona el elemento de la posición [j][index], es decir, 
            toma el elemento de la lista j en la posición index.
	    •	En cada iteración del bucle, se va agregando el elemento a la sublista correspondiente en outputLists.
        
        '''
    index = index + 1
a, b, c = outputLists[0], outputLists[1], outputLists[2]
print(a, b, c)