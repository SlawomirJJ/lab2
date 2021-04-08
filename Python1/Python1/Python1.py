# tekst = "Lorem ipsum dolor sit amet, ..."
#print (tekst)
#print (tekst)

paliwo = 8.5 * (67*0.1 + 124*0.15 + 11.7*0.2)
autostrada = 124*0.17
prom = 50
koszt = paliwo + autostrada + prom
print (koszt)
print (koszt / 2)
print (koszt / 3)
print (koszt / 4)
print (koszt / 5)

lista = [1,2,3,4,"napis", True, False, 8.5, 11]

slownik = {"jablecznik" : "ciasto z jablek", "czy lubisz jablecznik" : True}

print ("\n listy")
d=[10, 8, 10, 12, 6, 8, 7, 12, 10, 16, 16, 9, 14, 9, 11, 17, 18, 9, 5, 17, 11, 17, 7, 7, 12, 9, 5, 18, 6, 7, 9, 9, 6, 8, 8, 11, 13, 16, 8, 8, 12, 5, 18, 15, 17, 18, 7, 8, 13, 5, 12, 11, 11, 12, 5, 17, 7, 15, 10, 14, 18, 5, 8, 9, 10, 14, 15, 13, 16, 14, 17, 16, 10, 7, 14, 15, 17, 11, 10, 18, 18, 9, 12, 18, 12, 13, 7, 10, 16, 12, 16, 8, 11, 15, 8, 7, 7, 10, 13, 13]

print (d[16])
print ("\n \n")
print (d[9])
print (d[10])
print (d[11])
print (d[12])
print (d[13])
print (d[14])

print ("\n \n")

print (d[9:15])#skrucony zapis
print ("\n ")
print (d[-1])#bierze ostatni element z listy

d[11] = d[11] - 0.1

lista = range(15)
print (lista)

print ("\n \n Słowniki \n")

dictionary = {'plytka1':101, 'plytka2':201, 'plytka3': 302, 'plytka4':102}

print (dictionary['plytka1'])

print (dictionary)
print(dictionary.keys())
print (dictionary.values())


dictionary['plytka5']=0 #dodanie wartości do słownika

print (dictionary)
del dictionary['plytka5']
print (dictionary)
del (dictionary)
#print (dictionary) #zgłaszawyjątek bo dictionary jest usunięty

print ("\n \n pętla for")

for i in range(len(d)):
    d[i] = d[i]*0.1


print ("\n  \n")

for element in [1,2,3,4,5]:
    print (element)
print ("zrobimy sobie odstep")
print (element)

print ("\n  len \n")
print (len([851, 1, 58])) #len zwraca nam długość listy


print ("\n \n")
zmienna = 8
if zmienna > 5:
    print ("Zmienna jest wieksza niz 5")

print ("\n \n")
zmienna = 8
if zmienna == 15:
    print ("Zmienna jest rowna 15")
else:
    print ("Zmienna nie jest rowna 15")

print ("\n \n")
zmienna = 8
if zmienna == 5:
    print ("Zmienna jest rowna 5")
elif zmienna == 8:
    print ("Zmienna jest rowna 8")
elif zmienna > 5:
    print ("Zmienna jest rowna 5 ale nie jest rowna 8")
else:
    print ("Zmienna jest mniejsza od 5")



print ("\n \n Pętla while")
x=0
while x<5:
    print ("zmienna x wynosi ",x)
    x+=1



x=0
while True:
    print ("To wyswietli sie zawsze gdy warunek jest spelniony")
    if x==5:
        print ("zmienna x wynosi ", x)
        break
    else:
        print (x)
    x+=1 


print ("\n \n ")
x=[1,2,3,4,5]
while x:
    y=x.pop()# metoda pop() zwraca ostatnią wartość z listy jednocześnie ją usuwając
    print ("ostatnia wartości z listy x to ", y)
else:
    print ('koniec')

