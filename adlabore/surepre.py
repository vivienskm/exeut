from abc import ABC, abstractmethod

class MyAbc(ABC):
    @abstractmethod
    def my_method(self):
        pass

class ConcreteClass(MyAbc):
    def my_method(self):
        print("This is the implementation of my_method.")

# You can't instantiate MyAbc directly because it contains abstract methods
# my_abc_instance = MyAbc()  # This will raise a TypeError

# You can instantiate ConcreteClass since it implements all abstract methods
concrete_instance = ConcreteClass()
concrete_instance.my_method()  # Output: This is the implementation of my_method.
