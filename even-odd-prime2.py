positive_response=["Y","Yes","yes","y"]
response=input ("Hello do you want to perform a calculation?: ")
calculation=["even","odd","prime"]

while response in positive_response:
    selected_calc=input("select any of the calculations: ")
    while selected_calc.lower() not in calculation:
        print("select from the list")
        selected_calc=input("select any of the calculations: ")
    if selected_calc=="even":
        for num in range(100):
            exclude=[0,1]
            if num%2==0 and num not in exclude:
                print(num)
    elif selected_calc=="odd":               
        for num in range(100):
            exclude=[0]
            if num%2==1 and num not in exclude:
                print(num)
    elif selected_calc=="prime":               
        for num in range(100): 
            if num%2==1 and num%3!=0 and num%5!=0 and num%7!=0 and num%9!=0 or num==3 or num==5 or num==7 or num==9:
                print(num)
else:
    print ("thanks and all the best")
