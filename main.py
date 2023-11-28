# KOMENTOWANIE
#To jest komentarz w jednej lini
"""To
jest
komentarz
w
wielu
liniach"""

#ZMIENNE
print("Zmienne")
imie="Bartosz"
wiek=16 #Określenie zmiennej 'wiek' na 16
print(imie) #Wydala kod 'imie'
print(wiek)

#określanie typu zmiennej
print("Określanie typie zmiennej")
wiek_x=str("16") #Określenie typu zmiennej wiek_x na string (tekst)
wiek_y=int(16) #Określenie typu zmiennej wiek_y na int (liczba calkowita)
wiek_z=float(16) #Określenie typu zmiennej wiek_z na float (liczba z ułamkiem)
print(wiek_x, "string")
print(wiek_y, "int")
print(wiek_z,"float")
print(type(wiek_x)) #Mówi nam o typie zmiennej
print(type(wiek_y))
print(type(wiek_z))

#'' i " " niczym sie nie różni
imie="Bartosz"
print(imie)
imie='Bartosz'
print(imie)

#duże znaki zmiennych różnią się
Imie="Kordian"
print(Imie)
print(imie)

#Zmienne nie mogą się zaczynać liczbą i nie mogą mieć w sobie spacji innych znaków specjalnych, oprócz _
_moje_2imie="Łukasz" #git
print(_moje_2imie)
#2moje - imie="Łukasz" #nie git

#Wpisywanie wiele zmiennych
#Wiele zmiennych do wielu wartości
print("Wiele zmiennych do wielu wartości")
x, y, z="procesor", "karta graficzna", "RAM"
print(x)
print(y)
print(z)

#Wiele zmiennych do jednej wartości
print("Wiele zmiennych do jednej wartości")
x=y=z="zasilacz"
print(x)
print(y)
print(z)

#Odpakowywanie kolekcji
print("Odpakowywanie kolekcji")
rtx=["3050", "3060", "3070", "3080", "3090"]
w, v, x, y, z=rtx
print(w)
print(v)
print(x)
print(y)
print(z)

#Zmienne wyjściowe
print(imie)
print(imie, wiek) #string, int --git
#print (imie+wiek) #string + int -nie git
print(imie+Imie)
rok=2022
print(rok+wiek) #int + int --git

#Globalne zmienne
miasto="Siemce" #zmienna globalna
def test1(): #funkcja, więcej o nich później
  print("Moje miasto to "+miasto)
test1()
def test2():
  miasto="Katowice" #zmienna w funkcji jest lokalna
  print("Moje miasto to "+miasto)
test2()
print("Moje miasto to "+miasto) #print jest poza funkcją więc nie bierze Katowic, które sa lokalne
def test3():
  global miasto #Tworzenie globalnej zmiennej w funkcji
  miasto="Będzin" #zmienna w funkcji jest globalna
test3()
print("Moje miasto to "+miasto) #print jest poza funkcją, lecz bierze będzin bo jest zmienną globalną

#TYPY ZMIENNYCH
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

#losowa liczba
import random
print(random.randrange(1, 10))

#STRING - ZWYKŁY TEKST
print("string")
x="Bartosz" #Bez określenia zmiennej
x=str("Bartosz") #Z okresleniem zmiennej.
print(x)

#wiele linijek
y="""Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.""" #By dać string w wielu linijkach trzeba dać """ """ lub ''' '''
print(y)

#Wyciągniecie znaku
x="XD"
print(x[0]) #0 to pierwszy znak

#pętla for w string'u
for x in "Bartosz":
  print(x)

#długość string'u
x="Bartosz"
print(len(x))

#sprawdź czy w string'u
z="O jasny ****, toż to laseraptor. Myślałem, że wygineły tysiące lat temu"
print("laseraptor" in z)
if "laseraptor" in z:
  print("Jak widać nie wygineły")

#sprawdź czy w string'u
z="O jasny ****, toż to laseraptor. Myślałem, że wygineły tysiące lat temu"
print("żyją" not in z)
if "żyją" not in z:
  print("Jak widać nie żyją")

#slicing string
b="Witaj świecie!"
print(b[2:8])
print(b[:5])
print(b[2:])
print(b[-5:-2])

#Modify strings
q=" Witaj, świecie! "
print(q.upper()) #CAPS LOCK ON
print(q.lower()) #caps lock off
print(q.strip()) #usuwa zbędne spacje
print(q.replace("W", "P")) #Zamienia znaki
print(q.split(",")) #Rozdziela słowa oddzielone w tym przypadku przecinek

#String Cocncatenation - Łączenie ciągów
a="Witaj"
b="świecie"
c= a+" "+b
print(c)

#String format - jak wiadomo nie można łączyc inta z stringiem, przez co można wykorzystać 'format'
wiek=16
tekst="Mam na imię Bartosz i mam {} lat"
print(tekst.format(wiek))
ilosc=4
nr_rzeczy=327
cena=34.80
moje_zamowienie="Poprosze {} kawałki rzeczy o numerze {} za {}"
print(moje_zamowienie.format(ilosc, nr_rzeczy, cena))
moje_2_zamowienie="Chciałbym zapłacić {2} za {0} kawałków rzeczy o numerze {1}" #wstawianie w nawiasy kolejności
print(moje_2_zamowienie.format(ilosc, nr_rzeczy, cena))

#Escape characters
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

#string methods - https://www.w3schools.com/python/python_strings_methods.asp


#INT - LICZBA CAŁKOWITA
print("int")
x=16
x=int(16)
print(x)
y=-3321
z=int(4.6) #int nie ma ułamków więc wynik to 4
w=int("5")
print(y)
print(z)
print(w)

#float - liczba wymierna
print("float")
x=16.5
x=float(16.5)
print(x)
y=float(18)
z=-314.32
print(y)
print(z)
v=35e3 #e lub E. float może mieć e by zaznaczyć moc 10
print(v)

#Matematyka
print("Matematyka")
x=35
y=5
z=6
print("Liczby to:", x, y, z)
print("Dodawanie:", x+y) #Dodawanie
print("Odejmowanie:", x-y) #Odejmowanie
print("Mnożenie:", x*y) #Mnożenie
print("Dzielenie:", x/z) #Dzielenie
print("Modulus:", x%y) #Modulus - Reszta z dzielenia
print("Potegowanie:", x**y) #Potęgowanie
print("Dzielenie zaokrąglone w dół:", x//z) #Zaokrągla dzielenie w dół, 35/6 = 5.8(3), leczy wynik będzie wynosił 5

x=35
print("Początkowa liczba:", x)
x+=5
print("Liczba po dodaniu 5 to:", x)
x-=10
print("Liczba po odjęciu to:", x)
x&=13 #AND, aktualnie x=30 czyli binarnie to 11110, a 13 binarnie to 01101, porównując bity te same to 01100, czyli 12
print(x)
x|=3
print(x)
x^=3
print(x)
x>>=1
print(x)
x<<=1
print(x)