n=int(input())
factorial = 1
if n< 0:
   print(n)
elif n == 0:
   print(n)
else:
   for i in range(1,n + 1):
       factorial = factorial*i
   print(factorial)
