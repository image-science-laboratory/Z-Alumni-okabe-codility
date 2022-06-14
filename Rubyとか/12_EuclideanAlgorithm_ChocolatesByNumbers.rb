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


def solution(n, m)
  # write your code in Ruby 2.2
  return n / GCD(n, m)
end
