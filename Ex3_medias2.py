#Exercício 3 - Lista


def media2():
    a = 0
    i = 1
    soma = 0
    media = 0
    while i>=1:
        print "Insira uma nota"
        a = float (raw_input())
        if a>0:
            soma = soma +a
            i+=1
        else:
            media = soma/(i-1)
            print "A media das notas é %f" % (media)
            i=-1
                

# Nota: 0.5
