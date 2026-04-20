
from random import random

def gameOver(A, B):
    if A == 15 or B == 15:
        return True
    else:
        return False

def simOneGame(pA, pB):
   """

   :param pA: probability of A winning a point on serve
   :param pB: probability of B winning a point on serve
   :return: the score of the game for A, and for B
   """
   serving = "A"
   scoreA = 0
   scoreB = 0
   while not gameOver(scoreA, scoreB):
       if serving == "A":
           if random() < pA:
               scoreA += 1
           else:
               serving = "B"
       else:
           if random() < pB:
               scoreB += 1
           else:
               serving = "A"
   return scoreA, scoreB


def simNgames(n, pA, pB):
   """

   :param n: number of games to simulate
   :param pA: probability of A winning a point on serve
   :param pB: probability of B winning a point on serve
   :return: winA: the number of games won by A; winB: the number of games won by B
   """
   winA = 0
   winB = 0
   for i in range(n):
       scoreA, scoreB = simOneGame(pA, pB)
       if scoreA > scoreB:
           winA += 1
       else:
           winB += 1
   return winA, winB

def printIntro ():
   """
   This function prints out introductory text for the user
   :param: none
   :return: none
   """
   print("This program simulates a game of racquetball between two")
   print("players called 'A' and 'B' The skill of each player is")
   print("represented by the probability of that player winning a point")
   print("when that player serves. This probability is expressed as a")
   print("floating point number between 0 and 1")
   print("PLayer A will always serve first")

def getInputs():
   """
   This function prompts the user for three input values: the probability of
   A winning a point on serve; the probability of B winning a point on
   serve; and the number of games to simulate. (More games gives a truer
   probability of winning)
   :return: a: A's probability of winning; b: B's probability of winning;
   n: Number of games to simulate
   """
   a = float(input("Please enter the probability of A winning a point when serving: "))
   b = float(input("Please enter the probability of B winning a point when serving: "))
   n = int(input("Please enter the number of games to simulate: "))
   return a, b, n

def printSummary(winA, winB):
   """
   This function prints out the results of your simulation, in whatever
   format is desired.

   :param winA: the number of games won by A
   :param winB: the number of games won by B
   :return: None
   """
   n = winA + winB
   print("Games played: " + str(n))
   print("Wins for A: ", winA, "or :", 100*winA/n, " %")
   print("Wins for B: ", winB, "or :", 100*winB/n, " %")



if __name__ == "__main__":
   printIntro()
   a, b, n = getInputs()
   winA, winB = simNgames(n, a, b)
   printSummary(winA, winB)

