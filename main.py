import requests
from bs4 import BeautifulSoup
import pandas as pd
from colorama import Fore



lotniska = {'WAW': 'Warszawa', 'KRK': 'Kraków', 'GDN': 'Gdańsk', 'WRO': 'Wrocław', 'POZ': 'Poznań', 'SZZ': 'Szczecin',
     'KTW': 'Katowice', 'RZE': 'Rzeszów', 'BZG': 'Bydgoszcz', 'LUZ': 'Lublin','LCJ':'Łódź','SZY':'Olsztyn'}


kraje = {'AL': 'Albania', 'AD': 'Andora', 'AM': 'Armenia', 'AT': 'Austria', 'AZ': 'Azerbejdżan',
         'BY': 'Białoruś', 'BE': 'Belgia', 'BA': 'Bośnia i Hercegowina', 'BG': 'Bułgaria', 'HR': 'Chorwacja',
         'CY': 'Cypr', 'CZ': 'Czechy', 'DK': 'Dania', 'EE': 'Estonia', 'FI': 'Finlandia', 'FR': 'Francja',
         'GE': 'Gruzja', 'DE': 'Niemcy', 'GR': 'Grecja', 'HU': 'Węgry', 'IS': 'Islandia', 'IE': 'Irlandia',
         'IT': 'Włochy', 'KZ': 'Kazachstan', 'XK': 'Kosowo', 'LV': 'Łotwa', 'LI': 'Liechtenstein', 'LT': 'Litwa',
         'LU': 'Luksemburg', 'MK': 'Macedonia', 'MT': 'Malta', 'MD': 'Mołdawia', 'MC': 'Monako', 'ME': 'Czarnogóra',
         'NL': 'Holandia', 'NO': 'Norwegia', 'PL': 'Polska', 'PT': 'Portugalia', 'RO': 'Rumunia', 'RU': 'Rosja',
         'SM': 'San Marino', 'RS': 'Serbia', 'SK': 'Słowacja', 'SI': 'Słowenia', 'ES': 'Hiszpania', 'SE': 'Szwecja',
         'CH': 'Szwajcaria', 'TR': 'Turcja', 'UA': 'Ukraina', 'GB': 'Wielka Brytania', 'VA': 'Watykan',
         'DZ': 'Algieria', 'AO': 'Angola', 'BJ': 'Benin', 'BW': 'Botswana', 'BF': 'Burkina Faso', 'BI': 'Burundi',
         'CM': 'Kamerun', 'CV': 'Republika Zielonego Przylądka', 'CF': 'Republika Środkowoafrykańska', 'TD': 'Czad',
         'KM': 'Komory', 'CG': 'Kongo', 'CD': 'Demokratyczna Republika Konga', 'CI': 'Wybrzeże Kości Słoniowej',
         'DJ': 'Dżibuti', 'EG': 'Egipt', 'GQ': 'Gwinea Równikowa', 'ER': 'Erytrea', 'ET': 'Etiopia', 'GA': 'Gabon',
         'GM': 'Gambia', 'GH': 'Ghana', 'GN': 'Gwinea', 'GW': 'Gwinea Bissau', 'KE': 'Kenia', 'LS': 'Lesotho',
         'LR': 'Liberia','LY': 'Libia', 'MG': 'Madagaskar', 'MW': 'Malawi', 'ML': 'Mali', 'MR': 'Mauretania', 'MU': 'Mauritius',
         'YT': 'Majotta', 'MA': 'Maroko', 'MZ': 'Mozambik', 'NA': 'Namibia', 'NE': 'Niger', 'NG': 'Nigeria','RE': 'Reunion',
         'RW': 'Rwanda', 'ST': 'Wyspy Świętego Tomasza i Książęca', 'SN': 'Senegal', 'SC': 'Seszele', 'SL': 'Sierra Leone',
         'SO': 'Somalia', 'ZA': 'Republika Południowej Afryki', 'SS': 'Sudan Południowy', 'SD': 'Sudan', 'SZ': 'Suazi',
         'TZ': 'Tanzania', 'TG': 'Togo', 'TN': 'Tunezja', 'UG': 'Uganda', 'EH': 'Sahara Zachodnia', 'ZM': 'Zambia',
         'ZW': 'Zimbabwe', 'AR': 'Argentyna', 'BO': 'Boliwia', 'BR': 'Brazylia', 'CL': 'Chile', 'CO': 'Kolumbia',
         'EC': 'Ekwador', 'FK': 'Falklandy', 'GF': 'Gujana Francuska', 'GY': 'Gujana', 'PE': 'Peru', 'PY': 'Paragwaj',
         'SR': 'Surinam', 'UY': 'Urugwaj', 'VE': 'Wenezuela', 'AI': 'Anguilla', 'AG': 'Antigua i Barbuda',
         'AW': 'Aruba', 'BS': 'Bahamy', 'BB': 'Barbados', 'BZ': 'Belize', 'BM': 'Bermudy', 'VG': 'Brytyjskie Wyspy Dziewicze',
         'CA': 'Kanada', 'KY': 'Kajmany', 'CR': 'Kostaryka', 'CU': 'Kuba', 'DM': 'Dominika', 'DO': 'Dominikana',
         'SV': 'Salwador', 'GL': 'Grenlandia', 'GD': 'Grenada', 'GP': 'Gwadelupa', 'GT': 'Gwatemala', 'HT': 'Haiti',
         'HN': 'Honduras', 'JM': 'Jamajka', 'MQ': 'Martynika', 'MX': 'Meksyk', 'MS': 'Montserrat','AN': 'Antyle Holenderskie',
         'NI': 'Nikaragua', 'PA': 'Panama', 'PR': 'Portoryko', 'BL': 'Saint-Barthélemy', 'KN': 'Saint Kitts i Nevis',
         'LC': 'Saint Lucia', 'MF': 'Saint Martin', 'PM': 'Saint Pierre i Miquelon', 'VC': 'Saint Vincent i Grenadyny',
         'TT': 'Trynidad i Tobago', 'TC': 'Turks i Caicos', 'US': 'Stany Zjednoczone',
         'VI': 'Wyspy Dziewicze Stanów Zjednoczonych',
         'AF': 'Afganistan', 'BH': 'Bahrajn', 'BD': 'Bangladesz', 'BT': 'Bhutan', 'BN': 'Brunei', 'KH': 'Kambodża','CN': 'Chiny',
         'HK': 'Hongkong', 'IN': 'Indie', 'ID': 'Indonezja', 'IR': 'Iran', 'IQ': 'Irak', 'IL': 'Izrael',
         'JP': 'Japonia', 'JO': 'Jordania',
         'KP': 'Korea Północna', 'KR': 'Korea Południowa', 'KW': 'Kuwejt', 'KG': 'Kirgistan', 'LA': 'Laos', 'LB': 'Liban', 'MO': 'Makau',
         'MY': 'Malezja', 'MV': 'Malediwy', 'MN': 'Mongolia', 'MM': 'Mjanma', 'NP': 'Nepal', 'OM': 'Oman','PK': 'Pakistan', 'PH': 'Filipiny',
         'QA': 'Katar', 'SA': 'Arabia Saudyjska', 'SG': 'Singapur', 'LK': 'Sri Lanka', 'SY': 'Syria', 'TW': 'Tajwan','TJ': 'Tadżykistan',
         'TH': 'Tajlandia', 'TL': 'Timor Wschodni', 'TM': 'Turkmenistan', 'AE': 'Zjednoczone Emiraty Arabskie','UZ': 'Uzbekistan',
         'VN': 'Wietnam', 'YE': 'Jemen'}

