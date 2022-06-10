# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"

# 全てがピークだと仮定しても，フラッグの最大数は√nになる(√nが最大)
# → N√N で多分間に合う

def solution(a)
  # write your code in Ruby 2.2
  peaks = [] # index of peak
  n = a.length 

  1.upto(n - 2) do |i|
    peaks << i if a[i - 1] < a[i] && a[i] > a[i + 1]
  end
  return 0 if peaks.length == 0

  max = 0 
  sqn = Math.sqrt(n).to_i + 2
  pn = peaks.length
  # peaks
  1.upto(sqn) do |i|
    cnt = 1
    prev = 0 
    current = 1 

    while current < pn 
      #puts "current:#{current} pc:#{peaks[current]} prev:#{prev} pp:#{peaks[prev]}"
      if peaks[current] - peaks[prev] >= i 
        cnt += 1 
        prev = current 
      end 
      current += 1
    end
    max = i if cnt >= i 
    # "i:#{i} cnt:#{cnt}"
  end
  return max
end
