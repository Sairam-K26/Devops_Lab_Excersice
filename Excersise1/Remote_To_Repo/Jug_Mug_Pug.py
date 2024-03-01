n=int(input())
if n%3==0 or str(3) in str(n):
  print("Jugs")
elif n%5==0 or str(5) in str(n):
  print("Mugs")
elif n%7==0 or str(7) in str(n):
  print("Pugs")
else:
  print(n)
