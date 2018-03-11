#def functionname(start point, end point) - positional
#def functionname (star=0, end=0) - keyword - use keyword to set default

#--------------------------------------------------------
#define functions & return statement
def even_number(start_point=0,end_point=20,step=5):
    even_number=[]
    for number in range(start_point,end_point,step):
        if number%2==0:
            even_number.append(number)
    return even_number

#--------------------------------------------------------
#call function
print("*****\n",even_number(2),"\n******")


#--------------------------------------------------------

           
            
