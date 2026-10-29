#parent class/super class/base class
class Animal:
    Ismammal = True
    age = 3

    def movement(self):
        print("Animal is moving")


#child class/sub class/derived class
class Dog(Animal):
    def bark(self):
        print("woof!! woof!! woof!!")



class cat(Animal):
    def meow(self):
        print("meow!! meow!! meow!!")


dog1 = Dog()
dog1.movement()
print("dog1.age")

cat1 = cat()
cat1.meow()

