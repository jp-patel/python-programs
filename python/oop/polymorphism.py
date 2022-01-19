# how to use polymorphism in python

class Parrot:

    def fly(self):
        print("Parrot can fly")
        print()
    
    def swim(self):
        print("Parrot can't swim")
        print()

class Penguin:

    def fly(self):
        print("Penguin can't fly")
        print()
    
    def swim(self):
        print("Penguin can swim")
        print()

# common interface
def flying_test(bird):
    bird.fly()

#instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
flying_test(blu)
flying_test(peggy)
