def MyFunc(a, b):
  return a ** b

print(MyFunc(100, 2))

sum = 0
for i in range(10):
  sum += MyFunc(10, i)
print(sum)


