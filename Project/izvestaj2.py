#izvestaj2
import logovanje22
from datetime import datetime

def izvestaj2():
    sum = 0
    print("")
    datum01 = input("Unesi datum pocetka za izvestaj u formatu 18-01-2015: ")
    datum02 = input("Unesi datum kraja za izvestaj u formatu 18-01-2015: ")
    try:
        datum1 = datetime.strptime(datum01,"%d-%m-%Y")
        datum2 = datetime.strptime(datum02,"%d-%m-%Y")
    except:

        print("Pogresan format datuma.")
        izvestaj2()
    print("")


    with open("izvestavanje.txt") as fajl:
        podaci = [i.split("/") for i in fajl.read().splitlines()]
    d = {}
    c = {}

    for datum, kategorija, naziv,cena, kolicina, ukupna_cena in podaci:
        datum = datetime.strptime(datum,"%d-%m-%Y")
        if datum >= datum1 and datum <= datum2:
            try:
                d[kategorija] += int(ukupna_cena)
            except KeyError:
                d[kategorija] = int(ukupna_cena)

    print("Izvestaj za period od " +datum01+ " do "+ datum02)
    print("")
    print("Ukupan promet za svaku kategoriju:")
    print("Kategorija   |ukupna_cena | \n""------------+-------------+")
    for kategorija, ukupna_cena in d.items():
        print("{0:13}|{1:12}".format(kategorija, str(ukupna_cena)))


    for datum, kategorija, naziv,cena, kolicina, ukupna_cena in podaci:
        datum = datetime.strptime(datum,"%d-%m-%Y")
        if datum >= datum1 and datum <= datum2:
            try:
                c[kategorija] += int(kolicina)
            except KeyError:
                c[kategorija] = int(kolicina)
    print("")
    print("Kolicina za svaku kategoriju:")
    print("Kategorija   |kolicina    | \n""------------+-------------+")
    for kategorija, kolicina in c.items():
        print("{0:13}|{1:12}".format(kategorija, str(kolicina)))


    logovanje22.menadzer()