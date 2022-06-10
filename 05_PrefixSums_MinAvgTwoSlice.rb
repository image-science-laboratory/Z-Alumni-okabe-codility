
def solution(a)
    # write your code in Ruby 2.2
    n = a.length 
    cumSum = Array.new(n + 1, 0)
    1.upto(n) do |i|
      cumSum[i] = cumSum[i - 1] + a[i - 1]
    end 
  
    #p cumSum
  
    minAve = 10 ** 10
    minInd = 1
    left = 0 
    right = 2
    while left < n - 1
      ave = (cumSum[right] - cumSum[left]) / (right - left).to_f
      if minAve > ave 
        minAve = ave 
        minInd = left 
        #print "update "
      end 
      
     # puts "left:#{left} right:#{right} ave:#{ave} min:#{minAve}"
  
      if  right == n || right - left > 2 && a[right] >= ave 
        left += 1 
      else
        right += 1
      end
      
    end
    return minInd
  end