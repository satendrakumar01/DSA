class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x=0
        dict={"--X":-1,"X++":1,"X--":-1,"++X":1}
        for item in operations:
            if item in dict:
               x=x+dict[item]
        return x
        