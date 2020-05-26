import pdb
from Debugging.functions import addition, subtraction
def fun():
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
print (fun())
addition()
subtraction()

