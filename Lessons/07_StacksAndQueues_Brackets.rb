# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"

def solution(s)
  # write your code in Ruby 2.2
  stack = []
  hash = {}
  hash["("] = 0 
  hash["{"] = 1
  hash["["] = 2
  hash[")"] = 3 
  hash["}"] = 4
  hash["]"] = 5

  last = ""
  s.chars.each do |c|
    if hash[c] < 3
      last = c 
      stack << c  
    else 
      if hash[last] != hash[c] - 3 
        return 0 
      end 
      stack.pop
      last = stack[-1]
    end
  end
  return stack.length == 0 ? 1 : 0
end
