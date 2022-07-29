# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root :
            return 0
        
        queue=[[root]]# we make a queue here and it also contain nextLevel
        
        output=[] #output array to store logest chain of tree of elements level by level {[3],[9,20],[15,7]}
        
        while queue:#checking while queue
            
            level=queue.pop(0)#pop out the root from queue and store the root in level variable 
            
            output.append(item.val for item in level )#append the data or value of root present in variable                                                           #level to output
            
            nextLevel=[] # here from the next 
            for item in level:#level took each element refernce of queue.pop temporay  
                
                
                if item.left:# check if item left 
                    
                    nextLevel.append(item.left)# append to nextlevel
                    
                if item.right:# chek if item right 
                    
                    nextLevel.append(item.right) #append to nextlevel
                    
            if nextLevel:#if next level has element then 
                
                queue.append(nextLevel) #APPEND IN QUEUE TO 
                
                
        return len(output)#HERE LENGTH OF OUTPUT  WHICH HAVE  ALL LEVEL LENGTH
                
        
        