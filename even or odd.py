class number():
    even=0
    def check(self,num):
        if num%2==0:
            self.even=1
    def eo(self,num):
        self.check(num)
        if self.even==1:
            print(num,"is even")
        else:
            print(num,"is odd")
n=number()
n.eo(32)



#segregate the even and odd parameters in a list and print even list and odd list seperately using class number
#n1=number(10)
#n2=number(32)
#n3=number(57)
#n4=number(31)
#n5=number(45)
#n6=number(67)
#output:even num:[10,32]
#odd num:[57,31,45,67]
class number:
    even_list=[]
    odd_list=[]
    def __init__(self,val):
        self.val=val
        if val%2==0:
            number.even_list.append(val)
        else:
            number.odd_list.append(val)
n1=number(10)
n2=number(32)
n3=number(57)
n4=number(31)
n5=number(45)
n6=number(67)
print(f"Even numbers: {number.even_list}")
print(f"odd numbers:{number.odd_list}")
