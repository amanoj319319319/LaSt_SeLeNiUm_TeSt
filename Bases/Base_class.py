'''
from Bases.Commond_class import *
from Utiities.Utility_class import *
class Base(Commond,Utility):
    def method_B1(self,b1,b2,b3,x,y,a,b,name):
        b=(b1+b2+b3)
        print ("value of b is:-", b)
        self.method_D1(a,b)
        self.method_C1(x, y)
        self.method_U1(name)
b=Base()
b.method_B1(10000,20000,30000,100,200,1,2,"manoj")

'''


from Bases.Commond_class import Commond
class Basepage(Commond):
    def method1(self):
        c=Commond()
        c.method_C1(500,200)#First way of calling Commond class methods
        self.method_C1(500,200)#second way of calling Commond class methods
b=Basepage()
b.method1()
b.method_C1(500,200)#third way of calling Commond class methods



