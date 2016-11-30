#Jovan Penezic


###Biblioteke###
from __future__ import division
import math
import random


###Funkcije###



def GeorgeLeibnitz (epsilon):
    k = 1
    pi = 0
    while(math.fabs((4.0*(-1)**(k+1))/(2*k-1)) > epsilon):
        pi += 4.0*(-1)**(k+1)/(2*k-1)
        k += 1
    print "George-Leibnitz\n", pi, "\n", k, "\n", math.fabs(pi - math.pi),"\n"


def Wallis (epsilon):
    k = 1
    pi = 2.0
    while((pi*(4.0*k**2)/(4.0*k**2-1)-pi) > epsilon):
        pi *= 4.0*k**2/(4*k**2-1)
        k += 1
    print "Wallis\n",pi,"\n",k,"\n",math.fabs(pi-math.pi),"\n"


def Nilakantha (epsilon):
    k = 1
    pi = 3.0
    while(math.fabs((4.0*(-1)**(k+1)/(2*k*(2*k+1)*(2*k+2)))) > epsilon):
        pi += 4.0*(-1)**(k+1)/(2*k*(2*k+1)*(2*k+2))
        k += 1
    print "Nilakantha\n",pi,"\n",k,"\n",math.fabs(pi-math.pi),"\n"


def Monte_Carlo (epsilon):
    tacke = 0
    tacke_u_krugu = 0
    pi = 0
    while(math.fabs(math.pi - pi) > epsilon):
        x = random.random()
        y = random.random()
        if(x**2 + y**2 <= 1.0):
            tacke_u_krugu += 1
        tacke += 1
        pi = tacke_u_krugu/tacke * 4
    print "Monte Karlo\n",pi,"\n",tacke,"\n",math.fabs(pi-math.pi),"\n"


###Glavni program###



epsilon = raw_input("Unesite toleranciju greske: ")
try:
    number = float(epsilon)
except ValueError:
    print "Unesena vrednost nije broj"
    exit(1)

GeorgeLeibnitz(float(epsilon))
Wallis(float(epsilon))
Nilakantha(float(epsilon))
Monte_Carlo(float(epsilon))
