listt=[1,2,3,4,5]
def list_sum_product():
    summ=0
    for number in listt:
        summ+=number
    product=summ*len(listt)
    return product
print("\n\n",list_sum_product())

