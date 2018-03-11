#define even_number function & return statement
def even_number(start_point=0,end_point=1,step=1):
    even_number=[]
    for number in range(start_point,end_point,step):
        if number%2==0:
            even_number.append(number)
    return even_number

#--------------------------------------------------------
#define generate_even function & return statement
def generate_even():
    start_point=input("enter a start point: ")
    while not start_point.isdigit():
            start_point=input("please enter digit: ")
    end_point=input("enter an end point: ")
    while not end_point.isdigit():
            end_point=input("please enter digit: ")                  
    return(even_number(int(start_point),int(end_point)))

print(generate_even())
