class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"hi {self.name}")
per=Person("sai",34)
per.display()

