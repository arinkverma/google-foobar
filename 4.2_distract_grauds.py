# Distract the Guards
# ===================

# The time for the mass escape has come, and you need to distract the guards so that the bunny prisoners can make it out! Unfortunately for you, they're watching the bunnies closely. Fortunately, this means they haven't realized yet that the space station is about to explode due to the destruction of the LAMBCHOP doomsday device. Also fortunately, all that time you spent working as first a minion and then a henchman means that you know the guards are fond of bananas. And gambling. And thumb wrestling.
# The guards, being bored, readily accept your suggestion to play the Banana Games.
# You will set up simultaneous thumb wrestling matches. In each match, two guards will pair off to thumb wrestle. The guard with fewer bananas will bet all their bananas, and the other guard will match the bet. The winner will receive all of the bet bananas. You don't pair off guards with the same number of bananas (you will see why, shortly). You know enough guard psychology to know that the one who has more bananas always gets over-confident and loses. Once a match begins, the pair of guards will continue to thumb wrestle and exchange bananas, until both of them have the same number of bananas. Once that happens, both of them will lose interest and go back to guarding the prisoners, and you don't want THAT to happen!
# For example, if the two guards that were paired started with 3 and 5 bananas, after the first round of thumb wrestling they will have 6 and 2 (the one with 3 bananas wins and gets 3 bananas from the loser). After the second round, they will have 4 and 4 (the one with 6 bananas loses 2 bananas). At that point they stop and get back to guarding.
# How is all this useful to distract the guards? Notice that if the guards had started with 1 and 4 bananas, then they keep thumb wrestling! 1, 4 -> 2, 3 -> 4, 1 -> 3, 2 -> 1, 4 and so on.
# Now your plan is clear. You must pair up the guards in such a way that the maximum number of guards go into an infinite thumb wrestling loop!
# Write a function answer(banana_list) which, given a list of positive integers depicting the amount of bananas the each guard starts with, returns the fewest possible number of guards that will be left to watch the prisoners. Element i of the list will be the number of bananas that guard i (counting from 0) starts with.
# The number of guards will be at least 1 and not more than 100, and the number of bananas each guard starts with will be a positive integer no more than 1073741823 (i.e. 2^30 -1). Some of them stockpile a LOT of bananas.


class Graph:
    def __init__(self,banana_list):
        self.list_len = len(banana_list)
        self.graph = list([0]*self.list_len for i in xrange(self.list_len))
        for i in xrange(self.list_len):
            for j in xrange(self.list_len):
                if i < j: 
                    self.graph[i][j] = self.dead_lock(banana_list[i], banana_list[j])
                    self.graph[j][i] = self.graph[i][j]  

    def gcd(self, x, y):
       while(y):
           x, y = y, x % y
       return x

    def dead_lock(self, x,y):
        if x == y:
            return 0

        l = self.gcd(x,y)

        if (x+y) % 2 == 1:
            return 1

        x,y = x/l,y/l
        x,y = max(x,y), min(x,y)    
        return self.dead_lock(x-y,2*y)
 
    # A DFS based recursive function that returns true if a
    # matching for vertex u is possible
    def bpm(self, u, matchR, seen):
        for v in range(self.list_len):
            if self.graph[u][v] and seen[v] == False:
                seen[v] = True # Mark v as visited
 
                if matchR[v] == -1 or self.bpm(matchR[v], matchR, seen):
                    matchR[v] = u
                    return True
        return False
 
    # Returns maximum number of matching 
    def maxGaurdPair(self):
        matchR = [-1] * self.list_len
        result = 0 # Count of graud match
        for i in range(self.list_len):
            seen = [False] * self.list_len
            if self.bpm(i, matchR, seen):
                result += 1
        return self.list_len- 2*(result/2)


def answer(l):
    return Graph(l).maxGaurdPair()
    
