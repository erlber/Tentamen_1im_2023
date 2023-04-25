import time
import datetime

def space(num):
    for _ in range(num):
        print("")

medlemmer = [[101, "Finn Olav", "Konan", "2023-05-01", True], [102, "Magnar", "Rabliås", "2022-09-12", False], [103, "Arne-Jhonny", "Benz", "2023-01-31", True]]
# index      | 0 |      1     |    2   |      3      |  4  |  | 0 |      1     |    2   |      3     |   4  |  | 0  |      1      |    2   |      3      |  4  |
# 0 = ID
# 1 = Fornavn
# 2 = Etternavn
# 3 = Registreringsdato
# 4 = aktivt medlemskap True/False

def hovedMeny():
    print("|---- Medlemsregister for Tores Gym ----|")
    print("|                                       |")
    print("|-----------------|MENY|----------------|")
    print("| 1. Legg til nytt medlem               |")
    print("| 2. Rediger medlem                     |")
    print("| 3. Slett medlem                       |")
    print("| 4. List ut alle medlemer              |")    
    print("| 5. søk etter medlem                   |")
    print("| 0. Avslutt program                    |")
    print("|---------------------------------------|")
    valg = input("  Velg ett nummer fra menyen: ")
    return valg

def leggTilMedlem():
    space(50)
    print("|-------- Legg til nytt medlem ---------|")
    print("|                                       |")
    forNavn = input("| Fornanvn: ")
    etterNavn = input("| Fornanvn: ")
    regDato = str(datetime.date.today())
    aktiv = input("| Aktiver medlemskapet? y/n: ")
    if aktiv == "y":
        aktiv = True
    else:
        aktiv = False
    
    id = 0
    for medlem in medlemmer:
        if id < medlem[0]:
            id = medlem[0] + 1
    
    nyttMedlem = [id, forNavn, etterNavn, regDato, aktiv]
    medlemmer.append(nyttMedlem)

    listUtMedlemer(2, [nyttMedlem])
    print("| Er vellykket registrert i Tores medlemsregisster")
    input("| Trykke enter for å gå tilbake til hovedmeny: ")

    return ""


def listUtMedlemmer(versjon, medlemsliste = medlemmer):
    space(2)
    if versjon == 1:
        for medlem in medlemsliste:
            print(f"| ID: {medlem[0]}")
            time.sleep(0.2)
            print(f"| Fornanvn: {medlem[1]}")
            time.sleep(0.2)
            print(f"| Etternavn: {medlem[2]}")
            time.sleep(0.2)
            print(f"| Registrert: {medlem[3]}")
            time.sleep(0.2)
            if medlem[4]:
                print(f"| Medlamskap: Aktivt")
            else:
                print(f"| Medlamskap: Deaktivert")
            space(1)
            time.sleep(0.5)
        space(1)
        input("Trykke en enter for å gå tilbake til hovedmeny: ")

    elif versjon == 2:
        for medlem in medlemsliste:
            print(f"| ID: {medlem[0]} Navn: {medlem[1]} {medlem[2]}")
            time.sleep(0.2)
    
    return ""

def redigerMedlem():
    space(50)
    while True:
        print("|------------|Rediger medlem|-----------|")
        print("|                                       |")
        print("| 1. tast inn id for å redigere medlem  |")
        print("| 2. skriv ut alle medlemmer med id     |")
        print("| 0. Tilbake til hovedmeny              |")
        print("|---------------------------------------|")
        valg = input("  Velg ett nummer fra menyen: ")
        space(1)

        if valg == "1":
            id = input("   skriv inn id på medlem: ")
            for medlem in medlemmer:
                if medlem[0] == int(id):

                    forNavn = input("Skriv inn nytt fornavn eller trykk enter for å skip: ")
                    if forNavn:
                        medlem[1] = forNavn

                    etterNavn = input("Skriv inn nytt etternavn eller trykk enter for å skip: ")
                    if etterNavn:
                        medlem[2] = etterNavn
                    
                    while True:
                        aktiv = input("sett medlemskap til aktivt y/n eller trykke enter for å skip: ")
                        if aktiv == "y":
                            medlem[4] = True
                            break
                        elif aktiv == "n":
                            medlem[4] = False
                            break
                        elif not aktiv:
                            break
                        else:
                            print("Ugyldig innput value, velg 'y' eller 'n' ")
                            space(1)

        elif valg == "2":
            listUtMedlemmer(2)
        
        elif valg == "0":
            break

    return ""


def slettMedlem():
    #din kode hær
    pass


def søkEtterMedlem():
    søkeListe = []
    navn = input("  Navn på medlem du ønsker å søke etter: ").lower()
    for medlem in medlemmer:
        if navn in medlem[1].lower() or navn in medlem[2].lower():
            søkeListe.append(medlem)
    
    listUtMedlemer(1, søkeListe)


def main():
    run = True
    valg = ""
    while run:
        if valg == "0":
            break
        
        elif valg == "1":
            valg = leggTilMedlem()

        elif valg == "2":
            valg = redigerMedlem()

        elif valg == "3":
            valg = slettMedlem()

        elif valg == "4":
            valg = listUtMedlemmer(1)

        elif valg == "5":
            valg = søkEtterMedlem()

        else:
            valg = hovedMeny()
    
main()