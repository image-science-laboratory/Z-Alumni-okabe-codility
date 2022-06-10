# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"

def solution(a)
    # write your code in Ruby 2.2
    hash = {}
    a.each do |aa|
      hash[aa] = true 
    end 
  
    1.upto(10 ** 10) do |i|
      if hash.has_key?(i) == false 
        return i  
      end 
    end
  end
  