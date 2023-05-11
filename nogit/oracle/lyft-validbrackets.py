class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"(":")","[":"]","{":"}"}
        openers = ["(","[","{"]
        closer = []
        list_brackets = list(s)
        for string in list_brackets:
            if string in openers:
                closer.append(string)
            else:
                if not closer or brackets[closer[len(closer)-1]] != string:
                    return False
                closer.pop(len(closer)-1)
        return len(closer) == 0
sol = Solution()
print(sol.isValid('(){}}{'))