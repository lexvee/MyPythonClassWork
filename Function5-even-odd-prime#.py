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

#--------------------------------------------------------
#define odd_number function & return statement
def odd_number(start_point=0,end_point=1,step=1):
    odd_number=[]
    for number in range(start_point,end_point,step):
        exclude=[0]
        if number%2!=0 and number not in exclude:
            odd_number.append(number)
    return odd_number

#---------------------------------------------------------
#define generate_odd function & return statement
def generate_odd():
    start_point=input("enter a start point: ")
    while not start_point.isdigit():
            start_point=input("please enter digit: ")
    end_point=input("enter an end point: ")
    while not end_point.isdigit():
            end_point=input("please enter digit: ")                  
    return(odd_number(int(start_point),int(end_point)))

#---------------------------------------------------------
#define odd_number function & return statement
def prime_number(start_point=0,end_point=1,step=1):
    prime_number=[]
    for number in range(start_point,end_point,step):
        if number%2!=0 and number%3!=0 and number%5!=0 and number%7!=0 and number%9!=0 or number==3 or number==5 or number==7:
            prime_number.append(number)
    return prime_number

#---------------------------------------------------------
#define generate_prime function & return statement
def generate_prime():
    start_point=input("enter a start point: ")
    while not start_point.isdigit():
            start_point=input("please enter digit: ")
    end_point=input("enter an end point: ")
    while not end_point.isdigit():
            end_point=input("please enter digit: ")
            
    return(prime_number(int(start_point),int(end_point)))
           
#---------------------------------------------------------
print("\nEVEN NUMBERS\n*****\n",generate_even())
print("\nODD NUMBERS\n*****\n",generate_odd())
print("\nPRIME NUMBERS\n*****\n",generate_prime())

