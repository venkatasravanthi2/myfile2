num=int(input())
factorial = 1
if num < 0:
   print(num)
elif num == 0:
   print(num)
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print(factorial)
