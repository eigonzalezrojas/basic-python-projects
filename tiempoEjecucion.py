from time import time
start = time()

# Python program to create acronyms
word = "Artificial Intelligence"
text = word.split() # Divide la cadena word en una lista de palabras, separadas por los espacios en blanco
a = " "
for i in text:
    #
    a = a+str(i[0]).upper()
print(a)

end = time()
execution_time = end - start
print("Execution Time : ", execution_time,  "seg")