using System;
// you can also use other imports, for example:
// using System.Collections.Generic;

// you can write to stdout for debugging purposes, e.g.
// Console.WriteLine("this is a debug message");

class Solution {
    public int solution(int[] A) {
        // write your code in C# 6.0 with .NET 4.5 (Mono)
        int n = A.Length;
        var leftSum = new int[n];
        var rightSum = new int[n];

        // 左から見た累積和
        for(int i = 1; i < n; ++i) leftSum[i] = Math.Max(0, leftSum[i - 1] + A[i]);

        // 右から見た累積和
        for(int i = n - 2; i >= 0; --i) rightSum[i] = Math.Max(0, rightSum[i + 1] + A[i]);

        // Console.WriteLine(string.Join(" ", leftSum));
        // Console.WriteLine(string.Join(" ", rightSum));

        // 左右の累積和の合計が最大になる中間点を探す
        int max = 0;
        for(int i = 1; i < n - 1; ++i){
            int sum = leftSum[i - 1] + rightSum[i + 1];
            if(max < sum) max = sum;            
        }
        return max;
    }
}
