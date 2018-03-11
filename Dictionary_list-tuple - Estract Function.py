
item_list=["books","movie","pizza",("fun","games","football"),{"number":10,"position":"md","m":{"p":"c","v":"x","h":("b","l")}},["school", "office"]]

#------------------------------------------------------------------
def extract_item(itemsequence):
    if type(itemsequence)==dict:
        for item in itemsequence:
            if type(itemsequence[item])==dict:
                print(itemsequence[item])
            elif type(itemsequence[item])==list or type(itemsequence[item])==tuple:
                for inneritem in itemsquence[item]:
                    extract_item(inneritem)
            else:
                print(itemsequence[item])
    elif type(itemsequence)==list or type(itemsequence)==tuple:
        for item in itemsequence:
            extract_item(item)
    else:
        print(itemsequence)

#-----------------------------------------------------------------
extract_item(item_list)
