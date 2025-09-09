# Create class
class Vehicle:


        # Create init method
    def __init__(self, max_speed, milage):


        self.max_speed = max_speed
        self.milage = milage

# Objects creation
modelX = Vehicle(240, 18) 


# Access the variables inside init method
print("Model max speed:",modelX.max_speed)
print("Model Milage:", modelX.milage)