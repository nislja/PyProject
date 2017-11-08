#pretraga
import logovanje22
from datetime import datetime

# PRETRAGA ZA RACUNE
def ime_prodavca():
    print("Izabrali ste pretragu po prodavcu koji je izdao racun")
    ime = input("Unesi ime prodavca: ")
    file = open("Racuni.txt", "r")
    file = file.readlines()
    for racuni in file:
        a_racun = racuni.split("/")
        br_racuna = a_racun[0]
        cela_suma = a_racun[-2]
        vreme = a_racun[3]
        datum = a_racun[2]
        prodavac = a_racun[1]
        namestaj = a_racun[4]
        id = a_racun[5]
        kolicina = a_racun[6]
        cena = a_racun[7]
        kategorija = a_racun[8]
        cena_usluga = a_racun[9]
        usluga = a_racun[10]
        if ime == prodavac:
            print("\n")
            print("\tSALON NAMESTAJA\n")
            print("Br. racuna:  ",br_racuna)
            print("-----------------------------------------------------")
            print("Stavke racuna:\n")
            print("Namestaj: ","     ".join(namestaj.split("$")))
            print("Sifra:    ","           ".join(id.split("|")))
            print("Kolicina: ","              ".join(kolicina.split("^")))
            print("Cena:     ","           ".join(cena.split("*")))
            print("-----------------------------------------------------")
            print("Usluge:        ","   ".join(usluga.split("@")))
            print("Cene usluga:   ","   ".join(cena_usluga.split("(")))
            print("\n\t----------------------------------------")
            print("Ukupno (bez PDV): ", cela_suma, "din.")
            print("Ukupno (sa PDV):  ", int(cela_suma) + (int(cela_suma) *2)/10, "din.")
            print("\t-----------------------------------------")
            print("Vreme racuna:     ", vreme)
            print("Datum racuna:     ", datum)
            print("Racun izdao:      ", prodavac)
            print("-----------------------------------------------------")
            print("\tHvala!")
            racuni_pretraga()

def naziv_racuna():
    namest = []
    print("Izabrali ste pretragu po namestaju")
    ime = input("Unesi naziv namestaja: ")
    file = open("Racuni.txt", "r")
    file = file.readlines()
    for racuni in file:
        a_racun = racuni.split("/")
        br_racuna = a_racun[0]
        cela_suma = a_racun[-2]
        vreme = a_racun[3]
        datum = a_racun[2]
        prodavac = a_racun[1]
        namestaj = a_racun[4]
        namestaj = namestaj.split("$")
        namest.append(namestaj())
        id = a_racun[5]
        kolicina = a_racun[6]
        cena = a_racun[7]
        kategorija = a_racun[8]
        cena_usluga = a_racun[9]
        usluga = a_racun[10]
        if ime in namest:
            print("\n")
            print("\tSALON NAMESTAJA\n")
            print("Br. racuna:  ",br_racuna)
            print("-----------------------------------------------------")
            print("Stavke racuna:\n")
            print("Namestaj: ","     ".join(namestaj.split("$")))
            print("Sifra:    ","           ".join(id.split("|")))
            print("Kolicina: ","              ".join(kolicina.split("^")))
            print("Cena:     ","           ".join(cena.split("*")))
            print("-----------------------------------------------------")
            print("Usluge:        ","   ".join(usluga.split("@")))
            print("Cene usluga:   ","   ".join(cena_usluga.split("(")))
            print("\n\t----------------------------------------")
            print("Ukupno (bez PDV): ", cela_suma, "din.")
            print("Ukupno (sa PDV):  ", int(cela_suma) + (int(cela_suma) *2)/10, "din.")
            print("\t-----------------------------------------")
            print("Vreme racuna:     ", vreme)
            print("Datum racuna:     ", datum)
            print("Racun izdao:      ", prodavac)
            print("-----------------------------------------------------")
            print("\tHvala!")
            racuni_pretraga()

def broj_racuna():
    print("Izabrali ste pretragu po broju racuna")
    ime = input("Unesi broj racuna: ")
    file = open("Racuni.txt", "r")
    file = file.readlines()
    for racuni in file:
        a_racun = racuni.split("/")
        br_racuna = a_racun[0]
        cela_suma = a_racun[-2]
        vreme = a_racun[3]
        datum = a_racun[2]
        prodavac = a_racun[1]
        namestaj = a_racun[4]
        id = a_racun[5]
        kolicina = a_racun[6]
        cena = a_racun[7]
        kategorija = a_racun[8]
        cena_usluga = a_racun[9]
        usluga = a_racun[10]
        if ime == br_racuna:
            print("\n")
            print("\tSALON NAMESTAJA\n")
            print("Br. racuna:  ",br_racuna)
            print("-----------------------------------------------------")
            print("Stavke racuna:\n")
            print("Namestaj: ","     ".join(namestaj.split("$")))
            print("Sifra:    ","           ".join(id.split("|")))
            print("Kolicina: ","              ".join(kolicina.split("^")))
            print("Cena:     ","           ".join(cena.split("*")))
            print("-----------------------------------------------------")
            print("Usluge:        ","   ".join(usluga.split("@")))
            print("Cene usluga:   ","   ".join(cena_usluga.split("(")))
            print("\n\t----------------------------------------")
            print("Ukupno (bez PDV): ", cela_suma, "din.")
            print("Ukupno (sa PDV):  ", int(cela_suma) + (int(cela_suma) *2)/10, "din.")
            print("\t-----------------------------------------")
            print("Vreme racuna:     ", vreme)
            print("Datum racuna:     ", datum)
            print("Racun izdao:      ", prodavac)
            print("-----------------------------------------------------")
            print("\tHvala!")
            racuni_pretraga()

