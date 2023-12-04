# KOMENTOWANIE
# To jest komentarz w jednej lini
"""To
jest
komentarz
w
wielu
liniach"""

# ZMIENNE
print("Zmienne")
imie = "Bartosz"
wiek = 16  # Określenie zmiennej 'wiek' na 16
print(imie)  # Wydala kod 'imie'
print(wiek)
print("")

# określanie typu zmiennej
print("Określanie typie zmiennej")
wiek_x = str("16")  # Określenie typu zmiennej wiek_x na string (tekst)
wiek_y = int(16)  # Określenie typu zmiennej wiek_y na int (liczba calkowita)
wiek_z = float(16)  # Określenie typu zmiennej wiek_z na float (liczba z ułamkiem)
print(wiek_x, "string")
print(wiek_y, "int")
print(wiek_z, "float")
print(type(wiek_x))  # Mówi nam o typie zmiennej
print(type(wiek_y))
print(type(wiek_z))
print("")

# '' i " " niczym sie nie różni
imie = "Bartosz"
print(imie)
imie = 'Bartosz'
print(imie)
print("")

# duże znaki zmiennych różnią się
Imie = "Kordian"
print(Imie)
print(imie)
print("")

# Zmienne nie mogą się zaczynać liczbą i nie mogą mieć w sobie spacji innych znaków specjalnych, oprócz _
_moje_2imie = "Łukasz"  # git
print(_moje_2imie)
# 2moje - imie="Łukasz" #nie git
print("")

# Wpisywanie wiele zmiennych
# Wiele zmiennych do wielu wartości
print("Wiele zmiennych do wielu wartości")
x, y, z = "procesor", "karta graficzna", "RAM"
print(x)
print(y)
print(z)
print("")

# Wiele zmiennych do jednej wartości
print("Wiele zmiennych do jednej wartości")
x = y = z = "zasilacz"
print(x)
print(y)
print(z)
print("")

# Odpakowywanie kolekcji
print("Odpakowywanie kolekcji")
rtx = ["3050", "3060", "3070", "3080", "3090"]
w, v, x, y, z = rtx
print(w)
print(v)
print(x)
print(y)
print(z)
print("")

# Zmienne wyjściowe
print(imie)
print(imie, wiek)  # string, int --git
# print (imie+wiek) #string + int -nie git
print(imie + Imie)
rok = 2022
print(rok + wiek)  # int + int --git
print("")

# Globalne zmienne
miasto = "Siemce"  # zmienna globalna


def test1():  # funkcja, więcej o nich później
    print("Moje miasto to " + miasto)


test1()


def test2():
    miasto = "Katowice"  # zmienna w funkcji jest lokalna
    print("Moje miasto to " + miasto)


test2()
print("Moje miasto to " + miasto)  # print jest poza funkcją więc nie bierze Katowic, które sa lokalne


def test3():
    global miasto  # Tworzenie globalnej zmiennej w funkcji
    miasto = "Będzin"  # zmienna w funkcji jest globalna


test3()
print("Moje miasto to " + miasto)  # print jest poza funkcją, lecz bierze będzin bo jest zmienną globalną
print("")

# TYPY ZMIENNYCH
"""
Text Type: 	str
Numeric Types: 	int, float, complex
Sequence Types: 	list, tuple, range
Mapping Type: 	dict
Set Types: 	set, frozenset
Boolean Type: 	bool
Binary Types: 	bytes, bytearray, memoryview
None Type: 	NoneType
"""

# losowa liczba
import random

print(random.randrange(1, 10))
print("")

# STRING - ZWYKŁY TEKST
print("string")
x = "Bartosz"  # Bez określenia zmiennej
x = str("Bartosz")  # Z okresleniem zmiennej.
print(x)
print("")

# wiele linijek
y = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""  # By dać string w wielu linijkach trzeba dać """ """ lub ''' '''
print(y)
print("")

# Wyciągniecie znaku
x = "XD"
print(x[0])  # 0 to pierwszy znak
print("")

