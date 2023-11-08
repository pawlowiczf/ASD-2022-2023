"""
Problem komiwojazera (travelling salesman problem, TSP)
Mamy miasta C = {0,1,...,n-1} oraz odleglosci miedzy nimi D (macierz)
Miasta leza na plaszczyznie

Zadanie polega na znalezieniu kolejnosci odwiedzania miast, tak, by zaczac od miasta 0,
skonczyc w 0 (cykl), odwiedzic wszystkie miasta, pokonujac droge o najmniejszej sumie odleglosci miedzy miastami.

1) Okreslenie funkcji:
f(S, t) - dlugosc najkrotszej trasy, ktora startuje w 0, odwiedza wszystkie miasta ze zbioru S i konczy w miescie t ( 0, t nalezy do zbioru S )

2) Zapis rekurencyjny:
f(S, t) = min( f(S-{t}, r) + d(r, t) ), gdzie r nalezy do S-{t}
Innymi slowy, szukamy minimum po trasie, ktora odwiedza wszystkie wierzcholki z S-{t} i konczy sie w 'r' + d(r,t)

3) Warunek brzegowy:
f( {0}, 0 ) = 0
else inf

4) Odczytywanie wyniku:

"""


def setup(D, S, F): # D - odleglosci miedzy miastami, S - wierzcholek startowy, Memo - tablica do zapisywania wartosci funkcji f()
    #
    n = len(D)

    for city in range(n):
        if city != S:
            F[ city ][ 1 << S | 1 << city ] = D[S][city]
    #
    return F
#end procedure setup()


def contain(i, subset):
    return ( ( 1 << i ) & subset ) != 0
#end procedure contain()


def solve(D, S, F):
    #
    n = len(D)

    for length in range(3, n + 1):
        for subset in combinations(length, n):
        
            if contain(S, subset):

                for next in range(n):
                    if next != S and contain(next, subset):
                        state = ( 1 << next ) ^ subset 
                        minDist = float('inf')
                    
                        for end in range(n):
                            if  end != S and end != next and contain(end, subset):
                                F[next][subset] = min( F[next][subset], F[end][state] + D[end][next] )
                        #end 'for' loop
                #end 'for' loop
    #end 'for' loops

    return F
#end procedure solve()


def ConvertBinary(number):
    #
    sequence = [] 

    while number > 0:
        sequence.append( number % 2 )
        number = number // 2
    #

    return sequence
#end proedure ConvertBinary()


def countOnes(length, number):
    #
    sequence = ConvertBinary(number)
    counter = 0

    for bit in sequence:
        counter += bit
    #

    return counter == length
#end procedure countOnes()


def combinations(length, n):
    #
    setBit = []
    for number in range( 2 ** n ):
        if countOnes(length, number):
            setBit.append(number)
    #

    return setBit
#end procedure combinations()


def findMinimalCost(D, S):
    #
    n = len(D)
    F = [ [ float('inf') for _ in range( 2 ** n ) ] for _ in range(n) ]
    endState = ( 1 << n ) - 1
    minTourCost = float('inf')

    F = setup(D, S, F)
    F = solve(D, S, F)

    for end in range(n):
        if end != S:
            minTourCost = min( minTourCost, F[end][endState] + D[end][S] )
    #end for

    return minTourCost
#end procedure findMinimalCost()



# Testy:

D = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
print( findMinimalCost(D, 0) )


D = [ [107,816,247,307,92,417,423,55,365,876,435,456,299,101,577,324,10,335,978,130],
[94,146,382,92,570,256,895,664,574,853,571,507,301,493,250,952,584,144,319,61],
[365,916,585,259,660,605,759,975,189,698,449,670,264,140,359,372,281,698,157,772],
[839,860,603,100,651,676,711,572,505,120,499,423,904,389,635,431,710,234,260,866],
[93,254,382,986,18,840,676,346,94,706,457,937,305,325,798,299,738,84,810,996],
[539,137,723,644,620,712,389,126,490,450,594,717,646,169,856,273,495,279,57,848],
[909,307,516,917,945,78,559,882,704,155,670,715,117,335,777,971,385,367,974,325],
[161,969,7,347,475,973,158,601,703,693,460,307,994,174,193,519,218,352,449,227],
[962,602,600,942,197,912,690,224,578,266,888,145,366,564,876,978,920,356,219,577],
[441,808,949,345,914,614,407,162,239,830,76,416,28,282,137,273,856,578,643,957],
[394,794,246,421,237,23,522,68,457,105,684,572,603,4,722,129,587,663,84,667],
[201,295,715,818,883,274,901,816,400,515,922,104,794,844,577,73,737,692,229,660],
[361,454,720,921,3,142,61,151,297,304,791,283,291,820,158,74,504,799,125,551],
[211,721,293,143,690,557,984,726,212,834,989,236,469,344,822,844,462,251,494,868],
[874,204,899,266,188,63,899,941,841,968,320,104,206,68,494,918,811,983,529,767],
[595,677,681,160,336,341,837,145,404,991,504,440,16,335,254,851,1000,491,769,98],
[333,588,694,477,675,595,858,149,972,677,761,468,970,54,991,374,68,832,783,137],
[197,225,379,451,654,298,138,809,133,854,105,732,614,864,525,55,39,144,431,504],
[352,39,151,380,551,218,708,865,241,898,70,322,5,110,102,369,269,89,601,704],
[115,519,166,58,81,231,71,129,612,143,228,540,697,590,968,624,435,772,215,556 ] ]
print( findMinimalCost(D, 0) ) # 1708
