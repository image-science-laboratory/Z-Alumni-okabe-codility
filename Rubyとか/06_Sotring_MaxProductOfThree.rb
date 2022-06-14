# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"

def solution(a)
  # write your code in Ruby 2.2
  posi = a.select{|aa| aa > 0}.sort
  nega = a.select{|aa| aa < 0}.sort
  zero = a.select{|aa| aa == 0}

  posiSmall = []
  3.times do 
    posiSmall << posi[0] if posi.length > 0 
    posi.shift  
  end 
  
  posiBig = [] 
  posi.reverse!
  3.times do 
    posiBig << posi[0] if posi.length > 0   
    posi.shift
  end 

  negaSmall = []
  3.times do 
    negaSmall << nega[0] if nega.length > 0 
    nega.shift  
  end 

  negaBig = [] 
  nega.reverse!
  3.times do 
    negaBig << nega[0] if nega.length > 0 
    nega.shift  
  end 

  zeros = []
  3.times do 
    zeros << 0 if zero.length > 0
    zero.shift 
  end  
  
  ngo = []
  ngo << posiSmall
  ngo << posiBig
  ngo << negaSmall
  ngo << negaBig
  ngo << zeros 
  ngo.flatten!
  
  max = -Float::INFINITY
  ngo.combination(3) do |bits|
    seki = bits.inject(:*)
    max = seki if max < seki 
  end
  return max
end
