#Input an integer value
n = int(input("Enter the number you want to find:"))
sum = 0

#Iterates for n+1 timess: i=1 to n+1
for i in range(1, n+1):
   sum = sum+i
   print("\nSum =", sum) 