linie_lotnicze = {'LO': 'LOT Polish Airlines',
                  'W6': 'Wizz Air', 'FR': 'Ryanair', 'LH': 'Lufthansa', 'OK': 'Czech Airlines',
                  '4U': 'Lufthansa CityLine', 'UA': 'United Airlines',
                  'AF': 'Air France', 'KL': 'KLM', 'AY': 'Finnair', 'TP': 'TAP Air Portugal',
                  'SK': 'SAS Scandinavian Airlines', 'LOT': 'LOT Polish Airlines',
                  'QR': 'Qatar Airways', 'TK': 'Turkish Airlines', 'AA': 'American Airlines', 'BA': 'British Airways',
                  'DL': 'Delta Air Lines', 'EK': 'Emirates',
                  'SQ': 'Singapore Airlines', 'AC': 'Air Canada', 'AI': 'Air India', 'CX': 'Cathay Pacific',
                  'EY': 'Etihad Airways', 'JL': 'Japan Airlines',
                  'QF': 'Qantas', 'TG': 'Thai Airways', 'VS': 'Virgin Atlantic', 'AZ': 'Alitalia', 'CA': 'Air China',
                  'ET': 'Ethiopian Airlines',
                  'LX': 'International Air Lines', 'NH': 'All Nippon Airways', 'A3': 'Aegean Airlines', 'AV': 'Avianca',
                  'CM': 'Copa Airlines',
                  'CZ': 'China Southern Airlines', 'FJ': 'Fiji Airways', 'G3': 'Gol Transportes Aéreos', 'GR': 'TUIfly',
                  'HU': 'Hainan Airlines',
                  'IB': 'Iberia', 'KQ': 'Kenya Airways', 'MH': 'Malaysia Airlines', 'OZ': 'Asiana Airlines',
                  'PR': 'Philippine Airlines', 'S7': 'S7 Airlines',
                  'TU': 'Tunisair', 'WY': 'Oman Air', 'ZH': 'Shenzhen Airlines', 'ZR': 'Buraq Air',
                  'OS': 'Austrian Airlines'}

