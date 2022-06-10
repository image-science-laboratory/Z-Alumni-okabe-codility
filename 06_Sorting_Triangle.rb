# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"

def solution(a)
  # write your code in Ruby 2.2
  arr = a.sort
  n = arr.length 
  2.upto(n - 1) do |i|
    return 1 if arr[i - 2] + arr[i - 1] > arr[i]
  end
  return 0
end