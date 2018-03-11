positive_response=["Y","Yes","yes","y"]
response=input ("Hello do you want to perform a calculation?: ")
calculation=["even","odd","prime"]

while response in positive_response:
    selected_calc=input("select any of the calculations: ")
    while selected_calc.lower() not in calculation:
        print("select from the list")
        selected_calc=input("select any of the calculations: ")
    if selected_calc=="even":
        start_point=input("what is range start point: ")
        end_point=input("what is range end point: ")
        for num in range(int(start_point),int(end_point)):
            exclude=[0,1]
            if num%2==0 and num not in exclude:
                print(num)
    elif selected_calc=="odd":               
        start_point=input("what is range start point: ")
        end_point=input("what is range end point: ")
        for num in range(int(start_point),int(end_point)):
            exclude=[0]
            if num%2==1 and num not in exclude:
                print(num)
    elif selected_calc=="prime":               
        start_point=input("what is range start point: ")
        end_point=input("what is range end point: ")
        for num in range(int(start_point),int(end_point)):
            if num%2==1 and num%3!=0 and num%5!=0 and num%7!=0 and num%9!=0 or num==3 or num==5 or num==7:
                print(num)
else:
    print ("thanks and all the best")
