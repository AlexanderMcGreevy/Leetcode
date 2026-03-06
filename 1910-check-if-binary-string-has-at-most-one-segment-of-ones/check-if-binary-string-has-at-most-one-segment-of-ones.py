class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        over = False
        for i in s:
            if i == "0":
                over = True
            elif i == "1" and over:
                return False
        return True



        