using System;
using System.Linq;
using System.Collections.Generic;
// you can also use other imports, for example:
// using System.Collections.Generic;

// you can write to stdout for debugging purposes, e.g.
// Console.WriteLine("this is a debug message");

class Solution {
    public int solution(int[] A) {
        // write your code in C# 6.0 with .NET 4.5 (Mono)
        int n = A.Length;
        
        // nの約数を見つける(同じ数のブロックで分割するため)
        var dic = new Dictionary<int, bool>();
        int sqn = (int)Math.Ceiling(Math.Sqrt(n));
        for(int i = 1; i <= sqn; ++i){
            if(n % i == 0){
                dic[i] = true;
                dic[n / i] = true;
            }
        }
        var divisor = new int[dic.Keys.Count()];
        dic.Keys.CopyTo(divisor, 0);
        Array.Sort(divisor);
        //Console.WriteLine(string.Join(" ", divisor));

        var peaks = new List<int>();
        for(int i = 1; i < n - 1; ++i){
            if(A[i - 1] < A[i] && A[i] > A[i + 1]) peaks.Add(i);
        }
        int pn = peaks.Count;
        //Console.WriteLine(string.Join(" ", peaks));

        // 上から順番に見てみる (1ブロックはどうせ無理なのでパス -2から)
        for(int i = divisor.Length - 2; i >= 0; --i){
            int div = divisor[i];
            int blockSize = n / div;
            //Console.WriteLine("i:" + i + " div:" + div + " pn:"+ pn +" blocksize:" + blockSize);
            // 割り切れる範囲にpeaksが入っているか確認していく
            int block = 0; // 現在参照しているブロック
            int j = 0;
            while (j < pn){
                //範囲外ならだめ
                int pj = peaks[j];
                int left = block * blockSize;
                int right = (block + 1) * blockSize; 
                
                // Console.WriteLine("j:"+ j +" block:"+ block + " pj:" + pj + " left:" + left + " right:"+ right);
                if(pj < left || right <= pj) break;

                // 範囲端ならとりあえず次
                // if(pj == left || right == pj) {
                //     j += 1;
                //     continue;
                // }

                //範囲内の間進める                
                while(left <= pj && pj < right && j < pn - 1) {
                    j += 1;
                    pj = peaks[j];
                } 
                block += 1;
            }
            // block が n / div と同じなら全てのブロックにピークがある
            if(block >= div){
                return div;
            }
        }

        return 0;
    }
}