def datum_izdavanja():
    print("Izabrali ste pretragu po datumu")
    print("")
    datum01 = input("Unesi datum pocetka za izvestaj u formatu 18-01-2015: ")
    datum02 = input("Unesi datum kraja za izvestaj u formatu 18-01-2015: ")
    try:
        datum1 = datetime.strptime(datum01,"%d-%m-%Y")
        datum2 = datetime.strptime(datum02,"%d-%m-%Y")
    except:
        print("Pogresan format datuma.")
        racuni_pretraga()

    ime = input("Unesi ime prodavca: ")
    file = open("Racuni.txt", "r")
    file = file.readlines()
    for racuni in file:
        a_racun = racuni.split("/")
        br_racuna = a_racun[0]
        cela_suma = a_racun[-2]
        vreme = a_racun[3]
        datum = a_racun[2]
        datum = datetime.strptime(datum,"%d-%m-%Y")
        prodavac = a_racun[1]
        namestaj = a_racun[4]
        id = a_racun[5]
        kolicina = a_racun[6]
        cena = a_racun[7]
        kategorija = a_racun[8]
        cena_usluga = a_racun[9]
        usluga = a_racun[10]
        if datum >= datum1 and datum <= datum2:
            print("\n")
            print("\tSALON NAMESTAJA\n")
            print("Br. racuna:  ",br_racuna)
            print("-----------------------------------------------------")
            print("Stavke racuna:\n")
            print("Namestaj: ","     ".join(namestaj.split("$")))
            print("Sifra:    ","           ".join(id.split("|")))
            print("Kolicina: ","              ".join(kolicina.split("^")))
            print("Cena:     ","           ".join(cena.split("*")))
            print("-----------------------------------------------------")
            print("Usluge:        ","   ".join(usluga.split("@")))
            print("Cene usluga:   ","   ".join(cena_usluga.split("(")))
            print("\n\t----------------------------------------")
            print("Ukupno (bez PDV): ", cela_suma, "din.")
            print("Ukupno (sa PDV):  ", int(cela_suma) + (int(cela_suma) *2)/10, "din.")
            print("\t-----------------------------------------")
            print("Vreme racuna:     ", vreme)
            print("Datum racuna:     ", datum)
            print("Racun izdao:      ", prodavac)
            print("-----------------------------------------------------")
            print("\tHvala!")
            racuni_pretraga()

def racuni_pretraga():
    print("")
    print("Pretrazi racune po:\n1. Prodavcu koji ga je izdao\n2. Nazivu Namestaja\n3. Broju racuna\n4. Datum izdavanja")
    x = input("Unesite broj zeljenog nacina pretrazivanja: ")
    int(x)
    if x == "1":
        ime_prodavca()
    elif x == "2":
        naziv_racuna()
    elif x == "4":
        broj_racuna()
    elif x == "3":
        datum_izdavanja()


# PRETRAGA ZA USLUGE

def naziv_usluga_pretraga():
    print("")
    usluga = open("Usluge-salona.txt","r")
    sadrzaj = usluga.readlines()
    usluga.close()
    print("Izabrali ste pretragu po nazivu.")
    ime = input("Unesite naziv usluge: ")
    for linija in sadrzaj:
        naziv, opis, cena, tip = linija.split("/")
        red = linija.split("/")
        if naziv == ime:
            print("Naziv   |Opis                    |Cena        \n"
            "--------+------------------------+------------+")
            print("{0:8}|{1:24.24}|{2:16.12}".format( naziv, opis, cena))
    usluga_pretraga()


def cena_usluga_pretraga():
    print("")
    usluga = open("Usluge-salona.txt","r")
    sadrzaj = usluga.readlines()
    usluga.close()
    print("Izabrali ste pretragu po opsegu cene.")
    cena_min = input("Unesite minimalnu cenu usluge: ")
    cena_max = input("Unesite maksimalnu cenu usluge: ")
    for linija in sadrzaj:
        naziv, opis, cena, tip = linija.split("/")
        red = linija.split("/")
        if int(cena) >= int(cena_min) and int(cena) <= int(cena_max):
            print("Naziv   |Opis                    |Cena        \n"
            "--------+------------------------+------------+")
            print("{0:8}|{1:24.24}|{2:16.12}".format( naziv, opis, cena))
    usluga_pretraga()


