'''
    Este código agrupa palabras que son anagramas, es decir, 
    palabras que contienen las mismas letras pero en diferente orden, 
    como “tea”, “eat”, y “ate”.

'''

from collections import defaultdict

def group_anagrams(a):
    # Creamos un defaultdict que devuelve una lista vacía como valor por defecto
    dfdict = defaultdict(list)
    for i in a:
        print(f"Palabra original: {i}")
        sorted_i = "".join(sorted(i))
        print(f"Palabra ordenada: {sorted_i}")
        '''
        * Se recorre cada palabra en la lista a.
	    * Para cada palabra, la función sorted(i) ordena sus letras alfabéticamente, 
        lo que convierte palabras anagramas en la misma secuencia de letras. 
        Por ejemplo, sorted("tea"), sorted("eat") y sorted("ate") darán como resultado la lista ['a', 'e', 't'].
	    * La línea " ".join(sorted(i)) convierte la lista ordenada en una cadena de texto con las letras separadas por un espacio, 
        aunque podría hacerse sin espacio. Por ejemplo, "tea" se convierte en "a e t".
	    * Luego, esa cadena ordenada (que actúa como clave) se usa para agrupar 
        las palabras originales que son anagramas en una lista dentro del diccionario dfdict. 
        Todas las palabras que tienen la misma secuencia ordenada de letras se almacenan juntas.

        '''
        dfdict[sorted_i].append(i)
        # El papel de defaultdict es asegurarse de que las palabras con la misma secuencia ordenada (es decir, los anagramas) se agrupen en una lista bajo la misma clave. 
        print(f"Diccionario actual: {dfdict}")
    return dfdict.values()

words = ["tea", "eat", "bat", "ate", "arc", "car"]
print(group_anagrams(words))