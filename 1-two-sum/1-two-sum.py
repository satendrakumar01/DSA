class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dick={}
        
        for i,el in enumerate(numbers):
            if target-el in dick:
                return [dick[target-el],i]
            else:
                dick[el]=i
