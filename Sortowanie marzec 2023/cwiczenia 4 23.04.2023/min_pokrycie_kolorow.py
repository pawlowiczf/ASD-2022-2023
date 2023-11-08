# Mamy tablice n-elementowa i kazdy element ma jakis kolor (niech to beda liczby).
# Jest kolorow k
# Znajdz podciag tablicy, ktory zawiera wszystkie kolory oraz jest najkrotszy

# Trzymaj k licznikow dla kazdego z kolorow O(n+k). Wykrywaj zmiany licznika z 0 na 1
# Licznik kolorow ktore mamy w biezacych przedziale, mozemy stwierdzic, czy mamy wszysktie kolory
# na poczatku cnt = 0, iterujemy dwoma indeksami po calej tablicy i, j. Oba na poczatku
# Dopoki nie mamy w naszym przedziale wszystkich kolorow zwiekszamy j, podbijamy counter. Jezeli
# counter osiagnie k, to mamy przedzial miedzy i, j ktory zawiera wszystkie kolory i mozemy zapisac te indeksy na boku
# Jesli mamy juz wszystkie kolory, to idziemy j i odejmujemy licznik kolorow cnt = k - 1. I idziemy takim robaczkiem
