#class constructor __init__(method)
class abc():
    def __init__(self,val):
        print("this is a class method")
        self.val=val
        print("the value is",val)
obj=abc(10)
