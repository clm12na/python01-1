# Palabras en pokemon.txt
Repositorio para trabajar en SD.<br/>
Grupo formado por:<br/>
David José Corral Plaza

En este ejercicio hemos desarrollado un código que se encarga de encontrar la mayor sucesión de palabras con un cierto criterio en un fichero. A continuación, explicamos el funcionamiento de cada una de las funciones definidas:

#def areIn(list_aux, word)<br/>
Se encarga de devolver True si la palabra "word" está en la lista "list_aux" o False en caso contrario.

#def equalOrNot(word,wordAux)<br/>
Se encarga de devolver True si la palabra "word" es igual a "wordAux" o False en caso contrario.

#def foundNext(listf, list_aux, word)<br/>
Se encarga de encontrar en una lista principal, lisft, una palabra, WordAux, que es igual a word y que no se encuentre almacenada en list_aux. Devuelve esa palabra.

#def compareList(list_aux, list_sol)<br/>
Se encarga de decidir si la lista list_aux es mayor, tiene un mayor numero de palabras consecutivas, que la lista que, hasta el momento, era la definitiva, list_sol.

#def createList(fich)<br/>
A partir de una ruta de un fichero, en primera instancia cargamos todas las palabras del fichero en una lista principal y, para cada una de esas palabras en la lista, realizamos una iteración que, haciendo uso de las funciones anteriormente definidas, obtiene la mayor lista de palabras consecutivas con el criterio predefinido.
