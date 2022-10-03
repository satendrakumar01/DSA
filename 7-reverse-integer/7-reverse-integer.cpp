class Solution {
public:
  int reverse(int x) {
        long int rev=0,r;
         while(x!=0)
        {
            r=x%10;
            rev = rev*10+r; 
             if(rev<INT_MIN || rev>INT_MAX)
             {
                 return 0;
             }
             x=x/10; 
             }
        return rev;
    }
};