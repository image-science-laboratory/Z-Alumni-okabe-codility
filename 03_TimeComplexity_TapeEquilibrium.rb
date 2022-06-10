# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"

def solution(a)
    # write your code in Ruby 2.2
    left = a[0]
    right = a.inject(:+) - a[0]
    min = (left - right).abs
    1.upto(a.length - 2) do |i|
      left += a[i]
      right -= a[i]
      diff = (left - right).abs 
      min = diff if min > diff
    end
    return min
end
  