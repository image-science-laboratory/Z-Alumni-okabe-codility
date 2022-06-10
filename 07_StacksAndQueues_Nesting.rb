# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"

def solution(s)
  # write your code in Ruby 2.2
  cnt = 0 
  s.chars.each do |c|
    if c == "("
      cnt += 1
    else 
      return 0 if cnt == 0
      cnt -= 1 
    end
  end
  return cnt == 0 ? 1 : 0
end
