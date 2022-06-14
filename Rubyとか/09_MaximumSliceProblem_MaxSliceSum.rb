# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"

def solution(a)
  # write your code in Ruby 2.2
  n = a.length
  max = -1 * (10 ** 10)
  current = 0
  left = 0 
  right = 0
  while right < n
    current += a[right]
    max = current if max < current
    #puts "left:#{left} right:#{right} current:#{current} max:#{max}"
    if current < 0 
      current = 0
      right += 1
      left = right 
      next 
    end 
    right += 1
  end
  return max
end
