# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"

def solution(n, a)
    # write your code in Ruby 2.2
    counter = Array.new(n, 0)
    prev = false
    max = 0
    a.each do |aa|
      if aa <= n  
        aa -= 1
        counter[aa] += 1 
        max = counter[aa] if max < counter[aa]
        prev = false
      elsif prev == false 
        counter = Array.new(n, max)
        prev = true
      end
    end
    return counter
end
  