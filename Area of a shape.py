#Area of a shape - Algorithm
#1. Great User
#2. Present options
#3. Evaluate options
#4. Collect values based on selected option
#5. Evaluate values
#6. Calculate
#7. Throw result

#1. Great User
print ("Hello, Welcome to our page")

#2. Present options
positive_response=["Y","Yes","yes","y"]
response=input ("Do you want to perform a calculation")
shapes=["triangle", "circle", "rectangle"]
print (" select any of the", shapes)

#3. Evaluate options
while response in positive_response:
    selectedshape=input("please select any shape = ")
    while selectedshape.lower() not in shapes:
        print ("0nly select from the list")
        selectedshape=input("Please select a shape = ")

    #4. Collect values based on selected option
    if selectedshape=="circle":
        radius=input("please enter radius = ")

    #5. Evaluate values
        while not radius.isdigit():
            radius=input("please enter radius = ")

    #6 Calculate and throw result
        print("the area of the circle with radius",radius,"is",(float(radius)**2)*3.142)

    #7 Repeat step #4, #5 & #6 for other options
    elif selectedshape=="triangle":
        base=input("please enter base = ")
        height=input ("please enter height = ")
        while not base.isdigit() and height.isdigit:
            base=input("please enter base = ")
            height=input("please enter height = ")
        print("the area of the triangle with base & height",base,"&",height,"=",(float(base)*float(height))/2)
    elif selectedshape=="rectangle":
        width=input("please enter width = ")
        length=input ("please enter length = ")
        while not width.isdigit() and length.isdigit:
            width=input("please enter width = ")
            length=input("please enter length = ")
        print("the area of the triangle with base & height",width,"&",length,"=",float(width)*float(length))    
    response=input ("Do you want to perform a calculation")
else:
    print("we are happy to miss you")
    
    #8 Prompt user for another option

