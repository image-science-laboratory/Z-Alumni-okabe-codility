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
    gcd = GCD(aa, bb)

    # gcdで割り続けると良い感じ
    # [2,2,3] と [2,3,3]だと6で割って[2],[3]
    # → [2], [3] と 6のgcdで割ると[1], [1]

    # [2,2,3] と [2,3,3,5]だと 6でわって[2], [3,5]
    # → [2], [3, 5] と 6のgcdで割ると[1], [5]
    # → 6 と [5]のgcdで割っても5 

    # 初期のGCDと更新した空間で割り続ければ初期のGCDに含まれないやーつが出るはず
    prev = -1
    while aa != prev 
      prev = aa
      aa = aa / GCD(aa, gcd)
    end 

    prev = -1
    while bb != prev 
      prev = bb 
      bb = bb / GCD(bb, gcd)
    end 

    #puts "gcd:#{gcd} aa:#{aa} bb:#{bb}"
    ans += 1 if aa * bb == 1
  end
  return ans
end