# pętla for w string'u
for x in "Bartosz":
    print(x)
    print("")

# długość string'u
x = "Bartosz"
print(len(x))
print("")

# sprawdź czy w string'u
z = "O jasny ****, toż to laseraptor. Myślałem, że wygineły tysiące lat temu"
print("laseraptor" in z)
if "laseraptor" in z:
    print("Jak widać nie wygineły")

# sprawdź czy w string'u
z = "O jasny ****, toż to laseraptor. Myślałem, że wygineły tysiące lat temu"
print("żyją" not in z)
if "żyją" not in z:
    print("Jak widać nie żyją")
    print("")

# slicing string
b = "Witaj świecie!"
print(b[2:8])
print(b[:5])
print(b[2:])
print(b[-5:-2])
print("")

# Modify strings
q = " Witaj, świecie! "
print(q.upper())  # CAPS LOCK ON
print(q.lower())  # caps lock off
print(q.strip())  # usuwa zbędne spacje
print(q.replace("W", "P"))  # Zamienia znaki
print(q.split(","))  # Rozdziela słowa oddzielone w tym przypadku przecinek
print("")

# String Cocncatenation - Łączenie ciągów
a = "Witaj"
b = "świecie"
c = a + " " + b
print(c)
print("")

# String format - jak wiadomo nie można łączyc inta z stringiem, przez co można wykorzystać 'format'
wiek = 16
tekst = "Mam na imię Bartosz i mam {} lat"
print(tekst.format(wiek))
ilosc = 4
nr_rzeczy = 327
cena = 34.80
moje_zamowienie = "Poprosze {} kawałki rzeczy o numerze {} za {}"
print(moje_zamowienie.format(ilosc, nr_rzeczy, cena))
moje_2_zamowienie = "Chciałbym zapłacić {2} za {0} kawałków rzeczy o numerze {1}"  # wstawianie w nawiasy kolejności
print(moje_2_zamowienie.format(ilosc, nr_rzeczy, cena))
print("")

# Escape characters
'''nie możemy wpisać np. print("Jesteśmy "najlepsi"") więc to nam to umożliwia'''
print("Jesteśmy \"Najlepsi\"")
'''
\' 	Single Quote
\\ 	Backslash
\n 	New Line
\r 	Carriage Return
\t 	Tab
\b 	Backspace
\f 	Form Feed
\ooo 	Octal value
(\)xhh 	Hex value -(bez nawiasów)
'''
txt = 'It\'s alright.'
print(txt)
txt = "This will insert one \\ (backslash)."
print(txt)
txt = "Hello\nWorld!"
print(txt)
txt = "Hello\rWorld!"
print(txt)
txt = "Hello\tWorld!"
print(txt)
txt = "Hello \bWorld!"
print(txt)
txt = "\110\145\154\154\157"
print(txt)
txt = "\x48\x65\x6c\x6c\x6f"
print(txt)
print("")

# string methods - https://www.w3schools.com/python/python_strings_methods.asp


# INT - LICZBA CAŁKOWITA
print("int")
x = 16
x = int(16)
print(x)
y = -3321
z = int(4.6)  # int nie ma ułamków więc wynik to 4
w = int("5")
print(y)
print(z)
print(w)
print("")

# float - liczba wymierna
print("float")
x = 16.5
x = float(16.5)
print(x)
y = float(18)
z = -314.32
print(y)
print(z)
v = 35e3  # e lub E. float może mieć e by zaznaczyć moc 10
print(v)
print("")

