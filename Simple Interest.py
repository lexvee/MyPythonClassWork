#simple interet: P=Principal, R=Rate, T=Time
P = 2000
R = 0.1
T = 5
si = (P*R*T)/100
print ("The SI of P is", "$",si)

#request for input from user
P = input ("Enter the P in $: ")
R = input ("Please enter the R in #: ")
T = input ("Again enter the T in Yr: ")
si = (float(P)*float(R)*float(T))/100
print ("The SI of P is", "$",si)

#evaluating input with Isdigit
P = input ("Enter the P in $: ")
R = input ("Please enter the R in #: ")
T = input ("Again enter the T in Yr: ")
if P.isdigit() and R.isdigit() and T.isdigit():
    si = (float(P)*float(R)*float(T))/100
    print ("The SI of P is", "$",si)
else:
    print ("Please enter only degit")
    P = input ("Enter the P in $: ")
    R = input ("Please enter the R in #: ")
    T = input ("Again enter the T in Yr: ")
    si = (float(P)*float(R)*float(T))/100
    print ("The SI of P is", "$",si)
