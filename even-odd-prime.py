positive_response=["Y","Yes","yes","y"]
response=input ("Hello do you want to perform a calculation?: ")
calculation=["even","odd","prime"]

while response in positive_response:
    selected_calc=input("select any of the calculations: ")
    while selected_calc.lower() not in calculation:
        print("select from the list")
        selected_calc=input("select any of the calculations: ")
    if selected_calc=="even":
        start_point=input("what is your start point from 1-2000?: ")
        end_point=input("what is your end point from 1-2000 but < start point?: ")
        while not start_point.isdigit() and end_point.isdigit():
            start_point=input("what is your start point from 1-2000?: ")
            end_point=input("what is your end point from 1-2000 but < start point?: ")
            for num in range(float(start_point),float(end_point),1):
                exclude=[0,1]
                if num%2==0 and num not in exclude:
                    print(num)
    elif selected_calc=="odd":               
        for num in range(2000):
            exclude=[0]
            if num%2==1 and num not in exclude:
                print(num)