# Matematyka
print("Matematyka")
x = 35
y = 5
z = 6
print("Liczby to:", x, y, z)
print("Dodawanie:", x + y)  # Dodawanie
print("Odejmowanie:", x - y)  # Odejmowanie
print("Mnożenie:", x * y)  # Mnożenie
print("Dzielenie:", x / z)  # Dzielenie
print("Modulus:", x % y)  # Modulus - Reszta z dzielenia
print("Potegowanie:", x ** y)  # Potęgowanie
print("Dzielenie zaokrąglone w dół:", x // z)  # Zaokrągla dzielenie w dół, 35/6 = 5.8(3), leczy wynik będzie wynosił 5
print("")

x = 35
print("Początkowa liczba:", x)
x += 5
print("Liczba 35 po dodaniu 5 to:", x)
x -= 10
print("Liczba 40 po odjęciu 10 to:", x)
x &= 13  # AND, aktualnie x=30 czyli binarnie to 11110, a 13 binarnie to 01101, porównując bity te same to 01100, czyli 12
print("Liczba 30 po AND z 13 to:", x)
x |= 5  # OR, aktualnie x=12 binarnie to 1100, a 5 binarnie to 0101, zamieniając 1 za 0 daje nam 1101, czyli 13
print("Liczba 12 po OR z 5 to:", x)
x ^= 3  # XOR, aktualnie x=13 binarnie to 1101, a 3 to 0011, or lecz gdy 1 i 1 się spotkają dają 0, czyli wynik to 1110 czyli 14
print("Liczba 13 po XOR z 3 to:", x)
x >>= 2  # przesuwa bity w prawo o 2/usuwa dwa ostatnie bity z liczby x=14 binarnie 1110 czy;i wynik to binarnie 0011, czyli 3
print("Liczba 14 po przesunięciu w prawo o 2 to:", x)
x <<= 5  # przesuwa bity w lewo o 5/dodaje pieć 0 bitów na koniec x=3 binarnie 0011 co daje nam 001100000, czyli 96 (32+64)
print("Liczba 3 po przesunięciu w lewo o 5 to:", x)
print("")

'''Python Collections (Arrays)
There are four collection data types in the Python programming language:

- List is a collection which is ordered and changeable. Allows duplicate members.
- Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
- Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
- Dictionary is a collection which is ordered** and changeable. No duplicate members.

*Set items are unchangeable, but you can remove and/or add items whenever you like.
**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.'''

# Listy
print("Listy")
rozszerzona_lista = []  # Tworzenie pustej listy
lista = ["kasztany", 3, 43.21, "kasztany", True]  # Tworzenie listy
print(lista)  # wyświetla całą liczbę
print(len(lista))  # Długość liczby
print(lista[2])  # wyświetli 43.21, bo 0,1,2
print(lista[-1])  # wyświetli ostatni wyraz
print(lista[1:4])  # od 1 do 4 (wyświetli 1, 2 i 3 wyraz)
print("")

# Zmiana w liście
if 3 in lista:  # sprawdzenie czy jest w liście
    print("tak, 3 jest w liście")
else:
    print("Liczby 3 nie w liście")
lista[1] = 27  # Zmiana [1] wyrazu na 27 <-------------------<-------------------
if 3 in lista:  # sprawdzenie czy jest w liście
    print("Tak, 3 jest w liście")
else:
    print("Liczby 3 nie w liście")  # 3 zostało zamienione na 27 więc nie bezie gow  liście
lista[1:3] = [13, 19.07]  # zmiana wielu wyrazów <-------------------<-------------------
print(lista)
print("")

# Dodawanie do listy
lista.insert(2, "WHOT")  # daje obiekt WHOT po 2 wyrazie
print(lista)
lista.append(2077)  # dodawanie na koniec listy
print(lista)
print(rtx)
print(rozszerzona_lista)
rozszerzona_lista.extend(lista)  # Dodawanie wyrazów z listy "lista" do "rozszerzona_lista"
print(rozszerzona_lista)
rozszerzona_lista.extend(rtx)
print(rozszerzona_lista)
print("")

# Usuwanie z listy
lista.remove("kasztany")  # usuwa z listy. Kasztany są duplikatem więc usunięte zostały te pierwsze
print(lista)
lista.pop(0)  # Usuwa indeks [0]
lista.pop()  # usuwa ostatni indeks
del lista[2]  # działa tak samo jak pop(2)
print(lista)
rozszerzona_lista.clear()  # Usuwa wszystko z listy
print(rozszerzona_lista)
del rozszerzona_lista  # usuwa listę
# print(rozszerzona_lista) jest błędem, bo nie ma już listy
print("")

# Loopowanie/Wymienianie wyrazów z listy
for x in rtx:
    print(x)  # Wymienia wyrazy z listy
for i in range(len(lista)):
    print(lista[i])  # To samo
y = 0
while y < len(rtx):
    print(rtx[y])
    y += 1  # To samo
[print(x) for x in lista]  # najkrótsza linia by wymienić wyrazy
print("")

# List comprehension - rozumienie listy
nowa1 = []
nowa2 = []
int = x
for x in rtx:
    if x > "3070":
        nowa1.append(x)  # To jest długie zapytanie o to by dało do nowej listy jedynie wyrazy większe od 3070
print(nowa1)
nowa2 = [x for x in rtx if x <= "3070"]  # Krótkie zapytanie by do nowej listy dało wyrazy równe lub mniejsze 3070
print(nowa2)
# newlist = [expression for item in iterable if condition == True]
liczenie_do_10 = [x for x in range(10) if x < 5]  # Stwozenie listy liczb od 0 do 5 wyłącznie
print(liczenie_do_10)
wyrazy = ["siemanero", "stuu", "rezi", "multi", "Ruby"]
nowa3 = [x.upper() for x in wyrazy]  # Daje wyrazy jako duże litery
print(nowa3)
nowa4 = ['hello' for x in wyrazy]  # daje hello za wszystko
print(nowa4)
nowa5 = [x if x != "stuu" else "gimper" for x in wyrazy]  # zamienia stuu na gimper w nowej liście
print(nowa5)
print("")

# Sortowanie list
rozszerzona_lista = []
lista = ["kasztany", "3", "43.21", "kasztany", "True"]
rozszerzona_lista.extend(wyrazy + lista)
rozszerzona_lista.sort()
print(rozszerzona_lista)  # Sortowało
rtx.sort()
print(rtx)
rtx.sort(reverse=True)  # Sortowanie descending
print(rtx)

liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def myfunc(n):
    return abs(n - 5)  # Sortuje liczby najbliższe do 5


liczby.sort(key=myfunc)
print(liczby)
rozszerzona_lista.sort(key=str.lower)  # Ignoruje sortowanie dużych i małych liter oddzielnie
print(rozszerzona_lista)
print("")

# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	    Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	    Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	    Sorts the list

# If ... Else
print("If ... Else")
a = 5
b = 10
c = 7
if a > b:
    print("a jest większe od b")
elif a == b:
    print("a jes równe b")
else:
    print("b jest wieksze od a")

if a < b: print("a jest mniejsze od b")
print("a") if a > b else print("b")

if a < b and c < b:
    print("b jest większe od a i c")

if c < a or c < b:
    print("Jedno z założeń jest prawdziwe")

if b >= 10:
    print("Większe lub równe 10")
    if b >= 20:
        print("I większe od 20")
    else:
        print("Lecz nie większe od 20")

if a > b:
    pass  # if nie może być pusty, więc daje sie pass by nie dostać error
print("")

# Loops
print("Loops")
print("while - loopuje jeśli założenie jest True")
print("for - używany do iterazji przez sekwencje (listy, tuple, dictionary, set or string")
i = 1
while i < 6:  # wypisuje liczby do 6 (1, 2, 3, 4, 5)
    print(i)
    if i == 3:  # Gdzy dojdzie do 3 to stopuje przy użyciu break
        break
    i += 1
print("---------------")
x = 0
while x < 6:
    x += 1
    if x == 3:  # Kontynuuj następną iteracje jeśli x==3
        continue
    print(x)
else:
    print("x nie jest już mniejsze od 6")

print(rtx)
for p in rtx:
    if p == "3080":  # Mija 3080
        continue
    if p == "3050":
        break
    print(p)

for x in "popek":
    print(x)
print("-----")

for x in range(2, 6):
    print(x)
print("-----")

for x in range(2, 50, 8):  # od 2 do 51 co 8
    print(x)
    if x == 50:
        print("Doszło do końca!")
    elif x >= 42:
        print("Nie doszło do końca")

adj = ["red", "big"]
fruits = ["apple", "banana"]

for x in adj:
    for y in fruits:
        print(x, y)

for x in [0, 1, 2]:
    pass  # for nie może być pusty

# Funkcje
print("Funkcje")


def funkcja():  # Stworzenie funkcji
    print("Hello world from function!")


funkcja()  # Wezwanie funkcji


def Argumenty(fNazwa, lata):  # Argument fNazwa. Można się do niego odnieśc w wywołaniu funkcji by był zastąpiony
    print(fNazwa + " Dyba, lat: " + lata)


Argumenty("Bartosz", "18")
Argumenty("Barbara", "najmniejej")
Argumenty(lata="najmniej", fNazwa="Andrzej")  # Można dawać argument i coś by robić to w swojej kolejności


# Argumenty("Michał") jest błędem bo odnosi się do jednego argumentu, a nie dwóch


def mlodsi(*dzieci):  # Jeśli nie wiesz ile argumentów to daj *, stworzy to tuple
    print("Najmłodszymi są " + dzieci[2] + " i " + dzieci[1])


mlodsi("Hania", "Maja", "Amelia")


def moja_funkcja(**dzieci):  # Jeśli nie wiesz ile kluczy dla argumentów to daj **
    print("Jego nazwisko to: " + dzieci["nazwisko"])


moja_funkcja(imie="Hania", nazwisko="Kowalska")


def kraje(kraj="Polska"):  # default ustawienie dla 'kraj'
    print("Jaki jest najgorszy kraj w piłkę nożną?: " + kraj)


kraje("San Marino")
kraje()  # Polska, bo default to Polska


def zwróć(x):
    return 5 * x


zwróć(3)
print(zwróć(5))  # Zwraca 5 * 5
print(zwróć(98))


def puste():
    pass

def tri_recursion(k): # Loopowanie funkcji - Recursion
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

"""
Funkcja tri_recursion w Pythonie jest przykładem rekurencyjnej funkcji, która oblicza sumę liczb od 1 do k. Oto szczegółowy opis działania tej funkcji, gdy k jest równy 6:

Pierwsze wywołanie: tri_recursion(6)

Ponieważ k > 0 (6 > 0), funkcja przechodzi do obliczenia 6 + tri_recursion(5).
Nie może jednak obliczyć tego teraz, ponieważ musi najpierw obliczyć tri_recursion(5).
Drugie wywołanie: tri_recursion(5)

Podobnie jak wcześniej, oblicza 5 + tri_recursion(4).
Musi teraz obliczyć tri_recursion(4).
Trzecie wywołanie: tri_recursion(4)

Oblicza 4 + tri_recursion(3).
Musi teraz obliczyć tri_recursion(3).
Czwarte wywołanie: tri_recursion(3)

Oblicza 3 + tri_recursion(2).
Musi teraz obliczyć tri_recursion(2).
Piąte wywołanie: tri_recursion(2)

Oblicza 2 + tri_recursion(1).
Musi teraz obliczyć tri_recursion(1).
Szóste wywołanie: tri_recursion(1)

Oblicza 1 + tri_recursion(0).
Musi teraz obliczyć tri_recursion(0).
Siódme wywołanie: tri_recursion(0)

Teraz k jest równe 0, więc funkcja zwraca 0 bez dalszego wywoływania rekurencyjnego.
Rekurencja zaczyna się odwracać i zwracać wartości:

tri_recursion(0) zwraca 0.
tri_recursion(1) zwraca 1 + 0 = 1.
tri_recursion(2) zwraca 2 + 1 = 3.
tri_recursion(3) zwraca 3 + 3 = 6.
tri_recursion(4) zwraca 4 + 6 = 10.
tri_recursion(5) zwraca 5 + 10 = 15.
tri_recursion(6) zwraca 6 + 15 = 21.
W wyniku tego, funkcja wypisuje kolejne sumy częściowe: 1, 3, 6, 10, 15, 21, a ostateczny wynik to 21.
"""