print ("\n \n ")
x=[1,2,3,4,5]
while x:
    y=x.pop()
    print (y)
print ('koniec')



print ("\n \n ")
x = 15
wynik = (2 * (x**3))/8.51
print (wynik)

print ("\n ")
def f(x):              #funkcja: def nazwa_funkcji
    return (2 * (x**3))/8.51
 
print (f(5))

def funkcja():
    print ("wykonalo sie")


def f(x=0):
    return (2 * (x**3))/8.51

print ("\n \n ")

print (f())
print (f(5))


print ("\n \n ")
def f(x=0):
    return (2 * (x**3))/8.51
 
funkcja = f
 
print (f())
print (funkcja())

print ("\n \n ")
def wyswietl(napis):
    print (napis)
 
def wez_napis_i_cos_z_nim_zrob(napis, zrob):
    zrob(napis)
 
wez_napis_i_cos_z_nim_zrob("Jakis napis", wyswietl)



print ("\n \n ")
#kalkulator
def policz(jak, liczba1, liczba2):
    return jak(liczba1, liczba2)
 
def dodaj(x, y):
    return x+y

def odejmi(x, y):
    return x-y
 
def podnies_do_potegi(x, y):
    return x**y
 
def pomnoz(x, y):
    return x*y
 
def podziel(x, y):
    #tutaj zamieniamy jedna z liczb
    #na zmiennoprzecinkowa na 
    #potrzeby Pyhona2
    return (x*1.0)/y


print ("\n \n ")
#rekurencja, liczenie silni
def silnia(x):
    if x==1 or x==0:
        return 1
    else:
        return x*silnia(x-1)

print(silnia(5))


print ("\n \n Operacje na plikch ")

    #otwarcie pliku
#plik = open('ścieżka/do/pliku.txt')#ścieżka może być bezwzględna (cała ścieżka do pliku) lub może to być ścieżka z miejsca, w                                        którym uruchomiony jest program

# tak otwarty plik można przeczytać używając:
#print (plik.read())#  wielolinijkowy napis

#odczytanie linijka po linijce
#for linia in plik:
#    print (linia)

#linia.strip() # usuwa zbędne znaki końca linii

# Po zakończeniu pracy z plikiem należy go zamknąć
#plik.close()

# split - dzieli napis na listę wyrazów
tekst = "Jakis tam sobie tekst dla przykladu"
print (tekst.split())

#inny sposób otwarcia pliku
# with open('plik.txt') as plik:
#   for linia in plik:
#       print linia.strip().split()


# jeśli chcemy otworzyć plik w trybie do zapisu należy dodać "w" domyślnie jest r
# plik = open('plik.txt','r')
# plik = open('plik.txt','w')

#zapisywanie stringów do pliku  "Enter" - "\n" tabulacja - "\t" 
    #kiedy otwierasz plik w trybie zapisu cała zawartość jest czyszczona bezpowrotnie!!!
# plik.write(str(55552522))
# plik.write("\n")
# plik.write("Tutaj masz jakis napis")

#otwarcie w trybie dopisywania do pliku, to co się dopisuje idzie na koniec pliku
#plik = open('plik.txt','a')

#Kiedy otwierasz nieistniejący plik w trybie 'w' lub "a" jest on domyślnie tworzony.

plik1 = open('testowy_plik.txt','w')
plik1.write("Tutaj masz jakis napis")
plik1.close()

plik1 = open('testowy_plik.txt','a')
plik1.write("\n dodany napis")
plik1.close()

print ("\n \n Dodatkowe biblioteki")
import random
print (random.randint(1,20))

from time import sleep
sleep(10)

from module1 import *
a()
b()


# słowniki domyślne, zliczanie liter w stringu
from collections import defaultdict
d = defaultdict(int)
print  (d['x'])
 

napis = "aaabbccoooossasdk"
for litera in napis:
    d[litera] += 1
print (d)







