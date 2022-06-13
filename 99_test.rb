def fibo(n)
  sq5 = Math.sqrt(5)
  a = ((1 + sq5) / 2) ** n 
  b = ((1 - sq5) / 2) ** n 
  return ((a - b) / sq5).round
end


20.times do |i|
  puts "i:#{i} figo:#{fibo(i )}"
end