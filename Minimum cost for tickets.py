class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp=[0]*(max(days)+1)
        dp[0]=0
        for i in range(1,max(days)+1):
            if i in days:
                a=i-1
                if a<0:
                    a=0
                b=i-7
                if b<0:
                    b=0
                c=i-30
                if c<0:
                    c=0
                dp[i]=min(dp[a]+costs[0] , dp[b]+costs[1] , dp[c]+costs[2])
            else:
                dp[i]=dp[i-1]
        return(dp[max(days)])
