## https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:
        def getNext(n):
            list_n = list(str(n))
            ssq_n = sum([(int(x))**2 for x in list_n])
        # print(list_n, ssq_n)
        if ssq_n == 1:
            # print("it is happy")
            return True
        # elif ssq_n in seen:
        #     print("not happy")
        #     return False
        else:
            # print("more recursion")
            # seen.append(ssq_n)
            self.isHappy(ssq_n)
        
