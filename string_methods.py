# a = "Srinivasan"
# print(a.count('i'))
# it will count the given arguments are how many times repeated in the variable

# b = 'srinivasan'
# print(b.endswith('vasan'))
# it will check the arguments is ends with given variable by using boolean

# a = ['srinu', 'mark', 'score', 'surya']

# varun = "this is my book"
# print(varun.find("book"))
# the find will check arguments is available in our variables or not and it will return the index number

#print("hey {} thinnava {}" .format("dude","raa"))
#using .format we can change/add the contrast name from the given value


#examples of Startswith and Endswith
# websites = ['srinu.com', 'mark.in', 'score.com', 'surya.in']
# in_web=[]
# com_web=[]
# for i in websites:
#     if i.endswith("in"):
#         in_web.append(i)
#     else:
#         com_web.append(i)
# print("in websites list", in_web)
# print("com websites list", com_web)

# websites = ['ssrinu.com', 'mark.in', 'sscore.com', 'surya.in']
# ss_web=[]
# other_web=[]
# for i in websites:
#     if i.startswith("ss"):
#         ss_web.append(i)
#     else:
#         other_web.append(i)
# print("in websites list", ss_web)
# print("com websites list", other_web)


# isalpha, isdigit, isalnum, lower, upper, islower and isupper
# srinu = "surya"
# print(srinu.isalpha())

# srinu = "123"
# print(srinu.isdigit())

# srinu = "surya"
# print(srinu.isalnum())

# srinu = "surya123"
# print(srinu.isalnum())

# srinu = "Surya"
# print(srinu.islower()) 

# srinu = "Surya"
# print(srinu.isupper())

# srinu = "VRR"
# print(srinu.isupper())

# srinu = "surya"
# print(srinu.upper())

# srinu = "SURYA"
# print(srinu.lower())


# d="Run a Python script under Windows with the Command Prompt"
# f=d.split()
# n=[]
# for i in f:
#     if i == 'the':
#         i = "that"
#         n.append(i)
#     else:
#         n.append(i)
# print(n)
# f=" ".join(n)
# print(f)
    