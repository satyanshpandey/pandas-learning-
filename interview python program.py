#op:   [(1, 2), (2, 3), (3, 3), (4, 3), (1, 2)]

# input:
s1 = "1122233344411"
# code: 


count = 1
result = []
for i in range(1,len(s1)):
    if s1[i] == s1[i-1]:
         
        count+=1
    else:
        result.append((int(s1[i-1]),count))
        count = 1
        
result.append((int(s1[i]),count))
print(result)
