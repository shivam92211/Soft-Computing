x = float(input("input x:" ))
w = float(input("weight:" ))
b = float(input("bias:" ))

y = x*w + b
print (y)

if(y<0):
  out = 0
elif(y>=0)&(y<=1):
  out = y
else:
  out = 1

print("output:",out)