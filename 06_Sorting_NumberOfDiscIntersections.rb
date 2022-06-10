# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"

def solution(a)
  # write your code in Ruby 2.2
  n = a.length 
  lrList = Array.new(n * 2)

  #true→left  false→right
  n.times do |i|
    lrList[i * 2] = i - a[i]
    lrList[i * 2 + 1] = i + a[i] + 0.5
  end
  
  lrList.sort!
	#p lrList

  ans = 0 
  cnt = 0
  lrList.length.times do |i|
    x = lrList[i]
    if x % 1 == 0
      ans += cnt 
      cnt += 1
    else 
      cnt -= 1
    end
    
    #puts "i:#{i} cnt:#{cnt} ans:#{ans}"
  end
  
  return ans > 10000000 ? -1 : ans 
end
