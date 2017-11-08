# -*- coding: utf-8 -*-
import unos
import izmena
import brisanje
import pretraga
import izdavanje_racuna
import izvestaj
import izvestaj2
import time


def meni1():
    print("")
    print("Izaberite zeljeni fajl.\n1. Korisnici\n2. Kategorija\n3. Namestaj\n4. Usluge-salona\n5. Racuni\n6. Vracanje unazad. ")
    x = input("Unesite broj:  ")
    x = int(x)
    return x


def fajlovi_unos():
    print("")
    x = meni1()
    if x == 1:
        unos.korisnici_unos()
    elif x == 2:
        unos.kategorija_unos()
    elif x == 3:
        unos.namestaj_unos()
    elif x == 4:
        unos.usluga_unos()
    elif x == 5:
        print("Izabrali ste fajl Racuni, za koji nije dozvoljen unos.")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        fajlovi_unos()
    elif x == 6:
        print("Vracanje u nazad. ")
        unos_brisanje_izmena()
    else:
        print("Morate izabrati jednu od ponudjenih opcija.")
        fajlovi_unos()


def Izmena():
    print("")
    x = meni1()
    if x == 1:
        izmena.korisnici_izmena()
    elif x == 2:
        izmena.kategorija_izmena()
    elif x == 3:
        izmena.namestaj_izmena()
    elif x == 4:
        izmena.usluga_izmena()
    elif x == 5:
        print("Za racun nije dozvoljena izmena!")
        Izmena()
    elif x == 6:
        print("Vracanje unazad. ")
        unos_brisanje_izmena()
    else:
        print("Morate izabrati jednu od ponudjenih opcija.")
        Izmena()


def Pretraga():
    print("")
    print(
        "Izaberite sta zelite da pretrazujete. \n1. Komadi namestaja\n2. Usluge-salona\n3. Racuni.\n4. Vracanje u nazad")
    x = input("Unesite broj:  ")
    x = int(x)
    if x == 1:
        pretraga.namestaj_pretraga()
    elif x == 2:
        pretraga.usluga_pretraga()
    elif x == 3:
        pretraga.racuni_pretraga()
    elif x == 4:
        print("Vracanje u nazad")
        logovanje()
    else:
        print("Morate izabrati jednu od opcija")
        Pretraga()


def unos_brisanje_izmena():
    print("")
    print("Izaberite jednu od opcija.\n1. Unos.\n2. Brisanje.\n3. Izmena.\n4. Vracanje u nazad")
    x = input("Unesite broj:  ")
    x = int(x)
    if x == 1:
        print("Izabrali ste opciju unos. ")
        fajlovi_unos()
    elif x == 2:
        print("Izabrali ste opciju brisanje. ")
        brisanje.brisanje()
    elif x == 3:
        print("Izabrali ste opciju izmena.")
        Izmena()
    elif x == 4:
        print("Vracanje unazad. ")
        menadzer()
    else:
        print("Morate izabrati jednu od ponudjenih opcija.")
        unos_brisanje_izmena()


def prodavac():
    print("")
    print(
        "Izaberite jednu od sledecih opcija ukucavanjem rednog broja.\n1. Izdavanje racuna.\n2. Pretraga.\n3. Nazad na logovanje")
    x = input("Unesite broj:  ")
    x = int(x)
    if x == 1:
        print("Izabrali ste opciju izdavanje racuna. ")
        izdavanje_racuna.izdavanje_racuna()
    elif x == 2:
        print("Izabrali ste opciju pretraga. ")
        Pretraga()
    elif x == 3:
        print("Nazad na logovanje.")
        logovanje()
    else:
        print("Morate izabrati jednu od ponudjenih opcija.")
        prodavac()


def menadzer():
    print("")
    print(
        "Izaberite jednu od sledecih opcija ukucavanjem rednog broja.\n1. Unos, izmena i brisanje podataka.\n2. Pretraga.\n3. Izvestaj(1).\n4. Izvestaj(2)\n5. Nazad na logovanje. ")
    x = input("Unesite broj:  ")
    x = int(x)
    if x == 1:
        print("Izabrali ste opciju Unos, izmena i brisanje podataka. ")
        unos_brisanje_izmena()
    elif x == 2:
        print("Izabrali ste opciju pretraga. ")
        Pretraga()
    elif x == 3:
        print("Izabrali ste izvestaj o prodaji po danima")
        izvestaj.izvestaj()
    elif x == 4:
        print("Izabrali ste izvestaj o prodaji po kategoriji")
        izvestaj2.izvestaj2()
    elif x == 5:
        print("Nazad na logovanje.")
        logovanje()
    else:
        print("Morate izabrati jednu od ponudjenih opcija.")
        menadzer()


def logovanje():
    print("")
    print("Unesite podatke kako bi se ulogovali.")
    print("")
    korisnicko_ime = input("Unesite korisnicko ime: ")
    lozinka = input("Unesite lozinku: ")
    korisnici = open("korisnici.txt", "r")
    sadrzaj = korisnici.readlines()
    korisnici.close()
    sss = False
    for linija in sadrzaj:
        username, name, lname, password, uloga, tip = linija.split("/")
        if (korisnicko_ime == username) and (lozinka == password):
            ulogovani_korisnik = username
            print("Uspesno ste se ulogovali kao " + uloga + " " + name + " " + lname + "!")
            Uloga_korisnika = uloga
            sss = True
    if sss == False:
        logovanje()
    elif Uloga_korisnika == "menadzer":
        with open("podaci.txt", "a") as korisnici:
            datum = time.strftime("%d-%m-%Y")
            vreme = time.strftime("%H:%M:%S")
            rezultat = ("\n" + ulogovani_korisnik + "/" + datum + "/" + vreme + "/" + "mrnandzer")
            korisnici.write(str(rezultat))
        menadzer()
    elif Uloga_korisnika == "prodavac":
        with open("podaci.txt", "a") as korisnici:
            datum = time.strftime("%d-%m-%Y")
            vreme = time.strftime("%H:%M:%S")
            rezultat = ("\n" + ulogovani_korisnik + "/" + datum + "/" + vreme + "/" + "prodavac")
            korisnici.write(str(rezultat))
        prodavac()
    else:
        print("nema ulogu ")
    print("Netacno uneseni podaci probajte opet. ")
    logovanje()


if __name__ == '__main__':
    print("SALON NAMESTAJA")
    logovanje()
