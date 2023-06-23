# num = [1,2,3,4,5,6,7,8,9,10]
# num_to_remove = [1,9]

# num = [i for i in num if i not in num_to_remove] #shothand if elif
# print(num)

# websites = ["abc.com","xyz.in","work.com",'main.in']
# in_web=[]
# com_web=[]
# for i in websites:
#     if i.endswith('in'):
#         in_web.append(i)
#     else:
#         com_web.append(i)
# print("in websites", in_web)
# print("com websites",com_web)

# websites = ["abc.com","xyz.in","work.com",'main.in']

# in_web=[]
# com_web=[]
# f=[in_web.append(i) if i.endswith('in') else com_web.append(i) for i in websites]
# print(in_web,com_web)

#format

# print("hey {}, em {}" .format("uday","thinnava"))
# print("hey {}, em {}" .format(a="uday", b="thinnava"))


names=('meena', 'pavan', 'kiran', 'tharun', 'varun')

for i in names:
    print("Hey {} thinnava ra" .format(i))


