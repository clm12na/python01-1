# -*- coding: utf-8 -*-

def areIn(list_aux, word):
    for wordAux in list_aux:
        if word==wordAux:
            return True
        else:
            return False


def foundNext(listf, list_aux, word):
    for wordAux in listf:
        if areIn(list_aux, wordAux) == False and word[len(word)-1] == wordAux[0]:
            return wordAux
    return ""


def createList(fich):
    listf = []
    list_sol = []
    with open(fich) as myfich:
        for line in myfich: 
            for word in line.split(' '): 
                word = word.replace("\n","") 
                listf += [word]
    #Para cada línea del fichero, eliminamos los saltos de líneas y cargamos
    #las palabras en la list principal.
    
    for word in listf:
        list_aux = [] # Borramos el contenido de la lista auxiliar
        list_aux += [word]
        siguiente = foundNext(listf, list_aux, word)
        while siguiente != "": # Mientras encontremos una palabra que sea factible
            list_aux += [siguiente] # La añadimos
            word = siguiente # Actualizamos la palabra
            siguiente = foundNext(listf, list_aux, word) # Buscamos la siguiente
    
        if len(list_aux) > len(list_sol): # Si hemos obtenido más palabras en esta iteración
            list_sol = list(list_aux)


fichero = raw_input("Introduzca el nombre del fichero (ej. 'pokemon.txt'): ")
print "Mayor lista encontrada: "
createList(fichero)