##Create a class that uses encapsulation. Requirements include:
##
##    This class should make use of a private attribute or function. 
##
##    This class should make use of a protected attribute or function. 
##
##    Create an object that makes use of protected and private. 
##
##    Add comments throughout your Python explaining your code. 

class Animal:
    def __init__(self):
        #species is protected
        self._species = '' 

    #method private
    def __speciesSound(self, sound):
        print("This species makes a(n) {} sound".format(sound))


species = Animal()
species._species = "Dolphin"

print(species._species)

# I saw this is called 'mangling' and was not recommended.
# Is it common that people would use a protected property,
# and a private method like this? or do it differently?
species._Animal__speciesSound('oink')
