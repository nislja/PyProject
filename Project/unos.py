#unos
import logovanje22

def usluga_unos():
    print("Izabrali ste fajl Usluge-salona. ")
    naziv = input("Unesite naziv usluge: ")
    opis = input("Unesite opis usluge: ")
    cena = input("Unesite cenu usluge: ")
    tip = ("False")
    usluge_salona = open("Usluge-salona.txt","r")
    sadrzaj = usluge_salona.readlines()
    usluge_salona.close()
    for linija in sadrzaj:
        linija = linija.split("/")
        name = linija[0]
        while naziv == name:
            print("Ova usluga vec postoji ukucajte drugu")
            naziv = input("Unesite sifru opet:")
    rezultat = ("\n"+naziv+"/"+opis+"/"+cena+"/"+tip)
    with open("Usluge-salona.txt", "a") as usluge:
        usluge.write(str(rezultat))
    logovanje22.fajlovi_unos()


def namestaj_unos():
    print("")
    print("Izabrali ste fajl namestaj. ")

    brojnamestaja = open("namestaj.txt", "r")
    brojnamestaja = brojnamestaja.readlines()
    sifra=0
    for brnm in brojnamestaja:
        brnm.split("/")
        sifra+=1
    naziv = input("Unesite naziv: ")
    boja = input("Unesite boju: ")
    kolicina = input("Unesite kolicinu: ")
    cena = input("Unesite cenuu: ")
    katnam = input("Unesite kategoriju namestaja: ")
    tip = ("False")
    namestaj = open("namestaj.txt","r")
    sadrzaj = namestaj.readlines()
    namestaj.close()
    rezultat = (str(sifra)+"/"+naziv+"/"+boja+"/"+kolicina+"/"+cena+"/"+katnam+"/"+tip+"\n")
    with open("namestaj.txt", "a") as namestaj:
        namestaj.write(str(rezultat))
    logovanje22.fajlovi_unos()


def kategorija_unos():
    print("")
    print("Izabrali ste fajl kategorija. ")
    name = input("Unesite naziv kategorije: ")
    opis = input("Unesite opis kategorije: ")
    tip = ("False")
    kategorija = open("kategorija.txt","r")
    sadrzaj = kategorija.readlines()
    kategorija.close()
    for linija in sadrzaj:
        linija = linija.split("/")
        id = linija[0]
        while name == id:
            print("Ne mozete uneti vec postojecu kategoriju! ")
            name = input("Unesite novi naziv kategorije :")
    rezultat = ("\n"+name+"/"+opis+"/"+tip)
    with open("kategorija.txt", "a") as kategorija:
        kategorija.write(str(rezultat))
    logovanje22.fajlovi_unos()


def korisnici_unos():
    print("")
    print("Izabrali ste fajl korisnici. ")
    name = input("Unesi ime za novog korisnika: ")
    lname = input("Unesi prezime: ")
    password = input("Unesi lozinku: ")
    uloga = input("Unesi ulogu, prodavac ili menadzer. ")
    while uloga != "prodavac" and uloga != "menadzer":
        uloga = input("ukucajte prodavac ili menadzer")
    tip = ("False")
    korisnicko_ime = input("Unesite korisnicko ime: ")
    korisnici = open("korisnici.txt","r")
    sadrzaj = korisnici.readlines()
    korisnici.close()
    for linija in sadrzaj:
        linija = linija.split("/")
        username = linija[0]
        while korisnicko_ime == username:
            korisnicko_ime = input("Vec zauzeto kucaj opet: ")
    rezultat = ("\n"+korisnicko_ime+"/"+name+"/"+lname+"/"+password+"/"+uloga+"/"+tip)
    with open("korisnici.txt", "a") as korisnici:
        korisnici.write(str(rezultat))

    logovanje22.fajlovi_unos()
