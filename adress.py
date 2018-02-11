import json
from tinydb import TinyDB, Query

ad_json = "adressen.json"
db = TinyDB('db.json')
adressen = Query()


# lädt eine JSON-Datei und speichert die einträge in einem Dictionairy ab
def loadjson(diejson):
    fh = open(diejson, mode="r", encoding="utf8")
    mystring = json.load(fh)
    for entry in mystring:
        adressen.append(entry)

    print("---------------------------------------------")
    print("Erfolgreich geladen!")
    print("---------------------------------------------")


# speichert das Dictionary in einer JSON-Datei
def savejson(diejson):
    fh = open(diejson, mode="w", encoding="utf8")
    json.dump(adressen, fh, indent=4)
    print("---------------------------------------------")
    print("Erfolgreich gespeichert!")
    print("---------------------------------------------")


# Fügt einen Eintrag zum einkaufszettel.txt hinzu
def add_eintrag():
    print("Sie legen einen neuen Kontakt an!\n-----------------------------------\n")
    anrede = input("Anrede: ")
    name = input("Name: ")
    vorname = input("Vorname: ")
    straße = input("Straße: ")
    hausnummer = input("Hausnummer: ")
    plz = input("Postleitzahl: ")
    stadt = input("Stadt: ")
    print("Telefonnummern:")
    telefon = input("Telefon: ")
    mobil = input("Mobil: ")
    print("Emailadressen:")
    email_priv = input("E-Mail privat: ")
    email_gesch = input("E-Mail geschäftlich: ")

    liste = {"Anrede": anrede,
             "Name" : name,
             "Vorname": vorname,
             "Strasse": straße,
             "Hausnummer": hausnummer,
             "PLZ": plz,
             "Stadt": stadt,
             "Rufnummern": [
                 {"Typ": "Telefon", "Nummer": telefon}, {"Typ": "Mobil", "Nummer" : mobil}
             ],
             "E-Mail-Adressen": [
                 {"Typ": "Privat", "E-Mail": email_priv}, {"Typ": "Geschäftlich", "E-Mail": email_gesch}
             ]
             }
    db.insert(liste)

    print("---------------------------------------------")
    print("Erfolgreich hinzugefügt!")
    print("---------------------------------------------")


# Zeigt einen einzelnen Eintrag aus der Textfile
def show_eintrag(n):
    try:
        found = False
        for eintrag in db.search(adressen['Name'].search(n)):
            print(eintrag)
            found = True

        if found == False:
            print("Nichts gefunden")



        print("---------------------------------------------")

    except:
        print("---------------------------------------------")
        print("Eintrag ist nicht zulässig oder nicht in der Liste.")
        print("---------------------------------------------")

# ändert den Eintrag und überschreibt den alten
def change_eintrag():
    print("---------------------------------------------------------")
    show_list()
    print("---------------------------------------------------------")

    name = input("Welche Adresse möchten sie ändern? Geben sie den Namen an! ")

    try:
        for eintrag in db.search(adressen['Name'].search(name)):
            show_eintrag(name)
            was = input("Was wollen sie ändern? Geben sie ein, welches Attribut sie ändern möchten! ")
            print(eintrag[was])

        new = input("Geben sie einene neuen Wert ein! ")

        db.update({was: new}, adressen['Name'].search(name))

        show_eintrag(name)

    except:
        print("---------------------------------------------")
        print("Eingabe ungültig")
        print("---------------------------------------------")


# löscht einen Eintrag aus der Liste
def del_eintrag():
    show_list()
    name = input("Welchen Eintrag wollen sie löschen? Geben sie einen Namen ein! ")

    try:

        db.remove(adressen['Name'].search(name))

        print("---------------------------------------------")
        print("Eintrag erfolgreich gelöscht!")
        print("---------------------------------------------")


    except:
        print("---------------------------------------------")
        print("Eintrag ist nicht in der Liste oder ungültig. ")
        print("---------------------------------------------")


# zeigt die komplette Liste an
def show_list():
    print("----------------------------------------------------------------------")

    for entry in db.all():
        print(entry)
        print()
        print("----------------------------------------------------------------------")
        print()

    print("----------------------------------------------------------------------")


entscheidung = 0
while (entscheidung != "10"):
    entscheidung = input("Was wollen sie machen?: \nDrücken sie die 1, um einen neuen Kontakt hinzuzufügen\n"
                         "Drücken sie die 2, um einen bestehenden Kontakt zu suchen\n"
                         "Drücken sie die 3, um einen bestehenden Kontakt zu ändern\n"
                         "Drücken sie die 4, um einen bestehenden Kontakt zu löschen\n"
                         "Drücken sie die 5, um alle Kontakte anzuzeigen\n"
                         "Drücken sie die 8, um eine JSON-Datei zu laden\n"
                         "Drücken sie die 9, um die JSON-Datei zu speichern\n"
                         "Drücken sie die 10, um das Programm zu beenden")


    if (entscheidung == "1"):
        add_eintrag()


    elif (entscheidung == "2"):
        name = input("Kontakt suchen: Geben sie einen vorhandenen Nachnamen an: ")
        show_eintrag(name)


    elif (entscheidung == "3") :
        change_eintrag()


    elif (entscheidung == "4") :
        del_eintrag()


    elif (entscheidung == "5") :
        show_list()


    # beendet das Programm
    elif (entscheidung == "8") :
        loadjson(ad_json)


    elif (entscheidung == "9"):
        savejson(ad_json)


    elif (entscheidung == "10"):
        break


    else :
        print("---------------------------------------------")
        print("Falsche Eingabe!")
        print("---------------------------------------------")
