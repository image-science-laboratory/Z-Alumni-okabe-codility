# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"

def solution(a)
    # write your code in Ruby 2.2
    hash = Hash.new(0)
    a.each do |aa|
      hash[aa] += 1
    end 
  
    hash.keys.each do |key|
      if hash[key] % 2 == 1 
        return key 
      end 
    end
  end
  