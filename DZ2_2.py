#Jovan Penezic



###Funkcije###



def NZD(a, b):      #Funkcija podrazumeva a >= b
    if b==0:
        return a
    a %= b
    return NZD(b, a)


###Glavni program###



while(True):

    x = raw_input("Unesite prvi broj: ")
    try:
        number = int(x)
    except ValueError:
        print "Unesena vrednost nije ceo broj"
        exit(1)
    if int(x) <= 0:
        print "Brojevi moraju da budu veci od nule"
        exit(1)

    y = raw_input("Unesite drugi broj: ")
    try:
        number = int(y)
    except ValueError:
        print "Unesena vrednost nije ceo broj"
        exit(1)
    if int(y) <= 0:
        print "Brojevi moraju da budu veci od nule"
        exit(1)

    print NZD(int(x), int(y))