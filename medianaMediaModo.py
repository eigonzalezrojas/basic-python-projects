# Mean
list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
mean = sum(list1)/len(list1)
print(mean)


# Median

'''
La mediana es el valor que divide una lista ordenada en dos mitades: el 50% de los números es menor que la mediana y 
el 50% es mayor. Si la lista tiene un número impar de elementos, 
la mediana es el valor del medio. Si tiene un número par de elementos, 
la mediana es el promedio de los dos valores centrales.

'''

list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
list1.sort() #La función sort() ordena la lista de forma ascendente. 

if len(list1) % 2 == 0: # Se verifica si la longitud de la lista es par o impar
    m1 = list1[len(list1)//2]
    m2 = list1[len(list1)//2 - 1]
    median = (m1 + m2)/2
else:
    median = list1


# Mode
list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
frequency = {}
for i in list1:
    frequency.setdefault(i, 0)
    frequency[i]+=1

frequent = max(frequency.values())
for i, j in frequency.items():
    if j == frequent:
        mode = i