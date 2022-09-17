class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximum=0
        for item in accounts:
            a=sum(item)
            if a>maximum:
                maximum=a
        return maximum
        