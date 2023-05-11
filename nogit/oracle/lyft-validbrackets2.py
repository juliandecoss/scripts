class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"(":")","[":"]","{":"}"}
        openers = ["(","[","{"]
        closer = []
        list_brackets = list(s)
        sol = True
        def checker(string):
            if string in openers:
                closer.append(string)
            else:
                if not closer or brackets[closer[len(closer)-1]] != string:
                    sol =  False
                closer.pop(len(closer)-1)
            return closer
        list(map(checker,list_brackets))
        if not sol:
            return False
        return len(closer) == 0
sol = Solution()
print(sol.isValid(']'))