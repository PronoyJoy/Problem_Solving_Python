
s = input()

alpha_num = 0
alpha = 0
digit = 0
lower = 0
upper = 0

for i in s:
    if i.isalnum():
        alpha_num += 1
    if i.isalpha():
        alpha +=1
    if i.isdigit():
        digit +=1
    if i.islower():
        lower +=1
    if i.isupper():
        upper +=1




if (alpha_num > 0):
    print('True')
else:
    print('False')
if (alpha > 0):
    print('True')
else:
    print('False')
if (digit > 0):
    print('True')
else:
    print('False')

if (lower > 0):
    print('True')
else:
    print('False')

if (upper > 0):
    print('True')
else:
    print('False')






