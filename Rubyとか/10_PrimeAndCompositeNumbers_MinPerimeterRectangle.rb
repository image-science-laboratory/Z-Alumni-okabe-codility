# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"

def solution(n)
  # write your code in Ruby 2.2
 
  sqn = Math.sqrt(n)
  divisor = []
  1.upto(sqn) do |i|
    if n % i == 0
      divisor << i 
    end
  end
  
  min = 10 ** 10 
  divisor.each do |d|
    len = 2 * (d + n / d) 
    min = len if min > len 
  end
  return min
end
