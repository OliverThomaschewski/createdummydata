from asyncio.windows_events import NULL
from numbers import Number
from operator import length_hint
from pickle import FALSE
import random
from xmlrpc.client import DateTime
import pandas as pd
import numpy as np
from random import choice, randint, randrange
from datetime import timedelta
from datetime import datetime
from datetime import date

"""
HINWEISE:

Values der Dictinarys müssen immer als Liste angebeben werden, sonst funktioniert die Iteration
beim erstellen der Querys nicht richtig
"""


def random_date():
    """
    Erstellt ein zufälliges Datum zwischen dem start und endwert
    """
    start_date = date(2022, 1, 1)
    end_date = date(2022, 6, 5)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + timedelta(days=random_number_of_days)
    return random_date


plz = {
    "plz_id": [1, 2, 3, 4, 5],
    "plz": [14059, 10587, 10407, 10243, 78762],
    "stadt": ["Berlin", "Berlin", "Berlin", "Berlin", "Konstanz"],
}

kontaktdaten = {
    "kontaktdaten_id": [1, 2, 3, 4, 5, 6, 7],
    "vorzuname": ["Oliver Thomaschewski", "myLeo GmbH", "Lieblingsgym CrossFit", "Evope GmbH", "Max Mustermann", "John Doe", "Alice Wonderland"],
    "straße": ["Christstr. 29a", "Franklinstr. 10", "Sophie-Charlotten-Str. 5", "Storkower Strasse 105", "Musterstr. 1", "Reuterstr. 34", "Breslauerstr.3"],
    "plz_id": [1, 2, 1, 4, 3, 5, 1],
    "email": ["o.thomaschewski@gmail.com", "mail@myleo.de", "mail@lieblingsgymcrossfit.de", "germain@evope.com", "Muster@muster.de", "doe@doe.de", "wonder@land.de"]
}

studio = {
    "studio_id": [1, 2, 3],
    "kontaktdaten_id": [2, 3, 4],
    "ansprechperson": ["Lea Löhr", "Simon Keppler", "Germain Wagner"]
}

rechnungssteller = {
    "rechnungssteller_id": [1],
    "kontaktdaten_id": [1],
    "iban": ["de123456789"],
    "steuer_nr": ["20383/349"]
}

# Für fie Rechnungen erstelle ich ein zufälliges Rechnungsdatum
# und wähle den boolean für bezahlt oder nicht zufällig aus

rechnungsdatum = []
bezahlteRechnungen = []


for i in range(100):
    rechnungsdatum.append(random_date())
    bezahlteRechnungen.append(randint(0, 1))

rechnungen = {
    # erstellt Liste mit ganzen Zahlen von 1 bis 100
    "rechnungs_nr": np.arange(1, 101, 1),
    # erstellt Liste mit 100 Einsen (da die rechnungssteller_id eh immer 1 ist.)
    "rechnungssteller_id": np.ones(100),
    "datum": rechnungsdatum,
    "bezahlt": bezahlteRechnungen
}

geraetetyp = {
    "geraetetyp_id": [1, 2],
    "bezeichnung": ["Rower", "BikeErg"]
}

geraete = {
    "serien_nr": ["12345", "923047", "392732"],
    "geraetetyp_id": [1, 1, 2],
    "wochenpreis": [20, 20, 20]
}

schaeden = {

    "schaden:id": [1, 2, 3],
    "serien_nr": ["12345", "923047", "392732"],
    "beschreibung": ["Kratzer am Display", "Schraube fehlt", "Lauffläche vorne zerkratzt"]
}

ausleiher = {
    "ausleiher_id": [1, 2, 3],
    "kontakdaten_id": [5, 6, 7]
}


# Der Einfachheit halber erstelle ich Ausleihen, die immer nur eine Woche gehen.
# Das Enddatum der einen Ausleihe +1 ist das Startdatum der nächsten

ausleihe_id = []
startdatum = []
enddatum = []
kontaktdaten_id = []
rechnungs_nr = []

sDate = date(2022, 1, 1)
for i in range(50):

    ausleihe_id.append(i+1)

    startdatum.append(sDate)
    eDate = sDate + timedelta(days=7)
    enddatum.append(eDate)
    sDate = eDate + timedelta(days=1)

    kontaktdaten_id.append(choice(ausleiher.get("ausleiher_id")))
    rechnungs_nr.append(rechnungen.get("rechnungs_nr")[i])

ausleihe = {
    "ausleihe_id": ausleihe_id,
    "startdatum": startdatum,
    "enddatum": enddatum,
    "kontaktdaten_id": kontaktdaten_id,
    "rechnungs_nr": rechnungs_nr
}

"""
 Zu den 50 Ausleihen werden 75 Ausleiheninhalte erstellt
 Durch den cast in ein Set werden duplikate entfernt, die Schleife läuft dann solange, 
 bis 75 einmalige Tuples vorhanden sind.
 Wird i größer als die Anzahl der Ausleihen wird i auf 0 gesetzt um die Liste der Ausleihen
 von vorne zu durchlaufen und die Geräte dort dazu zu packen

"""

