# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"

def solution(a)
    # write your code in Ruby 2.2
    # n + 1 以下のフィボナッチ数列を列挙
    # n + 1 がフィボナッチ数列に含まれているならば回数1で到達できる
    n = a.length
    fibo = []
    fibo << 1 
    fibo << 2
    while fibo[-1] + fibo[-2] <= n + 1
      fibo << fibo[-1] + fibo[-2]
    end
  
    big = 10 ** 10
    leaf = [1]
    leaf << a 
    leaf << [1]
    leaf.flatten! # [1, a1, a2, ... , an-1, an, 1] の形(両岸を1にする)
    n = leaf.length
    arr = Array.new(n, big) # 距離iに到達できる最小回数を記録
    arr[0] = 0
    0.upto(n - 1) do |i|
      next if arr[i] == big
      fibo.each do |f|
        dist = i + f
        #p dist
        next if dist >= n || leaf[dist] == 0
        arr[dist] = arr[i] + 1 if arr[dist] > arr[i] + 1
      end
    end
    
    # p n
    # p fibo 
    # p leaf
    # p arr
    return arr[-1] != big ? arr[-1] : -1
  end
  