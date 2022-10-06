class Solution {
public:
    bool isPalindrome(int x) {
      if(x<0|| (x!=0 &&x%10==0)) return false;
        int sum=0;
        while(x>sum)
        {
            sum = sum*10+x%10;
            x = x/10;
        }
        // cout<<(x==sum)<<endl;
        // cout<<(x==sum/10)<<endl;
        // cout<<x<<endl;
        // cout<<sum<<endl;
        return (x==sum)||(x==sum/10);
//         here in case of pailndrome x==sum/10 is always equal;
    
        
        
    }
};