#version = 0.1

roll_width = 140
price_per_metre = 5

window_height = input("enter the heiht of the window (cm): ")
window_width = input("enter the width of the window (cm): ")

curtain_width = float(window_width)*0.75+20
curtain_length = float(window_height)+15

widths = curtain_width/roll_width
total_length = curtain_length*widths

total_length2 = (total_length*2)/100

price = total_length2*price_per_metre

print("you need", total_length, "metres of cloth for $",price)





               
               
