#initiate a class 
class employee:
   # special methods/magic method/ dunder method - constructor 
    def __init__(self): 
       print(id(self))
       print("Started executing attributes/data ")
       self.id = 123
       self.salary = 50000
       self.designation  = "SDE"
       print("attributes/data have been initiated")


    def travel(self, destination):
        print("This travel medthod was called manually")
        print(f"Employee is now travelling to {destination}")
        

    

# create an obj/instance of the class
sam = employee()
sam.name  = 'Mohit rajput'
print(sam.name)

print(id(sam))

sam.travel("kerela")

print(type(sam))