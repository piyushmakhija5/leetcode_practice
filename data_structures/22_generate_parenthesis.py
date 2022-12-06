## https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.n = n
        self.res = []
        self.dfs(0,0,[])
        return self.res

    def dfs(self, i, j, path):
        if i== self.n:
            while len(path) != self.n*2:
                path.append(')')
            self.res.append("".join(path))
            return
        self.dfs(i+1,j,path+["("])
        if j<i:
            self.dfs(i, j+1, path+[")"])
        return

        
        
        ## Recursion using yield and generate functions
        # def generate(p, left, right):
        #     if right >= left >= 0:
        #         if not right:
        #             yield p
        #         for q in generate(p + '(', left-1, right): yield q
        #         for q in generate(p + ')', left, right-1): yield q
        # return list(generate('', n, n))


    # ## Recursion using left right count
    #     def helper(p, left, right, parens=[]):
    #         print(p, left, right)
    #         if left:
    #             helper(p + '(', left-1, right)
    #         if right>left:
    #             helper(p + ')', left, right-1)
    #         if not right:
    #             parens += p, ## what is this??
    #         return parens
    #     return helper('', n, n)
