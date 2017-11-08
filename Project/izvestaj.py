#izvestaj1
import logovanje22
from datetime import datetime

def izvestaj():
    sum = 0
    print("")
    datum01 = input("Unesi datum pocetka za izvestaj u formatu 18-01-2015: ")
    datum02 = input("Unesi datum kraja za izvestaj u formatu 18-01-2015: ")
    try:
        datum1 = datetime.strptime(datum01,"%d-%m-%Y")
        datum2 = datetime.strptime(datum02,"%d-%m-%Y")
    except:
        print("Pogresan format datuma.")
        izvestaj()

    with open('Racuni.txt') as fajl:
        podaci = [i.split("/") for i in fajl.read().splitlines()]
    print("")
    d = {}
    for nesto1, nesto2, datum, nesto3, nesto4, nesto5, nesto6, nesto7, nesto8, nesto9, nesto10, cena, nesto12 in podaci:
        datum = datetime.strptime(datum,"%d-%m-%Y")
        if datum >= datum1 and datum <= datum2:
            try:
                d[datum] += int(cena)
            except KeyError:
                d[datum] = int(cena)

    print("Izvestaj za period od "+ datum01 +" do " + datum02)
    print("")
    print("Datum              |cena        | \n""------------------+-------------+")
    for datum, cena in d.items():
        print(datum,str(cena))
        sum += int(cena)
    print("SUMA JE :", sum)


    logovanje22.menadzer()