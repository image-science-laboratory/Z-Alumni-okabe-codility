# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"


def solution(a, b)
    # write your code in Ruby 2.2
    fibo = Array.new(50001)
    fibo[0] = 1
    fibo[1] = 1
    2.upto(fibo.length - 1) do |i|
      fibo[i] = fibo[i - 1] + fibo[i - 2]
    end
  
    # n段の梯子で頂点に到達するパターン数はフィボナッチ数列の(n + 1)項目に同じ
    # n段目に到達するパターンは(n - 1)段目と(n - 2)段目の和
    # (n - 1)段目に到達するパターン数から +1段するとn
    # (n - 2)段目に到達するパターン数から +2段するとn
    n = a.length 
    ans = Array.new(n)
    n.times do |i|
      aa = a[i]; bb = b[i]
      f = fibo[aa]
      ans[i] = f % (2 ** bb)
    end
    return ans
  end