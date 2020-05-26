'''
def fun():
    first_name=input("Enter your first name:-")
    last_name=input("Enter your last name:-")
    full_name=(first_name+last_name)
    print ("Full name is:-",full_name)
    print ("*********************")
    college_name=(input("Enter your college name:-"))
    college_code=input("Enter your college code:")
    combine=(college_name)+str(college_code)
    return combine
print (fun())
'''


#when we get errors at the moment of execution with out setting any breakpoints , first set the code (str) and then press s ,
#when we get errors at the momemt of exeution after setting the breakpoints , first set the code(str) and then press c and then ,
#press s and then follow your process asusual .

#https://www.youtube.com/watch?v=38n9STvQsO0
#https://www.youtube.com/watch?v=ChuU3NlYRLQ
#https://www.youtube.com/watch?v=ChuU3NlYRLQ
#youtube.com/watch?v=jOPOFCl6AFU
'''
import pdb
print (dir(pdb))
#pdb.set_trace()
first_name=input("Enter your first name:-")
last_name=input("Enter your last name:-")
full_name=(first_name+last_name)
print ("Full name is:-",full_name)
print ("*********************")
pdb.set_trace()
college_name=input("Enter your college name:-")
college_code=input("Enter your college code:")
combine=college_name+int(college_code)

print ("Combine is :-",combine)
'''



