#class members using class variables
class abc():
    var=100
    def display(self):
        print("this is class method")
obj=abc()
print(obj.var)
obj.display()
