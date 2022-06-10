# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"

def solution(a)
    # write your code in Ruby 2.2
    hash = {}
    a.each do |aa|
      hash[aa] = true 
    end 
    return hash.keys.length
end
  