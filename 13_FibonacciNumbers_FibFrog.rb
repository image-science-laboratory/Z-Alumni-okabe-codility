# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"

def solution(a)
    # write your code in Ruby 2.2
    n = a.length
    fibo = []
    fibo << 1 
    fibo << 2
    while fibo[-1] + fibo[-2] <= n 
      fibo << fibo[-1] + fibo[-2]
    end
  
    big = 10 ** 10
    leaf = [1]
    leaf << a 
    leaf << [1]
    leaf.flatten!
    n = leaf.length
    arr = Array.new(n, big)
    arr[0] = 0
    0.upto(n - 1) do |i|
      next if arr[i] == big
      fibo.each do |f|
        dist = i + f 
        next if dist >= n || leaf[dist] == 0
        arr[dist] = arr[i] + 1 if arr[dist] > arr[i] + 1
      end
    end
    
    return arr[-1]
  end
  