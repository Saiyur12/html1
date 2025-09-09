#Class creation
class myClass:


    #private variable
    __priavteVar = 27;


    #priavte method
    def __privMeth(self):
        print("I'm inside class myClass")


    #Function to print value of priavte variable    
    def hello(self):
        print("Private Variable value: ",myClass.__privateVar )

#Object creation and method call
foo = myClass()        
foo.hello()
foo.__privMeth