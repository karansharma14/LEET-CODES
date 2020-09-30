class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ar=[amount+1]*(amount+1)
        ar[0]=0
        for i in range(1,amount+1):
            for j in coins:
                if i>=j:
                    ar[i]=min(ar[i],ar[i-j]+1)
        if ar[amount]==amount+1:
            return(-1)
        return(ar[amount])
