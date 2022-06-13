n = 100000
fibo = {}
fibo[1] = true
fibo[2] = true 
p1 = 1
p2 = 2
p3 = p1 + p2 
while p3 < n 
  fibo[p3] = true
  p1 = p2 
  p2 = p3 
  p3 = p1 + p2 
end
puts fibo.length
p fibo