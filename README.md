# DomainColoring
Wykresy metodą kolorowania dziedziny w Pythonie. Nie oblicza poprawnie granic przy dzieleniu przez 0 - w tych miejscach wykresy są niepoprawne. Lista rzeczy, które warto zmienić korzystając z kodu:
-------------------------------------------------------------------------------------------------

# Dziedzina:
liczby na płaszczyźnie zespolonej będą miały części rzeczywiste położone pomiędzy -Dziedzina a Dziedzina. Podobnie części zespolone. Tak więc - dla Dziedzina = 2 płaszczyzna pokaże wykres dla liczb od -2-2i do 2+2i.

# LiczbaKrokow:
zostanie wygenerowanych kwadrat podanej wartości +1 liczb (inaczej mówiąc - każda z osi zostanie podzielona na LiczbaKrokow części) Tak więc dla LiczbaKrokow = 100 i Dziedzina = 2, pojawi się nam 101 możliwych równomiernie rozłożonych wartości liczb (zarówno części rzeczywistej, jak i urojonej). Czas obliczeń dość mocno rośnie przy jej zwiększaniu, ale wykresy są dokładniejsze.

# Skala:
w obliczeniach dotyczących jasności parametry są dobrane w taki sposób, że skala będzie wartością modułu, dla którego liczba będzie prawie że całkiem biała. Zwiększanie skali powoduje, że znacznie większe liczby mają żywe kolory, ale jednocześnie mniejsze liczby zlewają się czernią. Małe skale powodują odwrotny efekt - dobrze widać małe liczby, ale duże są jednolicie białe.

# f(z):
chociaż funkcja zdaje się być złożona, interesująca jest tylko jedna linijka - w bloku try:
y = ..... <- tutaj, po znaku równości, należy wprowadzić funkcję wykorzystując operatory pythona oraz numpy (jako np.funkjca()). Początkowo funkcja miała być znacznie prostsza, ale dzielenie przez zero powodowało błąd - więc musiałem wprowadzić obsługę tego błędu. Każdorazowe dzielenie przez zero automatycznie przypisuje funkcji wartość 3^40 + 3^40i, przy czym 3^40 zostało wybrane raczej przypadkowo i wynosi trochę ponad 1.2e19. Pamiętać, że argument to z, a nie x.

Po wygenerowaniu wykresu warto wygenerować wykres dla y = z bez zmiany skali (ale prawdopodobnie dobrze może być zmienić dziedzinę). Dzięki temu można potem zobaczyć, jakie wartości przymował pierwszy wykres.
