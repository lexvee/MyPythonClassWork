#define even_number function & return statement
def even_number(start_point=0,end_point=1,step=1):
    even_number=[]
    for number in range(start_point,end_point,step):
        if number%2==0:
            even_number.append(number)
    return even_number

#--------------------------------------------------------
def inputstart():
    start_point=input("enter a start point: ")
    while not start_point.isdigit():
            start_point=input("please enter digit: ")
    return(int(start_point))

#-------------------------------------------------------
def inputend():
    end_point=input("enter an end point: ")
    while not end_point.isdigit():
            end_point=input("please enter digit: ")
    return(int(end_point))
#--------------------------------------------------------

#define generate_even function & return statement
def generate_even():
                     
    return(even_number(int(inputstart()),int(inputend())))
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
    return(odd_number(int(inputstart()),int(inputend())))
#---------------------------------------------------------
#define prime_number function & return statement
def prime_number(start_point=0,end_point=1,step=1):
    prime_number=[]
    for number in range(start_point,end_point,step):
        if number%2!=0 and number%3!=0 and number%5!=0 and number%7!=0 and number%9!=0 or number==3 or number==5 or number==7:
            prime_number.append(number)
    return prime_number

#---------------------------------------------------------
#define generate_prime function & return statement
def generate_prime():
    return(prime_number(int(inputstart()),int(inputend())))
           
#---------------------------------------------------------
def what_to_print():
    calculation=input("what do you want to calculate (even, odd or prime)?: ")
    if calculation=="even":
        print("\nEVEN NUMBERS\n*****\n",generate_even(),"\n")
    elif calculation=="odd":
        print("\nODD NUMBERS\n*****\n",generate_odd(),"\n")
    elif calculation=="prime":
        print("\nPRIME NUMBERS\n*****\n",generate_prime(),"\n")
    else:
        print ("No calculation is needed... See you when next you need to carryout calculations")
        
#---------------------------------------------------------
print(what_to_print())
