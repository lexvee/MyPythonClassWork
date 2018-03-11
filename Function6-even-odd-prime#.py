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
print("\nPRIME NUMBERS\n*****\n",generate_prime())
