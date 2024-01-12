import math

def sigmoid(x):
  return 1/1+math.exp(-x)

n = int(input("enter the no of element:"))

print("your inputs", n)

inp = []

for i in range(0,n):
  ele = float(input("enter x values: "))
  inp.append(ele)

print(inp)

weight = []

for i in range(0,n):
  ele = float(input("enter weight values: "))
  weight.append(ele)

print(weight)

y = []

for i in range(0,n):
  yin = inp[i]*weight[i]
  y.append(yin)

z = round(sum(y))

print(round(sum(y)))



print(sigmoid(z))