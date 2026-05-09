from abc import ABC, abstractmethod
class animal(ABC):
    def move(self):
        pass
class Human(animal):
    def move(self):
        print("I can walk and run")
class snake(animal):
    def move(self):
        print("I can crawl")
class dog(animal):
    def move(self):
        print("I can bark")
class lion(animal):
    def move(self):
        print("I can roar")
R = Human()
R.move()
K = snake()
K.move()
R = dog()
R.move()
K = lion()
K.move()