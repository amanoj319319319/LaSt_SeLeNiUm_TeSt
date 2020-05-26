import pdb
from Debugging.functions_1 import abc
class xyz(object):
    def __init__(self):
        pass
    def fun(self):
        pdb.set_trace()
        first_name=input("Enter your first name:-")
        last_name=input("Enter your last name:-")
        full_name=(first_name+last_name)
        print ("Full name is:-",full_name)
        print ("*********************")
        college_name=(input("Enter your college name:-"))
        college_code=input("Enter your college code:")
        combine=(college_name)+str(college_code)
        pdb.set_trace()
        return combine

    def method_calling(self):
        a = abc()
        a.addition()
        a.subtraction()

x=xyz()
x.fun()
x.method_calling()