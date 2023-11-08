"""
Mamy graf, ktory reprezentuje nam wymiany walut. Np. za jednego dolara mozna dostac 1,2 euro
Za 1 euro mozna dostac 0,8 funta. Za 1 funta, mozna dostac 5 zl. Za 1 zl mozna dostac 0,3 dolara.
Mozemy sie wzbogacic, dokonujac cyklu kolejnych wymian walut 

Naszym zadaniem jest sprawdzic, czy jak dostaniemy taka liste wymian pomiedzy walutami, to czy istnieje taki ckyl
wymian, ze z 1 zlotowki dostaniemy wiecej. 

Bellman Ford, cykl o ujemnej wadze czy wystapil???

"""


"""
Zadanie 1. (malejace krawedzie, c.d.) Dany jest graf G = (V,E), gdzie kazda krawedz ma wage
ze zbioru {1, . . . , |E}} (wagi krawedzi sa parami rózne). Prosze zaproponowac algorytm, który dla danych
wierzchołków x i y oblicza sciezke o najmniejszej sumie wag, która prowadzi z x do y po krawedziach o
malejacych wagach (jesli sciezki nie ma to zwracamy inf).

Odpowiednio posortowac krawedzie, wedlug kosztu malejaco 
Mamy nieskonoczonosci w wierzcohlkach
DOdajemy do drogi lub nie krawedzie, jesli bylibysmy w stanie polepszyc te nasza odleglosc 

Bierzemy 
Jedna iteracja Bellmana-Forda


"""

