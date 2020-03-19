# 0,1,1,2,3,5,8,13,21 up to 150

a = 0
b = 1
list1 = []
while(1):
    n = 0
    n = n+1
    for i in range(0, n):
        c = a+b
        a = b
        b = c
        if c > 150:
            break
        else:
            list1.append(c)
            print(list1)

# 0,1,1,2,3,5,8,13,21 up to 150

# factorial

get_num = int(input('get number for factorial'))
factorial = 1
for i in range(1, get_num+1):
    factorial = factorial*i
print('tha factorial of', get_num, '=', factorial)

# factorial

# match two list

list1 = ['1', '2', '3', '4']
list2 = ['9', '5', '4', '7']
for i in list1:
    if i in list2:
        print('True')

# match teo list

# copy using for loop

list1 = ['aaa', 'bbb', 'ccc', 'ddd']
list2 = []
for i in list1:
    list2.append(i)
print(list2)

# copy using for loop

# add and multiply in list

list1 = []
while(1):
    n = int(input('Enter number'))
    list1.append(n)
    new = 0
    for i in list1:
        new = new+i

    print(new)

# add and multiply in list


# user and password checking

userdetails = {}
while(1):
    username = input('Register user name')
    password = input('Register the password')

    if username != '' and password != '':
        userdetails.update({username: password})
        print(userdetails)
    else:
        break

user1 = input('Enter the Register name')
pass1 = input('Enter the password')

if user1 in userdetails.keys():
    if pass1 in userdetails.get(user1):
        print('Welcome')
    else:
        print('user name or password is wrong')
else:
    print('Get lost user')

# user and password checking

# combine key and value pair

keys = []
k = []
while(1):
    key = input('Enter keys')
    if key == 'stop':
        break
    else:
        keys.append(key)
        print(len(keys))
        print(keys)
for i in range(0, len(keys)):
    values = input('Enter values')
    k.append(values)
    print(k)

dicta = dict(zip(keys, k))
print(dicta)

# combine key and value pair


# nested dictionary start

dict4 = {}

a = 0
b = 0
c = 0
d = 0
dict1_key = []
dict1_val = []
dict2_key = []
dict2_val = []
dict3_key = []
dict3_val = []
if(d == 0):
    while(a < 5):
        a = a+1
        key1 = input('enter the dict1 key')
        dict1_key.append(key1)
    for i in range(0, len(dict1_key)):
        val1 = input('Enter the val1 key')
        dict1_val.append(val1)
        dict1 = dict(zip(dict1_key, dict1_val))

    else:
        d = d+1
        dict4.update({'dict1': dict1})

if(d == 1):
    while(b < 5):
        b = b+1
        key2 = input('enter the dict2 key')
        dict2_key.append(key2)
    for i in range(0, len(dict2_key)):
        val2 = input('enter the dict2 val')
        dict2_val.append(val2)
        dict2 = dict(zip(dict2_key, dict2_val))
    else:
        d = d+1
        dict4.update({'dict2': dict2})

if(d == 2):
    while(c < 5):
        c = c+1
        key3 = input('Enter the dict3 key')
        dict3_key.append(key3)
    for i in range(0, len(dict3_key)):
        val3 = input('enter the dict3 value')
        dict3_val.append(val3)
        dict3 = dict(zip(dict3_key, dict3_val))
    else:
        d = d+1
        dict4.update({'dict3': dict3})

print(dict4)

# nested dictionary stop

# combine dictionary start

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
dict2 = {'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10}
dict3 = {'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15}
dict4 = {}
for x, y in dict1.items():
    dict4.update({x: y})
    for x, y in dict2.items():
        dict4.update({x: y})
        for x, y in dict3.items():
            dict4.update({x: y})
print(dict4)
        ## or or or or or or or or or ###

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
dict2 = {'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10}
dict3 = {'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15}
d=dict1.copy()
d.update(dict2)
d.update(dict3)
print(d)

# combine dictionary stop

# average of marks start
dict1 = {'s_no':1,'eng':60,'tam':85,'mat':90}
dict2 = {'s_no':2,'eng':50,'tam':90,'mat':45}
dict3 = {'s_no':3,'eng':20,'tam':60,'mat':30}
dict4 = {'s_no':4,'eng':70,'tam':45,'mat':40}
while(1):
    roll_no=int(input('Enter the roll no to check your average'))
    a=0
    n=0
    if roll_no in dict1.values():
        for x,y in dict1.items():
            if x!='s_no':
                a=a+y
                n=n+1
                b=a/n
        print('The average of given s_no',roll_no,' is = ',b)
    elif roll_no in dict2.values():
        for x,y in dict2.items():
            if x!='s_no':
                a=a+y 
                n= n+1 
                b=a/n 
        print('The average of given s_no',roll_no,' is = ',b)
    elif roll_no in dict3.values():
        for x,y in dict3.items():
            if x!='s_no':
                a=a+y 
                n= n+1 
                b=a/n 
        print('The average of given s_no',roll_no,' is = ',b)
    elif roll_no in dict4.values():
        for x,y in dict4.items():
            if x!='s_no':
                a=a+y 
                n=n+1 
                b=a/n
        print('The average of given s_no',roll_no,' is = ',b)
    else:
        print('Enter the correct roll no')
    if b>=90 and b<100:
        print('Grade is A')
    elif b>=80 and b<90:
        print('Grade is B')
    elif b>=70 and b<80:
        print('Grade is C')
    elif b>=60 and b<70:
        print('Grade is D')
    else:
        print('Failed')
            
 # average of marks stop


 # character count in string start      
str1 = "count a character occurance"
l=[]
for k in str1:
    if k not in l:
        print ('the no of character',k, 'instr1 = ', str1.count(k))
        l.append(k)
 #character count in string stop  

#Armstrong number
num1 = int(input('Enter the number to check'))
num=num1
lent = len(str(num))
sum = 0

temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** lent
    temp //= 10

if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

#Armstrong number

#quadratic equations start

import math
a=1
b=15
c=50
if a!='' and b!='' and c!='':
    d=(-b+(math.sqrt((b**2)-4*(a*c))))/(2*a)
    e=(-b-(math.sqrt((b**2)-4*(a*c))))/(2*a)
    print(d)
    print(e)


#quadratic equations End














# password not completed

password=[]
i=0
while(i<=5):
    pass1=input('Enter the password')
    i=i+1
    password.append(pass1)
    print(password)
else:
    if pass1 == '':
        if pass1 =='forgot':
            forgot_pass=input('Enter the last password you remember')
            for forgot_pass in password:
                if len(password) >=5:
                    pass1=input('Enter the password first')
                    del password[5]
                    password.insert(0,pass1)
                    print(password)
                    pass1=input('Enter the new password')
                else:
                    i=i+1
                    pass1=input('Enter the password')
                    password.append(pass1)
                    print(password)
            
            else:
                    print('given password is wrong')
        else:
            print('complete')

# password not completed