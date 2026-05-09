from abc import ABC, abstractmethod
class absclass (ABC):
    def print (self,x):
        print("Passed value: ", x)
    @abstractmethod
    def task(self):
        print("We are inside absclass task")
class testclass(absclass):
    def task(self):
        print("We are inside testclass task")
test_obj = testclass()
test_obj.task()
test_obj.print(100)