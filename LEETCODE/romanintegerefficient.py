
s= input('enter:')
roman={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
print(type(roman)) 

result = 0

for i in range(len(s)):

	if i+1 < len(s) and roman[s[i]] < roman[s[i+1]]:
		result = result - roman[s[i]]
	else:
		result = result + roman[s[i]]
print(result)

            
