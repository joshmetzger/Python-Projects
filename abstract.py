##Create a class that utilizes the concept of abstraction.
##
##    Your class should contain at least one abstract method and one regular method.  
##
##    Create a child class that defines the implementation of its parents abstract method. 
##
##    Create an object that utilizes both the parent and child methods. 

 
from abc import ABC, abstractmethod
#initial parent class
class food(ABC):
    def expiration(self, expDate):
        print("This food expires on: ", expDate)
        # def ine abstract method
        @abstractmethod
        def exp(self, expDate):
            pass

# child class
class foodExpire(food):
    def exp(self, expDate):
        print("This food has an expiration date of {}, at the current date of 5/30/2027".format(expDate))

#create object, call method, abstract method
junt = foodExpire()
junt.expiration("3/23/2002")
junt.exp("4/11/2045")
