#Jovan Penezic

recnik_cifara = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}



###Funkcije###



def slice_recnika(recnik,osnova):   # Funkcija za sliceovanje recnika (treba nam samo recnik do osnove-1 u proveri)
    return {cifra for cifra,i in recnik_cifara.iteritems() if i < osnova}


def provera_unosa(unos,osnova):     # Provera unetog broja
    tcifre = slice_recnika(recnik_cifara,osnova)
    for i in range(0,len(unos)):
        if(unos[i] not in tcifre):
            print "Uneseni broj nije u sistemu unesene osnove"
            exit(1)


def konvert(unos,osnova):   # Konvertovanje u decimalni sistem
    dec = 0
    stepen_osnove = 1

    if recnik_cifara[unos[0]] < (osnova / 2):
        for i in range(len(unos)-1,0,-1):
            dec += stepen_osnove * recnik_cifara[unos[i]]
            stepen_osnove *= osnova
        print dec
    else:
        unos1 = []      # Stringovi su immutable pa pravimo novi string radi komplementovanja broja

        i = len(unos) - 1
                                                                    # Broj se komplementuje kao da je predstavljen u len(unos)-bitnom sistemu:
        while(recnik_cifara[unos[i]] == 0 and i>0):                 # 1. Krecuci sa desne strane prepisujemo nule
            unos1.append(unos[i])
            i -= 1

        unos1.append(str(osnova - recnik_cifara[unos[i]]))          # 2. Prvu nenultu cifru komplementujemo do osnove
        i -= 1

        while i > 0:                                                # 3. Preostale cifre komplementujemo do najvece cifre
            unos1.append(str(osnova - 1 - recnik_cifara[unos[i]]))
            i -= 1

        for i in range(0,len(unos1)):   #Izracunavanje komplementovanog broja
            dec += stepen_osnove * recnik_cifara[unos1[i]]
            stepen_osnove *= osnova
        print -dec
        print "Broj je negativan"
        exit(1)



###Glavni program###



while(True):
    osnova = raw_input("Unesite osnovu: ")
    try:
        number = int(osnova)
    except ValueError:
        print "Unesena osnova je nepravilna"
        exit(1)

    if int(osnova) < 2 or int(osnova)>16:
        print "Unesena osnova je van granica osnova"
        exit(1)

    broj = raw_input("Unesite broj: ")

    provera_unosa(broj,int(osnova))
    konvert(broj,int(osnova))
