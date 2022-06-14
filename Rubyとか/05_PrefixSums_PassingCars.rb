# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"

def solution(a)
    # write your code in Ruby 2.2
    ans =  0
    eastCnt = 0 
    a.length.times do |i|
      if a[i] == 0 
        eastCnt += 1 
      else 
        ans += eastCnt
      end
    end
    return ans <= 1000000000 ? ans : -1
end
  