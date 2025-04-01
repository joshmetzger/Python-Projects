# parent class
class Pet:
    indoor_outdoor = ""
    warm_blood = True
    weight = 0
    legs = 4
    sound = None

    def pet_info(self):
        print("This is the outline parent pet class info")

    def make_sound(self):
        print("A pet will sound like...")

# child class
class Dog(Pet):
    species = "dog"
    name = ""
    breed = None
    sound = "Woof"
    

    def __init__(self, name, legs, breed, weight):
        self.name = name
        self.legs = legs
        self.breed = breed
        self.weight = weight

    def dog_info(self):
        print("This dog's name is {}".format(self.name))

    #polymorphic method inherited from parent
    def make_sound(self):
        print("This pet will sound like {}".format(self.sound))



# child class
class Cat(Pet):
    species = "cat"
    name = ""
    breed = None
    sound = "Meow"
    

    def __init__(self, name, legs, breed, weight):
        self.name = name
        self.legs = legs
        self.breed = breed
        self.weight = weight

    def cat_info(self):
        print("This cat's name is {}".format(self.name))

    #polymorphic method inherited from parent
    def make_sound(self):
        print("This pet will sound like {}".format(self.sound))






if __name__ == "__main__":

    # instantiate child class
    my_dog = Dog("Steven", 4, "Husky", 60)
    my_dog.dog_info()
    ##    print inherted behaviour from parent class
    my_dog.make_sound()


    # instantiate child class
    my_cat = Cat("Marcus", 4, "Orange", 3)
    my_cat.cat_info()
    ##    print inherted behaviour from parent class
    my_cat.make_sound()
