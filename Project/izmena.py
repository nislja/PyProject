#izmena
import logovanje22

def usluga_izmena():
    ime = input("Unesite naziv usluge: ")
    print("\nAko neki poatak ne zelite da menjate samo pritisnite enter.\n")
    fajl = open("Usluge-salona.txt","r+")
    redovi = fajl.readlines()
    rezultat = []
    for red in redovi:
        naziv, opis, cena, tip = red.split("/")
        red = red.split("/")
        if naziv == ime:
            print("Naziv   |Opis                    |Cena        |Tip               \n"
            "--------+------------------------+------------+-----------------+")
            print("{0:8}|{1:24}|{2:12}|{3:6}".format( naziv, opis, cena, tip))
            naziv = red[0]
            red[0] = naziv
            opis = input("Unesite novi opis: ")
            if opis == "":
                opis = red[1]
                red[1] = opis
            cena = input("Unesite cenu: ")
            if cena == "":
                cena = red[2]
            red[2] = cena
            tip = "False"
            red[3] = tip
        rezultat.append("/".join(red))
    fajl.seek(0)
    fajl.truncate()
    fajl.writelines(rezultat)
    fajl.close()
    logovanje22.Izmena()


def namestaj_izmena():
    print("")
    id = input("Unesite ID namestaja cije podatke zelite da menjate: ")
    print("\nAko neki poatak ne zelite da menjate samo pritisnite enter.\n")
    fajl = open("namestaj.txt","r+")
    redovi = fajl.readlines()
    rezultat = []
    for red in redovi:
        sifra, naziv, boja, kolicina, cena, kategorija, tip = red.split("/")
        red = red.split("/")
        if id == sifra:
            print("Sifra   |Ime       |Boja        |Stanje    |Cena      |Kategorija   |Tip               \n"
            "--------+----------+------------+----------+-----------+------------+-----------------+")
            print("{0:8.10}|{1:10.10}|{2:12}|{3:10}|{4:10}|{5:13}|{6:20}".format( sifra, naziv, boja, kolicina, cena, kategorija, tip))
            red[0] = id
            naziv = input("Unesite novi naziv: ")
            if naziv == "":
                naziv = red[1]
            red[1] = naziv
            boja = input("Unesite boju namestaja: ")
            if boja == "":
                boja = red[2]
            red[2] = boja
            kolicina = input("Unesite kolicinu: ")
            if kolicina == "":
                kolicina = red[3]
            red[3] = kolicina
            cena = input("Unesite cenu: ")
            if cena == "":
                cena = red[4]
            red[4] = cena
            red[5] = kategorija
            tip = "False\n"
            red[6] = tip
        rezultat.append("/".join(red))
    fajl.seek(0)
    fajl.truncate()
    fajl.writelines(rezultat)
    fajl.close()
    logovanje22.Izmena()


def kategorija_izmena():
    print("")
    ime = input("Unesite naziv kategorije cije podatke zelite da menjate: ")
    print("\nAko neki poatak ne zelite da menjate samo pritisnite enter.\n")
    fajl = open("kategorija.txt","r+")
    redovi = fajl.readlines()
    rezultat = []
    for red in redovi:
        naziv, opis, tip = red.split("/")
        red = red.split("/")
        if ime == naziv:
            print("Naziv    |Opis                   |Tip               \n"
            "--------+------------------------+-----------------+")
            print("{0:8}|{1:24.24}|{2:6}".format( naziv, opis, tip))
            red[0] = naziv
            opis = input("Unesite novi opis: ")
            if opis == "":
                opis = red[1]
            red[1] = opis
            tip = "False\n"
            red[2] = tip
        rezultat.append("/".join(red))
    fajl.seek(0)
    fajl.truncate()
    fajl.writelines(rezultat)
    fajl.close()
    logovanje22.Izmena()


def korisnici_izmena():
    print("")
    korisnicko_ime = input("Unesite korisnicko ime korisnika cije podatke zelite da menjate: ")
    print("\nAko neki poatak ne zelite da menjate samo pritisnite enter.\n")
    fajl=open("korisnici.txt","r+")
    redovi = fajl.readlines()
    rezultat = []
    for red in redovi:
        username, name, lname, password, uloga, tip = red.split("/")
        red = red.split("/")
        if korisnicko_ime == username:
            print("Sifra    |Ime       |Boja        |Stanje    |Cena      |Tip               \n"
            "---------+----------+------------+----------+----------+-----------------+")
            print("{0:8.10}|{1:10.10}|{2:12}|{3:10}|{4:10}|{5:20}".format( username, name, lname, password, uloga, tip))
            red[0] = username
            ime = input("Unesite novo ime: ")
            if ime == "":
                ime = red[1]
            red[1] = ime
            prezime = input("Unesite novo prezime: ")
            if prezime == "":
                prezime = red[2]
            red[2] = prezime
            sifra = input("Unesite novu sifru: ")
            if sifra == "":
                sifra = red[3]
            red[3] = sifra
            uloga = input("Unesite ulogu: ")
            while uloga != "prodavac" and uloga != "menadzer" and uloga!= "":
                uloga = input("Ukucajte prodavac ili menadzer: ")
            if uloga == "":
                uloga = red[4]
            red[4] = uloga
            tip = "False\n"
            red[5] = tip
        rezultat.append("/".join(red))
    fajl.seek(0)
    fajl.truncate()
    fajl.writelines(rezultat)
    fajl.close()
    logovanje22.Izmena()
