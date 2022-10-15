class Solution:
    def romanToInt(self, s: str) -> int:
        
        m={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        # b=[]
        sum=m[s[len(s)-1]]
        
        # for key in s:
        #     b.append(a[key])
            
        for i in range(len(s)-1):
            if(m[s[i]]<m[s[i+1]]):
                sum-=m[s[i]]
            else:
                sum+=m[s[i]]
            
            
            
                
        return sum
            
#            int sum=0;
#         unordered_map<char, int> m = {{'I', 1}, {'V', 5}, {'X', 10}, {'L', 50}, {'C', 100}, {'D', 500}, {'M', 1000}};
#         for(int i=0;i<s.length();i++)
#         {
#             if(m[s[i]]<m[s[i+1]])
#                 sum-=m[s[i]]; // when a smaller weight symbol comes before a larger weight symbol  ...example IV =  5-1 so we subtract 1 
       
#             else
#                 sum+=m[s[i]]; 
#         }
#         return sum;
        