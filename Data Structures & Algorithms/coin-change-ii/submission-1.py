class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Phase 1: Allocate state array and set base case
        dp = [0] * (amount + 1)
        dp[0] = 1

        # Phase 2: Process one coin denomination at a time
        for c in coins:
            # Phase 3: Sweep all possible amounts that this coin can contribute to
            for a in range(c, amount + 1):
                dp[a] += dp[a - c]

        # Phase 4: Final extraction
        return dp[amount]