zrodlo_strony = requests.get('https://www.esky.pl/okazje')
html_parser = BeautifulSoup(zrodlo_strony.text, 'html.parser')
wyszukaj_informacje_o_okazjach = html_parser.find_all(attrs={'data-qa-tile': True})
def okazja():
    lista_list = [[]]
    lista_list.clear()
    for okazje in wyszukaj_informacje_o_okazjach:
        link_do_okazji = okazje['href']
        ciag = okazje['data-qa-tile']
        lista = ciag.replace(';', ' ').split()
        for klucz in kraje:
            lista[1] = lista[1].replace(klucz, kraje[klucz])
            lista[5] = lista[5].replace(klucz, kraje[klucz])
        lista.append(link_do_okazji)
        lista_list.append(lista)
    return lista_list
def menu_okazji():
    odp = None
    zakres1 = 0
    zakres2 = 10000000 #poniżej tej wartości nie będzie okazji
    waluta_wartosc=[1,"PLN"]
    linia=None
    miasto_start=None
    while odp != 5:
        print("1: Zakres cen")
        print("2: Wybór waluty")
        print("3. Wybór przewoźnika")
        print("4. Wybór lotniska wylotu")
        print("5. Filtruj!")
        odp = int(input("Wybierz jedną z podanych opcji: "))
        if odp == 1:
            zakres1 = int(input("Podaj minimalną cenę jaką jesteś w stanie zapłacić: "))
            zakres2 = int(input("Podaj maksymalną cenę jaką jesteś w stanie zapłacić: "))
        elif odp == 2:
            waluta = input("Podaj kod waluty, która cię interesuje: ")
            response2 = requests.get('https://api.nbp.pl/api/exchangerates/tables/A')
            data = response2.json()
            rates = data[0]['rates']
            waluta_wartosc = None
            for rate in rates:
                if rate["code"] == waluta:
                    print("Wybrana waluta to:",rate["currency"],"o kursie:", rate["mid"])
                    waluta_wartosc = [rate["mid"],rate["code"]]
        elif odp == 3:
            linia=input("Podaj kod przewoźnika (linii lotniczej), który cię interesuje: ")
        elif odp == 4:
            miasto_start=input("Podaj miasto (kod lotniska), z którego byłoby ci najwygodniej wylecieć: ")
        print()
    return [zakres1, zakres2, waluta_wartosc, linia, miasto_start]


