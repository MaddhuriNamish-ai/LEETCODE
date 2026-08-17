class Solution {
public:
    int stoneGameV(vector<int>& stoneValue) {
        int n = stoneValue.size();
        vector<long long> pre(n + 1, 0);
        for (int i = 0; i < n; i++) pre[i + 1] = pre[i] + stoneValue[i];
        
        auto rangeSum = [&](int i, int j) -> long long {
            return pre[j + 1] - pre[i];
        };
        
        vector<vector<int>> dp(n, vector<int>(n, 0));
        
        for (int len = 2; len <= n; len++) {
            for (int i = 0; i + len - 1 < n; i++) {
                int j = i + len - 1;
                int best = 0;
                for (int k = i; k < j; k++) {
                    long long sum1 = rangeSum(i, k);
                    long long sum2 = rangeSum(k + 1, j);
                    int candidate;
                    if (sum1 < sum2) {
                        candidate = (int)sum1 + dp[i][k];
                    } else if (sum2 < sum1) {
                        candidate = (int)sum2 + dp[k + 1][j];
                    } else {
                        candidate = (int)sum1 + max(dp[i][k], dp[k + 1][j]);
                    }
                    best = max(best, candidate);
                }
                dp[i][j] = best;
            }
        }
        
        return dp[0][n - 1];
    }
};