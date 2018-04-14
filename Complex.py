#Rysowanie wykresów liczb zespolonych techniką kolorowania dziedziny

#Importy na samym początku, nie trzeba zwracać uwagi
import numpy as np
import matplotlib.pyplot as plt

#Ta część do łatwych zmian

#funkcja, której wykres ma zostać narysowany
def f(z):
    y = 0
    try:
	#Poniższa linijka to funkcja, dalej są błędy możliwe do napotkania
        y = z**7 - 1

    #Błąd dzielenia przez zero - daje wielką liczbę, bo granica dąży do +inf. - (3^40) + (3^40)*i
    except ZeroDivisionError:
        y = 3**40 + (3**40)*1j
    return y

#Dziedzina:
Dziedzina = 2 #Dla liczby n argumenty funkcji będą przyjmowały wartości takie, że
    #Re(z) należy do <-n, n>; Im(z) należy do <-n, n>
LiczbaKroków = 100 #To jest aktualna wielkość tablicy przechowywującej liczby:
    #Dla liczby n tablica będzie wielkości n x n - nie posiada informacji o wartościach

#Skala:
Skala = 40 #Kolor (prawie że) biały odpowiada liczbie podanej jako skala
#	Mnożniki w występującej funkcji jasności są dobrane w ten sposób
#Należy pamiętać, że większa skala oznacza, że większe wartości będą bardziej
#	widoczne jako kolor, ale mniejsze wartości będą bardziej czarne
#	Należy więc dobierać ją rozważnie

#--------------------------------------------
#Matplotlib w wersji 2.0.2:
    #2.2.2 pokazywała wewnętrzny typeError
    #2.1.2 wykrywała kolory poza zasięgiem 0..1 mimo, że nie było ich w tablicy

#Ta część to aktualny kod programu

#Zamiana koloru z HSL do RGB
#Algorytm: https://www.rapidtables.com/convert/color/hsl-to-rgb.html
#Przyjmowane argumenty: kolor jako tablica w postaci [H, S, L]
#H - odcień - w stopniach <0, 360)
#S - nasycenie - jako ułamek (w tym zastosowaniu - zawsze 1)
#L - jasność - jako ułamek
#Zwraca tablicę z kolejnymi wartościami koloru:
#[R, G, B]

def HSLtoRGB(color):
    H = color[0]
    S = color[1]
    L = color[2]

    C = (1 - abs(2*L -1) )*S
    X = C*(1 - abs( ((H/60)%2) - 1) )
    m = L - C/2

    Rp = Gp = Bp = 0

    if(H >= 0 and H < 60):
        Rp = C
        Gp = X
    elif(H >= 60 and H < 120):
        Rp = X
        Gp = C
    elif(H >= 120 and H < 180):
        Gp = C
        Bp = X
    elif(H >= 180 and H < 240):
        Gp = X
        Bp = C
    elif(H >= 240 and H < 300):
        Rp = X
        Bp = C
    elif(H >= 300 and H < 360):
        Rp = C
        Bp = X

    return [(Rp+m), (Gp+m), (Bp+m)]

#-----------------------------------------------

#Na początku Funkcja Gudermanna (stąd nazwa), następnie zamieniona w wykładniczą,
#	zamieniająca moduł liczby w liczbę od 0 do 1 - do przeliczania jasności
#   gd(0) = 0, rośnie asymptotycznie do 1, dla gd(35) ~= 0.964416
def gd(var):
    return -1.1**(-var) + 1

#-----------------------------------------------

#Za kolor praktycznie biały uznawana jest liczba będącą Skalą - z powodu
#	przeskalowania

def obliczJasnosc(modul):
    return gd(35*modul / Skala )

#-----------------------------------------------

#Funckja zamieniająca liczbę na kolor w postaci tablicy koloru HSL: [H, S, L]

def obliczHSL(liczba):
    H = np.angle(liczba, True)
    if H < 0:
        H += 360
    S = 1
    L = obliczJasnosc(np.absolute(liczba))
    return [H, S, L]

#------------------------------------------------

#Funkcja zamieniająca liczbę zespoloną na RGB - wywołuje oblicznie HSL na liczbie będącej
#   wynikiem funkcji f(z) na podanej liczbie i od razu zamienia HSL w RGB

def getColor(liczba):
    return HSLtoRGB( obliczHSL( f( liczba ) ) )

#------------------------------------------------

#Tworzy tablicę, która początkowo ma w sumie same liczby zespolone wg podanych na górze
#   wartości
varTab = [ [x for x in range(LiczbaKroków+1)] for y in range(LiczbaKroków+1)] #Początkowo zawiera liczby z R
krok = (2*Dziedzina)/LiczbaKroków #Ile ma być dodawane co krok, aby się zgadzało
for x in range(LiczbaKroków+1):
    for y in range(LiczbaKroków+1):
        varTab[x][y] = (-Dziedzina + krok*x)*1j + (-Dziedzina + krok*y)  #Wypełnianie tablicy liczbami zespolonymi

#Zamiana liczb zespolonych z tablicy na kolory - od razu w RGB: Używana jest dodatkowa Funkcja
#   w zasadzie jedynie upraszaczjąca zapis w tym miejscu
for x in range(LiczbaKroków+1):
    for y in range(LiczbaKroków+1):
        varTab[x][y] = getColor(varTab[x][y])

#Włożenie tablicy z kolorami do wykresu
plt.imshow(varTab, interpolation="bilinear", extent=[-Dziedzina, Dziedzina, Dziedzina, -Dziedzina])

#Pokazanie wykresu
plt.show()
