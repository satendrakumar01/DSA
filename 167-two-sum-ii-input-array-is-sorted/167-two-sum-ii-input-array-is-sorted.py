class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        m={}
        for i,el in enumerate(numbers):
            if target-el in m :
                return [m[target-el]+1,i+1]
            m[el]=i