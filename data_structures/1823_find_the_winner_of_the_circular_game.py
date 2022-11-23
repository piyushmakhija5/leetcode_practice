## https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        game = [i+1 for i in range(n)]
        start = 0
        while len(game) > 1:
            loser = (start+k-1)%(len(game))
            del game[loser]
            start = loser if loser <= len(game) else 0
            # print(loser, start, game)

        return game[0]
            
