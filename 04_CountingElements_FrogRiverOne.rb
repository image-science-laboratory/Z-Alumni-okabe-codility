# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"

def solution(x, a)
    # write your code in Ruby 2.2
    hash = {} 
    cnt = 0
    a.length.times do |i|
      cnt += 1 if hash.has_key?(a[i]) == false 
      return i if cnt == x 
      hash[a[i]] = true 
    end
    return -1
end
  