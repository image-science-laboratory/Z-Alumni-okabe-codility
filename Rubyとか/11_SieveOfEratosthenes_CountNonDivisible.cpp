// you can use includes, for example:
// #include <algorithm>

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;
#include <algorithm>
#include <cmath>
#include <iostream>
#include <unordered_map>
#include <vector>
vector<int> solution(vector<int> &A) {
  // write your code in C++14 (g++ 6.2.0)
  int n = A.size();

  // 各要素の出現回数を検索
  std::unordered_map<int, int> hash;
  for (int i = 0; i < n; ++i) {
    if (hash.find(A[i]) != hash.end())
      hash[A[i]] += 1;
    else
      hash[A[i]] = 1;
  }

  // // 確認
  // for(auto itr = hash.begin(); itr != hash.end(); itr++){
  //     cout <<itr->first <<" " <<itr->second << endl;
  // }

  // 倍数を足していく
  vector<int> erathos(2 * n + 2, 0);
  int esize = erathos.size();
  for (auto itr = hash.begin(); itr != hash.end(); itr++) {
    int a = itr->first;
    int cnt = itr->second;
    while (a < esize) {
      erathos[a] += cnt;
      a += itr->first;
    }
  }

  // for(int i = 0; i < esize; ++i){
  //     cout <<erathos[i] << " ";
  // }cout << endl;

  vector<int> ans(n);
  for (int i = 0; i < n; ++i) {
    ans[i] = n - erathos[A[i]];
  }

  return ans;
}
