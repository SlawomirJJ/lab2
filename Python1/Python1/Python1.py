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

print ("\n \n pętla for \n")

for i in range(len(d)):
    d[i] = d[i]*0.1
