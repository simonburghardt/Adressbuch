import xml.etree.ElementTree as ET
ad_xml = "adresstest.xml"
root = ""

adressen = []


# lädt eine JSON-Datei und speichert die einträge in einem Dictionairy ab
def loadxml(diexml):
    tree = ET.parse(ad_xml)
    root = tree.getroot()
    mydict = {}
    childlist = []
    childdict = {}
    for child in root:
        for kind in child:
            if len(kind):
                for subchild in kind:
                    childdict = kind.attrib
                    childdict[subchild.tag] = subchild.text
                    childlist.append(childdict)
                mydict[kind.tag] = childlist
            else:
                mydict[kind.tag] = kind.text
    print(mydict)

    print("---------------------------------------------")
    print("Erfolgreich geladen!")
    print("---------------------------------------------")



# speichert das Dictionary in einer JSON-Datei
def savexml():
    root = ET.Element('Adressbuch')
    baum = ET.ElementTree(root)

    for data in adressen:
        kontakt = ET.SubElement(root, 'Kontakt')
        for key in data:
            if isinstance(data[key], list):
                d = data[key]
                for entry in d:
                    n = ET.SubElement(kontakt, key, {'Typ': entry['Typ']})
                    i = 0
                    for eintrag in entry:
                        if i == 1:
                            m = ET.SubElement(n, eintrag)
                            m.text = entry[eintrag]
                        i += 1
            else:
                child = ET.SubElement(kontakt, key)
                child.text = data[key]

    baum.write('adresstest.xml')

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
             "Name": name,
             "Vorname": vorname,
             "Strasse": straße,
             "Hausnummer": hausnummer,
             "PLZ": plz,
             "Stadt": stadt,
             "Rufnummern": [
                 {"Typ": "Telefon", "Nummer": telefon}, {"Typ": "Mobil", "Nummer": mobil}
             ],
             "E-Mail-Adressen": [
                 {"Typ": "Privat", "E-Mail": email_priv}, {"Typ": "Geschäftlich", "E-Mail": email_gesch}
             ]
             }

    print("---------------------------------------------")
    print("Erfolgreich hinzugefügt!")
    print("---------------------------------------------")
    adressen.append(liste)


# Zeigt einen einzelnen Eintrag aus der Textfile
def show_eintrag(n):
    right = 0
    try:
        for eintrag in adressen:
            if eintrag['Name'] == n:
                print(eintrag)
                right = True

        if right == False:
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
        daten = 0
        for eintrag in adressen:
            if eintrag['Name'] == name:
                daten = eintrag

        was = input("Was wollen sie ändern? Geben sie ein, welches Attribut sie ändern möchten! ")

        if was == "Rufnummern":
            welche = input("Welchen Nummer möchten sie ändern? ")
            if welche == "Telefon":
                new = input("Geben sie einen neuen Wert ein! ")
                daten["Rufnummern"][0]["Nummer"] = new
            elif welche == "Mobil":
                new = input("Geben sie einen neuen Wert ein! ")
                daten["Rufnummern"][1]["Nummer"] = new
            else:
                print("Eine solche Rufnummer ist nicht vorhanden")

        elif was == "E-Mail-Adressen":
            welche = input("Welchen E-Mail möchten sie ändern? ")
            if welche == "Privat":
                new = input("Geben sie einen neuen Wert ein! ")
                daten["E-Mail-Adressen"][0]["E-Mail"] = new
            elif welche == "Geschäftlich":
                new = input("Geben sie einen neuen Wert ein! ")
                daten["E-Mail-Adressen"][1]["E-Mail"] = new
            else:
                print("Eine solche Email ist nicht vorhanden")


        else:
            new = input("Geben sie einene neuen Wert ein! ")
            daten[was] = new

        # print("---------------------------------------------")
        # print("Erfolgreich geändert!")
        # print("---------------------------------------------")
        # show_eintrag(name)
        # print("---------------------------------------------")

    except:
        print("---------------------------------------------")
        print("Eingabe ungültig")
        print("---------------------------------------------")


# löscht einen Eintrag aus der Liste
def del_eintrag():
    show_list()
    name = input("Welchen Eintrag wollen sie löschen? Geben sie einen Namen ein! ")

    try:

        for eintrag in adressen:
            if eintrag['Name'] == name:
                adressen.remove(eintrag)

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

    for reihe in adressen:
        print(reihe)
        print()
        print("----------------------------------------------------------------------")
        print()


    print("----------------------------------------------------------------------")


entscheidung = 0
while (entscheidung != "8"):
    entscheidung = input("Was wollen sie machen?: \nDrücken sie die 1, um einen neuen Kontakt hinzuzufügen\n"
                         "Drücken sie die 2, um einen bestehenden Kontakt zu suchen\n"
                         "Drücken sie die 3, um einen bestehenden Kontakt zu ändern\n"
                         "Drücken sie die 4, um einen bestehenden Kontakt zu löschen\n"
                         "Drücken sie die 5, um alle Kontakte anzuzeigen\n"
                         "Drücken sie die 6, um eine XML-Datei zu laden\n"
                         "Drücken sie die 7, um die XML-Datei zu speichern\n"
                         "Drücken sie die 8, um das Programm zu beenden")

    if (entscheidung == "1"):
        add_eintrag()

    elif (entscheidung == "2"):
        name = input("Kontakt suchen: Geben sie einen vorhandenen Nachnamen an: ")
        show_eintrag(name)

    elif (entscheidung == "3") :
        change_eintrag()

    elif (entscheidung == "4") :
        del_eintrag()

    elif (entscheidung == "5"):
        show_list()

    elif (entscheidung == "6"):
        root = loadxml(ad_xml)

    elif (entscheidung == "7"):
        savexml()

    elif (entscheidung == "8"):
        break

    else:
        print("---------------------------------------------")
        print("Falsche Eingabe!")
        print("---------------------------------------------")
