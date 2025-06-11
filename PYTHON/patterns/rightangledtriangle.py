
#Take input
print("Half pryamind Patter of Stars (*)):")
n = int(input("Enter the number of rows: "))
#Outer loop to handle numbers of rows
for i in range(n):
  #Inner loop to handle number of columns
       for j in range(i+1):
       #Display result 
         print("* ", end="")
       print()