# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"

def solution(n)
    # write your code in Ruby 2.2
    s = n.to_s(2) 
    i = 0 
    while s[i] == "0" do i += 1 end  
  
    cnt = 0 
    max = 0 
    while i < s.length 
      if s[i] == "1"
        max = cnt if max < cnt 
        cnt = -1
      end 
      cnt += 1 
      i += 1
    end
    return max
end