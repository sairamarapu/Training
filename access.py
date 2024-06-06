class Student:
    def _init_(self,name,roll_number,password):
        self.name=name
        self._roll_number=roll_number
        self.__password=password
    def display_details(self):
        print("Name:",self.name)
        print("Roll number:",self._roll_number)
        print("Password:",self.__password)

    def get_password(self):
        return self.__password
    
    def set_password(self,new_password):
        self.__password=new_password

student=Student("OM","Aoo1","OM12345")

print("Name (Public):",student.name)

print("Roll Number(Protected):",student._roll_number)

print("Password (Private):",student.get_password())

print("Password (Private):",student.set_password("om123"))
student.display_details()   