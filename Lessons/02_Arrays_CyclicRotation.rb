# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"

def solution(a, k)
    # write your code in Ruby 2.2
    n = a.length 
    ans = Array.new(n)
    n.times do |i|
      ans[(i + k) % n] = a[i]
    end 
    return ans
end
  