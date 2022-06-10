# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"

def solution(a, b)
  # write your code in Ruby 2.2
  stack = []
  cnt = 0 

  n = a.length 
  n.times do |i|
    #p stack
    if b[i] == 1
      stack << a[i]
    else 
      while stack.length > 0 
        last = stack[-1]
        # でかいのに出会うと食われる 
        if last > a[i]
          cnt += 1
          break 
        end 
        # 小さいやつは食べる
        stack.pop 
        cnt += 1
      end 
    end
  end
  return n - cnt
end










