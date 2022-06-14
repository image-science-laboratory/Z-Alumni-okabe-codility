# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"

def solution(a)
    # write your code in Ruby 2.2
    hash = Hash.new(0)
    a.each do |aa|
      hash[aa] += 1
    end
  
    half = a.length / 2
    hash.each_key do |key|
      if hash[key] > half 
        f = a.index{|aa| aa == key}
        #puts "hash:#{hash[key]} key:#{key} find:#{f}"
        return a.index{|aa| aa == key}
      end  
    end
    return -1
end
  