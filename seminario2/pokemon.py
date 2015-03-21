# -*- coding: utf-8 -*-
# Realizado por:
# David José Corral Plaza
#
#
# Puede encontrar los comentarios del código en README.md
# de la carpeta correspondiente al código.


def areIn(list_aux, word):
    for wordAux in list_aux:
        if word==wordAux:
            return True
        else:
            return False

def equalOrNot(word,wordAux):
    if word[len(word)-1] == wordAux[0]:
        return True
    else:
        return False

def foundNext(listf, list_aux, word):
    for wordAux in listf:
        if areIn(list_aux, wordAux) == False and equalOrNot(word,wordAux):
            return wordAux
    return ""

def compareList(list_aux, list_sol):
    if len(list_aux) > len(list_sol): 
        return True
    else:
        return False

def createList(fich):
    listf = []
    list_sol = []
    with open(fich) as myfich:
        for line in myfich: 
            for word in line.split(' '): 
                word = word.replace("\n","") 
                listf += [word]

    for word in listf:
        list_aux = []
        list_aux += [word]
        nexto = foundNext(listf, list_aux, word)
        while nexto != "": 
            list_aux += [nexto]
            word = nexto
            nexto = foundNext(listf, list_aux, word)
    
        if compareList(list_aux,list_sol) == True:
            list_sol = list(list_aux)


fichero = raw_input("Introduzca el nombre del fichero (ej. 'pokemon.txt'): ")
print "Mayor lista encontrada: "
createList(fichero)
