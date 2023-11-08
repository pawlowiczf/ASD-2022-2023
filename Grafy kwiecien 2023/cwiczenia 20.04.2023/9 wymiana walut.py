# Dana jest tabela kursów walut. Dla kazdych dwóch walut x oraz y wpis
# K[x][y] oznacza ile trzeba zapłacic waluty x zeby otrzymac jednostke waluty y. Prosze zaproponowac algorytm,
# który sprawdza czy istnieje taka waluta z, ze za jednostke z mozna uzyskac wiecej niz jednostke z
# przez serie wymian walut.

"""

Mamy graf, ktory reprezentuje nam wymiany walut. Np. za jednego dolara mozna dostac 1,2 euro
Za 1 euro mozna dostac 0,8 funta. Za 1 funta, mozna dostac 5 zl. Za 1 zl mozna dostac 0,3 dolara.
Mozemy sie wzbogacic, dokonujac cyklu kolejnych wymian walut 

Naszym zadaniem jest sprawdzic, czy jak dostaniemy taka liste wymian pomiedzy walutami, to czy istnieje taki ckyl
wymian, ze z 1 zlotowki dostaniemy wiecej. 

Bellman Ford, cykl o ujemnej wadze czy wystapil???

"""

def vertex(edges):
    n = 0 
    for edge in edges:
        n = max( n, edge[0], edge[1] )
    #
    return n + 1 
#end procedure vertex()


def relax(cost, z, currencies, k):
    firstCurrency, secondCurrency, converter = currencies[k]
    #
    if cost[ secondCurrency ] < cost[ firstCurrency ] * converter:
        cost[ secondCurrency ] = cost[ firstCurrency ] * converter 

        if secondCurrency == z:
            return True 
    #
    return False 
#end procedure relax()

def BellmanFord(currencies, z):
    n = vertex(currencies)
    cost = [ 0 for _ in range(n) ]
    cost[0] = 1

    for _ in range( n - 1 ):
        for k in range( len(currencies ) ):
            if relax( cost, z, currencies, k ):
                return True 
        #
    #
    return False 
#end procedure BellmanFord()

currencies = [(0, 1, 4.5),
              (0, 2, 4),
              (2, 0, 0.25),
              (1, 2, 0.75),
              (3, 2, 100),
              (0, 3, 0.4),
              (1, 4, 6),
              (3, 4, 2)]    

print( BellmanFord(currencies, 0) )


currencies = [
                (0,1 ,1),
                (1,2,2),
                (2,3,3),
                (3,0,0.1)

             ]

print( BellmanFord(currencies, 0) )