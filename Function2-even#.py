#def functionname(start point, end point) - positional
#def functionname (star=0, end=0) - keyword - use keyword to set default

#--------------------------------------------------------
#define even_number function & return statement
def even_number(start_point=0,end_point=1,step=1):
    even_number=[]
    for number in range(start_point,end_point,step):
        if number%2==0:
            even_number.append(number)
    return even_number

#--------------------------------------------------------
#define generate_number function & return statement
def generate_number():
    start_point=input("enter a start point: ")
    while not start_point.isdigit():
            start_point=input("please enter digit: ")
    end_point=input("enter an end point: ")
    while not end_point.isdigit():
            end_point=input("please enter digit: ")                  
    
    return(even_number(int(start_point),int(end_point)))

#-------------------------------------------------
#call function
listt=generate_number()

#--------------------------------------------------------

def list_sum_product():
    summ=0
    for number in listt:
        summ+=number
    product=summ*len(listt)
    return product
print("\n\n",list_sum_product())
#-------------------------------------------------------
def returnmany():
     return('james', 'surname', '25', 'result')

output=returnmany()
print(output)

    
    
