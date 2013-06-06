import math
def fibo(n): 
    x=0
    y=1
    while True: 
      print x
      print y  
      x=x+y
      y=y+x
      if y>=n:
        break
fibo(14) 
