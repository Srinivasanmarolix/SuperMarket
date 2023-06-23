from datetime import datetime

print("-----------------------------Welcome-------------------------------")
name=input("Enter your Name: ")

#list of items available in supermarker

Lists='''
Sugar   Rs 40/kg
Rice    Rs 25/kg
Boost   Rs 30/kg
Maggie  Rs 35/pack
Banana  Rs 10/piece
Oil     Rs 90/Ltr
Salt    Rs 25/kg
Paneer  Rs 25/kg
Mat     Rs 25/piece
'''
#declaration

price=0
pricelist=[]
totalprice=0
Finalfinalprice=0
ilist=[]
qlist=[]
plist=[]

items={
    'sugar':40,
    'rice':25,
    'boost':30,
    'maggie':35,
    'banana':10,
    'oil':90,
    'salt':25,
    'paneer':25,
    'mat':25
}

option=int(input("Press 1 to check the items list or Press 2 to exit: "))
if option ==1:
    print(Lists)
for i in range(len(items)):
    inp1=int(input("If you want to buy press 1 OR press 2 for exit: "))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter you item names: ")
        quantity=int(input("Enter Quantity: "))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item, quantity,items, price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("Sorry entered Item is not available")
    else:
        print("you entered wrong number")
    inp=input("can i bill the item YES or NO: ")
    if inp=="yes":
        pass
        if finalamount!=0:
            print(26*">", "SRINIVASAN SUPERMARKET", 26*"<")
            print(33*">", "CHITTOOR", 33*"<")
            print("Name: ",name,23*" ","Date: ",datetime.now())
            print(76*"-")
            print("S.No", 8*" ", "Items",5*" ","Quantity",5*" ","Price")
            for i in range(len(pricelist)):
                print(i,4*" ",7*" ",ilist[i],7*" ",qlist[i],9*" ",plist[i])
            print(76*"-")
            print(50*" ","Total amount: ", "Rs: ", totalprice)
            print(50*" ","GST amount: ", "  Rs: ", gst)
            print(76*"-")
            print(49*" ", "Final amount: ", "Rs: ", finalamount)
            print(76*"-")
            print(25*"<", "Thank you!! Come Again",25*">")
            print(76*"-")
            


