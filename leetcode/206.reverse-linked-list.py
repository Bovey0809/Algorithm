public static void main(String[] args) {
    int n = 5
    int k = 10
    int x = 100
    int[] price = new int[] {30, 25, 50, 25, 50}
    int[][] dp = new int[n * k][n]
    for (int i=0
         i < dp.length
         i + +) {
        for (int j=0
             j < dp[0].length
             j + +) {
            dp[i][j] = -1
        }
    }

    dp[0][0] = x
    for (int i=1
         i <= x / price[0]
         i + +) {
        dp[i][0] = dp[0][0] - i * price[0]
    }

    for (int i=1
         i < n
         i + +) {

        // System.out.println()

        for (int j=0
             j < n * k
             j + +) {
            int low = Math.max(0, j - k)
            int high = Math.min(n * k, j + k)
            int max = -1
            for (int kk=low
                 kk < high
                 kk + +) {
                if (kk < j) {
                    int tmp = dp[kk][i - 1] - price[i] * (j - kk)
                    if (tmp < 0) continue
                    max = Math.max(max, tmp)
                } else if (kk > j) {
                    if (dp[kk][i - 1] == -1) continue
                    int tmp = dp[kk][i - 1] + price[i] * (kk - j)
                    max = Math.max(max, tmp)
                } else {
                    max = Math.max(max, dp[kk][i - 1])
                }
            }
            dp[j][i] = max
        }

        // print
        // for (int f=0
                f < dp.length
                f + +) {
            // for (int b=0
                    b < dp[0].length
                    b + +) {
                // System.out.print(dp[f][b] + " ")
                // }
            // System.out.println()
            //}
    }

    System.out.println(dp[0][n - 1])
}
