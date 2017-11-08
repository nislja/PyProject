#brisanje
import logovanje22

def brisanje():
    print("")
    x = logovanje22.meni1()
    if x == 1:
        ime_fajla = "korisnici.txt"
        kljuc = input("Unestite korisnicko ime cije podatke zelite da obrisete: ")
    elif x == 2:
        ime_fajla = "kategorija.txt"
        kljuc = input("Unestite kategoriju namestaja za koju zelite da obrisete podatke: ")
    elif x == 3:
        ime_fajla = "namestaj.txt"
        kljuc = input("Unestite id namestaja cije podatke zelite da obrisete: ")
    elif x == 4:
        ime_fajla = "Usluge-salona.txt"
        kljuc = input("Unesite uslugu salona za koju zelite da obrisete podatke")
    elif x == 5:
        ime_fajla = "Racuni.txt"
        kljuc = input("Unesite id racuna koji zelite da obrisete: ")
    elif x == 6:
        print("Vracanje unazad. ")
        logovanje22.unos_brisanje_izmena()
    else:
        print("Morate izabrati jednu od ponudjenih opcija.")
        brisanje()

    fajl=open(ime_fajla,"r+")
    redovi = fajl.readlines()
    rezultat = []
    for red in redovi:
        red = red.split("/")
        id = red[0]
        if kljuc == id:
            red[-1] = "True\n"
        else:
            return
        rezultat.append("/".join(red))
    fajl.seek(0)
    fajl.truncate()
    fajl.writelines(rezultat)
    fajl.close()
    brisanje()
