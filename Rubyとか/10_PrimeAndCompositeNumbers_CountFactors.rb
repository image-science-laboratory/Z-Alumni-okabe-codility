# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"
require "prime"
def solution(n)
  nf = n.to_f 
  sqn = Math.sqrt(n)
  cnt = 0
  1.upto(sqn) do |i|
    if nf % i == 0
      cnt += 1
      cnt += 1 if i != sqn 
    end
  end
  return cnt
end
