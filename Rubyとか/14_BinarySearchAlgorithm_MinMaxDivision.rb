# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"


def BinarySearch(arr, k)
  # Mの範囲で二分探索
	left = 0 
	right = 10 ** 12 #条件内の最大和 log2(10**12)≒33 なのでNlogNなら間に合う

  # 探索済みについて(最終的に振動するのでその判定)
  hash = {}

	while left <= right 
		mid = (left + right) / 2 
		if check(arr, k, mid)
      return mid if hash.has_key?(mid)
      hash[mid] = true 
      right = mid - 1
    else
			left = mid + 1
		end
    #puts "left:#{left} right:#{right} mid:#{mid} check:#{check(arr, k, mid)}"
	end
  
  return hash.keys.min
end

# arrをk分割する際に各ブロックの和をs以下にできるか
def check(arr, k, s)
  return false if arr.max > s 

  sum = 0
  cnt = 0 
  ind = 0 
  while ind < arr.length 
    sum += arr[ind]
    if sum > s 
      sum = 0
      cnt += 1
      next 
    end
    ind += 1
  end
  return cnt < k 
end

def solution(k, m, a)
  # write your code in Ruby 2.2
 
  return BinarySearch(a, k)
  # p check(a, k, 5)
  # return -1
end