def usluga_pretraga():
    print("")
    print("Izaberite jednu od opcija.\n1. Pretraga po nazivu.\n2. Pretraga po opsegu cene.\n3. Vracanje u nazad.")
    x = input("Unesite broj zljenog nacina pretrazivanja: ")
    x = int(x)
    if x == 1:
        naziv_usluga_pretraga()
    elif x == 2:
        cena_usluga_pretraga()
    elif x == 3:
        print("Vracanje u nazad. ")
        return logovanje22.Pretraga()
    else:
        print("Morate izabrati jednu od ponudjenih opcija.")
        usluga_pretraga()


# PRETRAGA ZA NAMESTAJ

def namestaj():
    print("")
    namestaj = open("namestaj.txt","r")
    sadrzaj = namestaj.readlines()
    namestaj.close()
    return(sadrzaj)


def pretraga_naziv():
    print("")
    sadrzaj = namestaj()
    print("Izabrali ste pretragu po nazivu.")
    naziv = input("Unesite naziv namestaja: ")
    for linija in sadrzaj:
        sifra, ime, boja, stanje, cena, kategorija, tip = linija.split("/")
        red = linija.split("/")
        if naziv == ime:
            print("Sifra   |Ime       |Boja        |Stanje    |Cena      |Kategorija   |\n"
            "--------+----------+------------+----------+-----------+------------+")
            print("{0:8}|{1:10.10}|{2:12.12}|{3:10.10}|{4:10.10}|{5:13.10}|".format( sifra, ime, boja, stanje, cena, kategorija))
    namestaj_pretraga()


def pretraga_cena():
    print("")
    sadrzaj = namestaj()
    print("Izabrali ste pretragu po opsegu cene.")
    min_cena = input("Unesite minimalnu cenu: ")
    max_cena = input("Unesite maksimalnu cenu: ")
    print("Sifra   |Ime       |Boja        |Stanje    |Cena      |Kategorija   \n"
    "--------+----------+------------+----------+-----------+------------+")
    for linija in sadrzaj:
        sifra, ime, boja, stanje, cena, kategorija, tip = linija.split("/")
        red = linija.split("/")
        if int(cena) >= int(min_cena) and int(cena) <= int(max_cena):
            print("{0:8.8}|{1:10.10}|{2:12.12}|{3:10.10}|{4:10.10}|{5:13.13}".format( sifra, ime, boja, stanje, cena, kategorija))
    namestaj_pretraga()


def pretraga_kolicina():
    print("")
    sadrzaj = namestaj()
    print("Izabrali ste pretragu kolicini")
    kolicina = input("Unesite kolicinu namestaja: ")
    print("Sifra   |Ime       |Boja        |Stanje    |Cena      |Kategorija   \n"
    "--------+----------+------------+----------+----------+------------+")
    for linija in sadrzaj:
        sifra, ime, boja, stanje, cena, kategorija, tip = linija.split("/")
        red = linija.split("/")
        if int(stanje) == int(kolicina):
            print("{0:8.8}|{1:10.10}|{2:12.12}|{3:10.10}|{4:10.10}|{5:13.13}".format( sifra, ime, boja, stanje, cena, kategorija))
    namestaj_pretraga()


def pretraga_sifra():
    print("")
    sadrzaj = namestaj()
    print("Izabrali ste pretragu po sifri namestaja")
    id = input("Unesite sifru namestaja: ")
    for linija in sadrzaj:
        sifra, ime, boja, stanje, cena, kategorija, tip = linija.split("/")
        red = linija.split("/")
        if sifra == id:
            print("Sifra   |Ime       |Boja        |Stanje    |Cena      |Kategorija   \n"
            "--------+----------+------------+----------+----------+------------+")
            print("{0:8.10}|{1:10.10}|{2:12}|{3:10}|{4:10}|{5:13}".format( sifra, ime, boja, stanje, cena, kategorija))
    namestaj_pretraga()


def namestaj_pretraga():
    print("")
    print("Izaberite jednu od opcija.\n1. Pretraga po nazivu.\n2. Pretraga po opsegu cene.\n3. Pretraga po kolicini.\n4. Pretraga po sifri namestaja.\n5. Vracanje u nazad.")
    x = input("Unesite broj zeljenog nacina pretrazivanja: ")
    x = int(x)
    if x == 1:
        pretraga_naziv()
    elif x == 2:
        pretraga_cena()
    elif x == 3:
        pretraga_kolicina()
    elif x == 4:
        pretraga_sifra()
    elif x == 5:
        print("Vracanje u nazad. ")
        logovanje22.Pretraga()
    else:
        print("Morate izabrati jednu od ponudjenih opcija.")
        namestaj_pretraga()
