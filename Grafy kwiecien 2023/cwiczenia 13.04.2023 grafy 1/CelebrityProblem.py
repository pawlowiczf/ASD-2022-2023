"""
In a party of N people, only one person is known to everyone. Such a person may be present at the party, 
if yes, (s)he doesn’t know anyone at the party. We can only ask questions like “does A know B? “. 
Find the stranger (celebrity) in the minimum number of questions.
We can describe the problem input as an array of numbers/characters representing persons in the party. 
We also have a hypothetical function HaveAcquaintance(A, B) which returns true if A knows B, and false otherwise. How can we solve the problem? 
"""

def Knows(G, personA, personB):
    return G[personA][personB]
#end procedure Knows()


def FindCelebrity(G):
    #
    n = len(G)
    stack = []

    for person in range(n):
        stack.append(person)

    while len(stack) > 1:
        #
        personA, personB = stack.pop(), stack.pop()

        if Knows(G, personA, personB):
            stack.append( personB )
        elif Knows(G, personB, personA):
            stack.append( personA )

    #end 'while' loop

    if len(stack) == 0: return -1
    potentialCelebrity = stack.pop()

    for person in range(n):
        if person != potentialCelebrity and not Knows(G, person, potentialCelebrity) or Knows(G, potentialCelebrity, person):
                return -1
    #end 'for' loop 

    return potentialCelebrity
#end procedure FindCelebrity()