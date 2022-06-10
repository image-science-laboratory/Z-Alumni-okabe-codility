# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"

def solution(a)
  # write your code in Ruby 2.2
  n = a.length
  leftSum = Array.new(n, 0)
  rightSum = Array.new(n, 0)

  1.upto(n - 1) do |i| 
    tmp = leftSum[i - 1] + a[i]
    leftSum[i] = tmp > 0 ? tmp : 0
  end

  (n - 2).downto(0) do |i|
    tmp = rightSum[i + 1] + a[i]
    rightSum[i] = tmp > 0 ? tmp : 0 
  end

  max = 0 
  1.upto(n - 2) do |i|
    sum = leftSum[i - 1] + rightSum[i + 1]
    max = sum if max < sum 
  end
  return max
end
