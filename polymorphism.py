#polymorphism - lets one write a code that interacts with objects based on
#what they can do rather than what exact class they belong to


class Animal:
    def make_sound(self):
        pass


class Dog:
     def make_sound(self):
         print("Woof! woof!")


class Cat(Animal):
    def make_sound(self):
        print("meow!! meow!!")


class Duck(Animal):
    def make_sound(self):
        print("Quack!! Quack!!")


def print_animal_sound:
    print(animal.make_sound())

print (animal.make_sound(Dog())
print_animal_sound(Cat())
print_animal_sound(Duck())