def wyszkaj_okazje():
    lista=menu_okazji()
    for listy in okazja():
        kod_lotniska = listy[6]
        try:
            czytaj_csv = pd.read_csv("airports.csv")
            czytaj_csv = czytaj_csv[czytaj_csv["iata_code"] == kod_lotniska]
            miasto = czytaj_csv["municipality"].iloc[0]
        except IndexError:
            miasto="nieznane"

        if len(listy)==15:
            x=int(listy[12])*(1/int(lista[2][0]))
            listy[12]=round(x,3)
            listy[13] = lista[2][1]
            if int(listy[12])>=lista[0] and int(listy[12])<=lista[1]:
                if lista[3]!=None and lista[4]!=None:
                    if listy[8]==lista[3] and listy[2]==lista[4]:
                        for klucz in linie_lotnicze:
                            listy[8] = listy[8].replace(klucz, linie_lotnicze[klucz])
                        for klucz in lotniska:
                            listy[2]=listy[2].replace(klucz, lotniska[klucz])
                        print(Fore.RESET+"Wylot z", Fore.RED + listy[1], Fore.RESET+"lotnisko:", Fore.GREEN + listy[2],Fore.RESET+ "do",
                              Fore.RED + listy[5],Fore.RESET+ "lotnisko:", Fore.GREEN + miasto,Fore.RESET+ "linia lotnicza:",
                              Fore.YELLOW + listy[8],Fore.RESET+ "cena:", Fore.MAGENTA + str(listy[12]), Fore.MAGENTA + listy[13],
                              Fore.RESET+"Link do okazji:", listy[14], "\n")
                elif lista[3]!=None and lista[4]==None:
                    if lista[3]==listy[8]:
                        for klucz in linie_lotnicze:
                            listy[8] = listy[8].replace(klucz, linie_lotnicze[klucz])
                        for klucz in lotniska:
                            listy[2]=listy[2].replace(klucz, lotniska[klucz])
                        print(Fore.RESET + "Wylot z", Fore.RED + listy[1], Fore.RESET + "lotnisko:",
                              Fore.GREEN + listy[2], Fore.RESET + "do",
                              Fore.RED + listy[5], Fore.RESET + "lotnisko:", Fore.GREEN + miasto,
                              Fore.RESET + "linia lotnicza:",
                              Fore.YELLOW + listy[8], Fore.RESET + "cena:", Fore.MAGENTA + str(listy[12]),
                              Fore.MAGENTA + listy[13],
                              Fore.RESET + "Link do okazji:", listy[14], "\n")
                elif lista[3]==None and lista[4]!=None:
                    if lista[4]==listy[2]:
                        for klucz in linie_lotnicze:
                            listy[8] = listy[8].replace(klucz, linie_lotnicze[klucz])
                        for klucz in lotniska:
                            listy[2]=listy[2].replace(klucz, lotniska[klucz])
                        print(Fore.RESET + "Wylot z", Fore.RED + listy[1], Fore.RESET + "lotnisko:",
                              Fore.GREEN + listy[2], Fore.RESET + "do",
                              Fore.RED + listy[5], Fore.RESET + "lotnisko:", Fore.GREEN + miasto,
                              Fore.RESET + "linia lotnicza:",
                              Fore.YELLOW + listy[8], Fore.RESET + "cena:", Fore.MAGENTA + str(listy[12]),
                              Fore.MAGENTA + listy[13],
                              Fore.RESET + "Link do okazji:", listy[14], "\n")
                    for klucz in linie_lotnicze:
                        listy[8] = listy[8].replace(klucz, linie_lotnicze[klucz])
                    for klucz in lotniska:
                        listy[2] = listy[2].replace(klucz, lotniska[klucz])
                    print(Fore.RESET + "Wylot z", Fore.RED + listy[1], Fore.RESET + "lotnisko:", Fore.GREEN + listy[2],
                          Fore.RESET + "do",
                          Fore.RED + listy[5], Fore.RESET + "lotnisko:", Fore.GREEN + miasto,
                          Fore.RESET + "linia lotnicza:",
                          Fore.YELLOW + listy[8], Fore.RESET + "cena:", Fore.MAGENTA + str(listy[12]),
                          Fore.MAGENTA + listy[13],
                          Fore.RESET + "Link do okazji:", listy[14], "\n")
        else:
            x= int(listy[13]) * (1/int(lista[2][0]))
            listy[13]=round(x,2)
            listy[14]=lista[2][1]
            if int(listy[13]) >= lista[0] and int(listy[13]) <= lista[1]:
                if lista[3]!=None and lista[4]!=None:
                    if listy[8]==lista[3] and listy[2]==lista[4]:
                        for klucz in linie_lotnicze:
                            listy[8] = listy[8].replace(klucz, linie_lotnicze[klucz])
                        for klucz in lotniska:
                            listy[2]=listy[2].replace(klucz, lotniska[klucz])
                        print(Fore.RESET + "Wylot z", Fore.RED + listy[1], Fore.RESET + "lotnisko:",
                              Fore.GREEN + listy[2],
                              Fore.RESET + "do",
                              Fore.RED + listy[5], Fore.RESET + "lotnisko:", Fore.GREEN + miasto,
                              Fore.RESET + "linia lotnicza:",
                              Fore.YELLOW + listy[8], Fore.RESET + "cena:", Fore.MAGENTA + str(listy[13]),
                              Fore.MAGENTA + listy[14],
                              Fore.RESET + "Link do okazji:", listy[15], "\n")

                elif lista[3]!=None and lista[4]==None:
                    if lista[3]==listy[8]:
                        for klucz in linie_lotnicze:
                            listy[8] = listy[8].replace(klucz, linie_lotnicze[klucz])
                        for klucz in lotniska:
                            listy[2]=listy[2].replace(klucz, lotniska[klucz])
                        print(Fore.RESET + "Wylot z", Fore.RED + listy[1], Fore.RESET + "lotnisko:",
                              Fore.GREEN + listy[2],
                              Fore.RESET + "do",
                              Fore.RED + listy[5], Fore.RESET + "lotnisko:", Fore.GREEN + miasto,
                              Fore.RESET + "linia lotnicza:",
                              Fore.YELLOW + listy[8], Fore.RESET + "cena:", Fore.MAGENTA + str(listy[13]),
                              Fore.MAGENTA + listy[14],
                              Fore.RESET + "Link do okazji:", listy[15], "\n")
                elif lista[3]==None and lista[4]!=None:
                    if lista[4]==listy[2]:
                        for klucz in linie_lotnicze:
                            listy[8] = listy[8].replace(klucz, linie_lotnicze[klucz])
                            for klucz in lotniska:
                                listy[2] = listy[2].replace(klucz, lotniska[klucz])
                        print(Fore.RESET + "Wylot z", Fore.RED + listy[1], Fore.RESET + "lotnisko:",
                              Fore.GREEN + listy[2],
                              Fore.RESET + "do",
                              Fore.RED + listy[5], Fore.RESET + "lotnisko:", Fore.GREEN + miasto,
                              Fore.RESET + "linia lotnicza:",
                              Fore.YELLOW + listy[8], Fore.RESET + "cena:", Fore.MAGENTA + str(listy[13]),
                              Fore.MAGENTA + listy[14],
                              Fore.RESET + "Link do okazji:", listy[15], "\n")
                else:
                    for klucz in linie_lotnicze:
                        listy[8] = listy[8].replace(klucz, linie_lotnicze[klucz])
                    for klucz in lotniska:
                        listy[2] = listy[2].replace(klucz, lotniska[klucz])
                    print(Fore.RESET + "Wylot z", Fore.RED + listy[1], Fore.RESET + "lotnisko:",
                          Fore.GREEN + listy[2],
                          Fore.RESET + "do",
                          Fore.RED + listy[5], Fore.RESET + "lotnisko:", Fore.GREEN + miasto,
                          Fore.RESET + "linia lotnicza:",
                          Fore.YELLOW + listy[8], Fore.RESET + "cena:", Fore.MAGENTA + str(listy[13]),
                          Fore.MAGENTA + listy[14],
                          Fore.RESET + "Link do okazji:", listy[15], "\n")
wyszkaj_okazje()

