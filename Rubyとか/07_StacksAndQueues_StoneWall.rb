# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"

def solution(h)
  # write your code in Ruby 2.2
  cnt = 1
  n = h.length 
  stack = [h[0]]
  prev_h = h[0]
  1.upto(n - 1) do |i|
    #p stack 
    # puts "current:#{prev_h} cnt:#{cnt}"
    next if prev_h == h[i]
    prev_h = h[i]

    if prev_h < h[i]
      stack << h[i]
      cnt += 1
    else
      while stack.length > 0 && stack[-1] > h[i]
        stack.pop 
      end 
      next if stack[-1] == h[i]

      cnt += 1
      stack << h[i]  
    end
  end
  return cnt 
end