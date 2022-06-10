# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"

def solution(a)
    # write your code in Ruby 2.2
    hash = Hash.new(0)
  
    a.each do |aa|
      hash[aa] += 1
      return 0 if hash[aa] > 1 
    end
  
    1.upto(a.length) do |i|
      return 0 if hash.has_key?(i) == false
    end
  
    return 1
  
end
  