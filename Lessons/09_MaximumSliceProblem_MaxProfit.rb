# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"

def solution(a)
  # write your code in Ruby 2.2
  n = a.length 
  min = a[0]
  maxDiff = -1 * (10 ** 10)

  1.upto(n - 1) do |i|
    min = a[i] if min > a[i]
    diff = a[i] - min  
    maxDiff = diff if maxDiff < diff 
  end
  return [maxDiff, 0].max
end
