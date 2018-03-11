#Define and assign variables
positive_response=["Y","Yes","yes","y"]
response=input ("Hello do you want to perform a calculation?: ")
calculation=["even","odd","prime"]

#Confirm Calculation is needed, collect input data, loop and evaluate 
while response in positive_response:
    selected_calc=input("\nselect any of the calculations (even, odd or prime): ")
    while selected_calc.lower() not in calculation:
        print("select from the list", calculation)
        selected_calc=input("select any of the calculations: ")
    if selected_calc=="even":
        start_point=input("what is range start point: ")
        while not start_point.isdigit():
            start_point=input("what is range start point: ")
        end_point=input("what is range end point: ")
        while not end_point.isdigit():
            end_point=input("please enter digit: ")
        for num in range(int(start_point),int(end_point)):
            exclude=[0,1]
            if num%2==0 and num not in exclude:
                print(num,end=" ")
    elif selected_calc=="odd":               
        start_point=input("what is range start point: ")
        while not start_point.isdigit():
            start_point=input("what is range start point: ")
        end_point=input("what is range end point: ")
        while not end_point.isdigit():
            end_point=input("what is range end point: ")
        for num in range(int(start_point),int(end_point)):
            exclude=[0]
            if num%2==1 and num not in exclude:
                print(num,end=" ")
    elif selected_calc=="prime":               
        start_point=input("what is range start point: ")
        while not start_point.isdigit():
            start_point=input("what is range start point: ")
        end_point=input("what is range end point: ")
        while not end_point.isdigit():
            end_point=input("what is range end point: ")
        for num in range(int(start_point),int(end_point)):
            if num%2==1 and num%3!=0 and num%5!=0 and num%7!=0 and num%9!=0 or num==3 or num==5 or num==7:
                print(num,end=" ")
                
else:
    print ("No calculation is needed... See you when next you need to carryout calculations")
