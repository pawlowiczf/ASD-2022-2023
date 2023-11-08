"""
Filip Pawlowicz 414324 
Algorytm dynamiczny, funkcja F(i, b) - minimalny koszt dotarcia do planety n - 1, bedac na planecie 'i', i majac w zapasie 'b' paliwa.
Tablice dynamiczna wypelniam rekurencyjnie ( ze spamietywaniem ), na kazdej planecie rozwazam wszystkie mozliwe zatankowania i sprawdzam, jaki jest
koszt dotarcia do planety B. Ponadto, jesli fuel == 0, teleportuje sie na dana planete i proces jest powtarzany.
W ten sposob oczywiscie po wywolaniu funkcji rekurencyjnej dla planety A i fuel == 0 dostane minimalny koszt trasy. 

W kazdej instacji rekurencji mam 2 zagniezdzone petle, ktorych zlozonosc wynosi n * E. Wywoluje rekurencyjnie wszystkie mozliwe
zatankowania, wiec zlozonosc bedzie rzedu O(nE^2) albo O(n^2 * E^2) (ciezko mi okreslic). 
Jest to wiec zlozonosc wielomianowa wzgledem n i E. 

"""

from egz1btesty import runtests

class DataCreate:
    def __init__(self, D, C, F, E, T):
        self.D = D
        self.C = C 
        self.F = F
        self.E = E 
        self.T = T 
        self.n = len(D)
#end class 

def Rek(Data, a, fuel):
    #
    if a == Data.n - 1: return 0

    if Data.F[a][fuel] == float('inf'):

        if fuel == 0:
            b, price = Data.T[a]
            if a != b:
                Data.F[a][fuel] = min( Data.F[a][fuel], Rek(Data, b, 0) + price )
        #end 'if' clause
        
        for tank in range( fuel, Data.E + 1 ):
            costTank = ( tank - fuel ) * Data.C[a]

            b = a + 1
            while b < Data.n and Data.D[b] - Data.D[a] <= tank:
                Data.F[a][fuel] = min( Data.F[a][fuel], Rek(Data, b, tank - ( Data.D[b] - Data.D[a] ) ) + costTank )
                b += 1
            #end 'while' loop
        #end 'for' loop 
    #end 'if' clause 
    return Data.F[a][fuel]
#end procedure Rek()

def planets( D, C, T, E ):
    # 
    F = [ [ float('inf') for _ in range(E + 1) ] for _ in range( len(D) ) ]
    Data = DataCreate(D, C, F, E, T)

    return Rek(Data, 0, 0)
#end procedure planets()

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = True )
