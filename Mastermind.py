import random
from itertools import permutations
import matplotlib.pyplot as plt

COLOR_LIST = ["red", "blue", "green", "yellow", "white", "black"]
ALL_PERMUTATIONS = list(permutations(COLOR_LIST, 4))

class Sequence:
    def __init__(self, p1, p2, p3, p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4

    def getSequence(self):
        return [self.p1, self.p2, self.p3, self.p4]

    def compareSequence(self, other):
        redCount = 0
        whiteCount = 0
        for i in range(4):
            if self.getSequence()[i] == other.getSequence()[i]:
                redCount += 1
            elif self.getSequence()[i] in other.getSequence():
                whiteCount += 1
        return redCount, whiteCount

def takeTurn(guess):
    # make guess
    guesses.append(guess)
    print("guess:",guess.getSequence())

    # score guess
    redCount, whiteCount = guess.compareSequence(solution)
    scores.append([redCount, whiteCount])
    print(redCount,"red,",whiteCount,"white")

#num_turns = []
#for k in range(1000):
p1, p2, p3, p4 = random.choice(ALL_PERMUTATIONS)
solution = Sequence(p1, p2, p3, p4)
print("solution:",solution.getSequence())

# generate random first guess
p1, p2, p3, p4 = random.choice(ALL_PERMUTATIONS)
guess = Sequence(p1, p2, p3, p4)

guesses = []
scores = []

takeTurn(guess)

while guess.getSequence() != solution.getSequence():
    # compare guess with previous guesses to see if it meets the criteria
    i = 0
    j = 0
    while i < len(guesses):
        t1, t2, t3, t4 = ALL_PERMUTATIONS[j]
        guess = Sequence(t1, t2, t3, t4)
        redTest, whiteTest = guess.compareSequence(guesses[i])
        redCount, whiteCount = scores[i][0], scores[i][1]
        if redTest == redCount and whiteTest == whiteCount:
            i += 1
        else:
            i = 0
            j += 1

    takeTurn(guess)

print("solved in",len(guesses),"turns")
#num_turns.append(len(guesses))

#plt.hist(num_turns, bins=[1,2,3,4,5,6,7])
#plt.show()