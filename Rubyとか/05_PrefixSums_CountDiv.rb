# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"

def solution(a, b, k)
    # write your code in Ruby 2.2
    kf = k.to_f 
    return ((b / kf).floor * k - (a / kf).ceil * k) / k + 1
    
end
  