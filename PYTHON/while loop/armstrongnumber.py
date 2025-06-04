
#Take input from the user
num = int(input("Enter a 3 digit number: "))
 

# Initilaise
sum = 0


# Find the sum of the cube of each digit
temp = num
while temp > 0 :
   digit = temp % 10
   sum += digit ** 3
   temp //=100


# Display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an  Armstrong number")