ausleihe_id = ausleihe.get("ausleihe_id")
serien_nr = geraete.get("serien_nr")
tuples = []
i = 0
while len(tuples) < 75:
    length = len(tuples)
    tuples.append((ausleihe_id[i], choice(serien_nr)))

    # Durch den cast in ein Set werden duplikate entfernt
    tuples = list(set(tuples))
    i += 1
    if (i == 50):
        i = 0


ausleihe_id, serien_nr = zip(*tuples)

ausleiheninhalt = {
    "ausleihe_id": ausleihe_id,
    "serien_nr": serien_nr
}

angebotstyp = {
    "angebotstyp_id": [1, 2],
    "bezeichnung": ["coaching", "meeting"]
}
angebot = {
    "angebots_id": [1, 2, 3, 4, 5, 6],
    "angebotstyp_id": [1, 2, 1, 2, 1, 2],
    "lohn": [25, 25, 25, 25, 25, 10],
    "studio_id": [1, 1, 2, 2, 3, 3]
}

"""
Arbeitsstunden erzeugen

Ein bisschen unschön gelöst da kompliziert zum erweitern.
Die ersten 50 Rechnungen sind bei mir die Ausleihen, die letzten sollen für Arbeitsstunden sein (freieRgNr)
Nach jeden 50 zugeordneten Arbeitsstunden fängt es wieder von vorne an und die nächste Arbeitsstunde
wird der ersten Rechnung zugewiesen.
Die hinzugefügte Null soll dafür sein, Arbeitsstunden zu markieren, die noch nicht in einer Rechnung zusammengefasst wurden
"""

datum = []
anzahl = []
angebots_id = []
freieRgNr = rechnungen.get("rechnungs_nr")[50:]
freieRgNr = np.append(freieRgNr, 0)
rechnungs_nr = []

for i in range(300):
    datum.append(random_date())
    anzahl.append(randint(1, 5))
    angebots_id.append(choice(angebot.get("angebots_id")))

    if (i <= 50):
        rechnungs_nr.append(freieRgNr[i])
        continue
    if (i <= 101):
        rechnungs_nr.append(freieRgNr[i-51])
        continue
    if (i <= 152):
        rechnungs_nr.append(freieRgNr[i-102])
        continue
    if (i <= 203):
        rechnungs_nr.append(freieRgNr[i-153])
        continue
    if (i <= 254):
        rechnungs_nr.append(freieRgNr[i-204])
        continue
    else:
        rechnungs_nr.append(freieRgNr[i-255])
        continue


arbeitsstunden = {
    "arbeitsstunden_id": np.arange(1, 301, 1),
    "datum": datum,
    "anzahl": anzahl,
    "angebots_id": angebots_id,
    "rechnungs_nr": rechnungs_nr
}


# Liste mit Dictionarys und den Namen dieser. Beide müssen die Inhalte in gleicher Reihenfolge haben!!

dictionarys = [plz, kontaktdaten, rechnungssteller, rechnungen, geraetetyp, geraete, schaeden,
               ausleiher, ausleihe, ausleiheninhalt, studio, angebotstyp, angebot, arbeitsstunden]
dictianarys_names = ["plz", "kontaktdaten", "rechnungssteller", "rechnungen", "geraetetyp", "geraete", "schaeden", "ausleiher", "ausleihe",
                     "ausleiheninhalt", "studio", "angebotstyp", "angebot", "arbeitsstunden"]


# QUERYS erstellen

querys = []

for count, element in enumerate(dictionarys):  # Geht über jedes dictionary

    tuples = list(element.items())  # Packt Inhalte in Tuples

    # Schleife die Anzahl der Values mal durchläuft
    for x in range(len(tuples[0][1])):

        query = f"INSERT INTO {dictianarys_names[count]} VALUES ( "

        # Geht über jedes Tuple und holt sich den jeweiligen Wert und schreibt ihn in den String
        for i, e in enumerate(tuples):

            # Prüft auf Datentyp und wandelt in String um. Anschließend wird überprüft ob der String beendet werden muss oder nicht.
            if (isinstance(e[1][x], Number)):

                if (i == len(tuples)-1):
                    query += str(e[1][x])
                    query += " )"
                else:
                    query += str(e[1][x])
                    query += ", "
            elif (isinstance(e[1][x], date)):

                if (i == len(tuples)-1):
                    query += str("'" + datetime.strftime(e[1][x]) + "'" + " )")

                else:
                    query += str("'" + datetime.strftime(e[1][x], "%m/%d/%Y") + "'" + ", ")

            else:
                if (i == len(tuples)-1):
                    query += str("'" + e[1][x] + "'" + " )")

                else:
                    query += str("'" + e[1][x] + "'" + ", ")

        querys.append(query)

# Querys in .txt schreiben

with open(r'daten/querys.txt', 'w') as fp:
    for item in querys:
        fp.write("%s\n" % item)
