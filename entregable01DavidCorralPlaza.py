def primeraestrofa(beers):
     print beers,"bottles of beer on the wall,", beers,"bottles of beer."

def segundaestrofa(beers):
    print "Take one down, pass it around,",beers,"bottles of beer on the wall.\n"

beers = 99
while beers >= 1:
    primeraestrofa(beers)
    beers = beers - 1
    segundaestrofa(beers)
    