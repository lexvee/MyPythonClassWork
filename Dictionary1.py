
booklist=(["bk1","bk2","bk3"])
for book in booklist:
    print(book)
    
#------------------------------------------------------------------
itemdict={"name":"james","color":"white","race":"black"}
for item in itemdict:
    print(item)
    print(itemdict[item])

#-------------------------------------------------------------------
data={"key":"person","preference":["books","movie","pizza",("fun","games","football")]}
for item in data:
        if not type(data[item])==dict:
            print(data[item])
        else:
            for item in data[item]:
                print(item)
                
#------------------------------------------------------------------
#OR
for item in data:
    if type(data[item])==list or type(data[item])==tuple:
        for inneritem in data[item]:
            print(inneritem)
    elif type(data[item])==dict:
        for outeritem in data[item]:
            print(data[item][outeritem])
    else:
        print(data[item])

#-----------------------------------------------------------------
item_list=["books","movie","pizza",("fun","games","football"),{"number":10,"position":"md"},["school", "office"]]
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

extract_item(item_list)
