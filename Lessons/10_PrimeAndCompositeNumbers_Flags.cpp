// you can use includes, for example:
// #include <algorithm>

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;
#include <cmath>

int solution(vector<int> &A) {
  // write your code in C++14 (g++ 6.2.0)
  vector<int> peaks;
  int n = A.size();

  for (int i = 1; i < n - 1; ++i) {
    if (A[i - 1] < A[i] && A[i] > A[i + 1]) peaks.emplace_back(i);
  }
  if (peaks.size() == 0) return 0;

  // for(int i=0; i < peaks.size(); ++i) cout << peaks[i] << " "; cout << endl;

  int max = 0;
  int sqn = (int)(sqrt(n) + 2);
  int pn = peaks.size();
  for (int i = 1; i < sqn; ++i) {
    int cnt = 1;
    int prev = 0;
    int current = 1;

    while (current < pn) {
      if (peaks[current] - peaks[prev] >= i) {
        cnt += 1;
        prev = current;
      }
      current += 1;
    }
    if (cnt >= i) max = i;
  }
  return max;
}
