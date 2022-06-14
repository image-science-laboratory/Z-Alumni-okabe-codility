// you can use includes, for example:
// #include <algorithm>

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

#include <algorithm>
#include <cmath>
#include <unordered_map>
#include <vector>

vector<int> solution(int N, vector<int> &P, vector<int> &Q) {
  // write your code in C++14 (g++ 6.2.0)

  // 自然数Nを割る最小の素数を列挙する
  int n = N + 1;
  vector<int> prime(n, 0);
  int sqn = (int)sqrt(n);
  for (int i = 2; i <= sqn; ++i) {
    if (prime[i] > 0) continue;
    int k = i * i;
    while (k <= n) {
      if (prime[k] == 0) prime[k] = i;
      k += i;
    }
  }

  // Nまでの半素数を列挙する
  vector<int> semiPrime(n, 0);
  for (int i = 0; i < n; ++i) {
    if (prime[i] == 0) continue;  // 素数を約数に持たない→素数である
    // 約数の中で最小の素数で割る →
    // 割った先の値でもまだ約数を持つならば，その値は半素数ではない(素数2つの積ではない)
    if (prime[i / prime[i]] == 0) semiPrime[i] = 1;
  }

  // 半素数リストの累積和 → 任意の区間内の半素数の数をO(1)で計算できる
  vector<int> cumulative(n, 0);
  for (int i = 1; i < n; ++i) {
    cumulative[i] = cumulative[i - 1] + semiPrime[i];
  }

  // クエリ処理
  int pn = P.size();
  vector<int> ans(pn);
  for (int i = 0; i < pn; ++i) {
    ans[i] = cumulative[Q[i]] - cumulative[P[i]] + semiPrime[P[i]];
  }

  // for(int i = 0; i < prime.size(); ++i) cout << prime[i] << " "; cout <<
  // endl; for(int i = 0; i < semiPrime.size(); ++i) cout << semiPrime[i] << "
  // "; cout << endl; for(int i = 0; i < cumulative.size(); ++i) cout <<
  // cumulative[i] << " "; cout << endl;

  return ans;
}
