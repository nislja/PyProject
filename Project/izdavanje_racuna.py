#izdavanje racuna
import random
import time
import logovanje22


def izdavanje_racuna():
    datum = time.strftime("%d-%m-%Y")
    vreme = time.strftime("%H:%M:%S")

    korisnici = open("podaci.txt", "r")
    prodavci = korisnici.readlines()
    for podatak in prodavci:
        prodavac = podatak.split("/")
        prodavac = prodavac[0]


    fajl = open("namestaj.txt","r+")
    fajl_namestaj = fajl.readlines()
    rezultat_namestaj = []
    a_namestaj = []
    a_id = []
    a_cena = []
    a_kolicina = []
    a_kategorija = []
    suma = []


    print("Sifra   |Ime       |Boja        |Stanje    |Cena      |Kategorija   \n"
    "--------+----------+------------+----------+-----------+------------+")
    print("")
    for linija in fajl_namestaj:
        sifra, naziv, boja, stanje, cena, kategorija, tip = linija.split("/")
        red = linija.split("/")
        print("{0:8.10}|{1:10.10}|{2:12}|{3:10}|{4:10}|{5:13}".format( sifra, naziv, boja, stanje, cena, kategorija))
    print("")


    id = input("Unesi sifru namestaja: ")
    for linija in fajl_namestaj:
        sifra, naziv, boja, stanje, cena, kategorija, tip = linija.split("/")
        red = linija.split("/")
        while id  ==  sifra:
            kolicina = int(input("Unesite zeljenu kolicinu: "))
            while int(kolicina) > int(stanje):
                kolicina = input("Unesite raspolozivu zeljenu kolicinu: ")
                int(kolicina)
            stanje2 = int(stanje) - int(kolicina)
            red[3] = str(stanje2)
            a_namestaj.append(str(naziv))
            a_id.append(str(sifra))
            a_kolicina.append(str(kolicina))
            a_cena.append(cena)
            a_kategorija.append(kategorija)
            proba = (int(cena) * int(kolicina))
            suma.append(str(proba))
            cenaKrug = str(cena)
            nazivKrug = str(naziv)
            kategorijaKrug = str(kategorija)
            kolicinaKrug = str(kolicina)
            datumKrug = str(datum)
            print(cenaKrug, nazivKrug, kategorijaKrug, kolicinaKrug, datumKrug)
            izvestajkat = open("izvestavanje.txt", "a")
            izvestajkat.write(datumKrug +"/"+ kategorijaKrug +"/"+ nazivKrug +"/"+ cenaKrug+"/"+kolicinaKrug+"/"+str(proba)+ "\n")
            izvestajkat.close()
            id = input("unesi sifru namestaja za dalji unos, unos se prekida enterom: ")
        rezultat_namestaj.append("/".join(red))
    fajl.seek(0)
    fajl.truncate()
    fajl.writelines(rezultat_namestaj)
    fajl.close()
    suma = map(int, suma)
    suma = sum(suma)


    cena_usluga = []
    usluga = []
    suma1 = []
    fajl1 = open("Usluge-salona.txt", "r")
    fajl1_usluge = fajl1.readlines()
    fajl1.close()
    print("")
    print("Naziv        |cena        | \n""-------------+------------+")
    for linija in fajl1_usluge:
        naziv_usluge, opis, cena, tip = linija.split("/")
        print("{0:13}|{1:12}".format(naziv_usluge, str(cena)))
    ime = input("Ako kupac zeli neku uslugu ukucajte njen naziv ili kliknite enter: ")
    for linija in fajl1_usluge:
        naziv_usluge, opis, cena, tip = linija.split("/")
        while ime == naziv_usluge:
            print(ime, naziv_usluge)
            usluga.append(naziv_usluge)
            cena_usluga.append(cena)
            suma1.append((cena))
            ime = input("Unesite naziv usluge za dodavanje ili pritisnite enter: ")
    suma1 = map(int,suma1)
    suma1 = sum(suma1)
    cela_suma = (suma + suma1)


    brojracuna = open("Racuni.txt", "r")
    brojracuna = brojracuna.readlines()
    for brrc in brojracuna:
        brrc.split("/")
        br_racuna = brrc[0]
        if br_racuna == "":
            br_racuna = 0
        br_racuna = str(int(br_racuna) + 1)


    rezultat = (str(br_racuna)+"/"+str(prodavac)+"/"+datum+"/"+vreme+"/"+"$".join(a_namestaj)+"/"+"|".join(a_id)+"/"+"^".join(a_kolicina)+"/"+"*".join(a_cena)+"/"+"-".join(a_kategorija)+"/"+"(".join(cena_usluga)+"/"+"@".join(usluga)+"/"+str(cela_suma)+"/"+"False\n")
    with open("Racuni.txt", "a") as racuni:
        racuni.write(rezultat)


#PRINT Racuna
    izgled = open("Racuni.txt", "r")
    izgled = izgled.readlines()
    for racun in izgled:
        a_racun = racun.split("/")
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


    logovanje22.prodavac()