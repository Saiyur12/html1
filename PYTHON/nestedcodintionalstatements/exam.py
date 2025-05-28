
medical_cause=input("did you have a medical cause Y or N: ")
atten = int(input("enter the attendence of the student: "))


if medical_cause == 'Y': #checking the condition 1
  print ("you are allowed")
else:
 if atten>75:   #checking the conition 2
  
  print("Allowed")
 else:
  print("not allowed")