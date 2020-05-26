import pdb
def addition():
    first_number=int(input("enter the first number:-"))
    print (type(first_number))
    second_number=str(input("enter the second number:-"))
    print (type(second_number))
    pdb.set_trace()
    add=((first_number)+int(second_number))
    print ("The addition of both first and second is:-",add)


def subtraction():
    third_number=int(input("enter the third number:-"))
    print (type(third_number))
    fourth_number=str(input("enter the fourth number:-"))
    print (type(fourth_number))
    pdb.set_trace()
    sub=((third_number)-int(fourth_number))
    print ("The addition of both third and fourth is:-",sub)