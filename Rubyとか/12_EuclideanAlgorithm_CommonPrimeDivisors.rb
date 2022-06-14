# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"

# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"


def GCD(m, n)
	return 0 if m == 0 || n == 0
	while m != 0 && n != 0
		if m > n then
			m %= n
		else
			n %= m
		end
	end
	return [m, n].max
end

def LCM(m, n)
	return 0 if m == 0 || n == 0
	return m * n / GCD(m, n)
end


def solution(a, b)
  # write your code in Ruby 2.2
  ans = 0
  a.length.times do |i|
    aa = a[i]; bb = b[i]
    lcm = LCM(aa, bb)
    adiv = lcm / aa
    bdiv = lcm / bb
    abdiv = adiv * bdiv 
    ans += 1 if aa % abdiv == 0 && bb % abdiv == 0 
  end
  return ans
end
