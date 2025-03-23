def palindrome_check(a):
    low=0
    high=len(a)-1
    
    while low < high:
        if a[low] != a[high]:
            print(low)
            print(high)
            return False
        low +=1
        high -=1
    return True
#Find the substrings of a string   
s = "malayalam"
substrings = []

for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        substrings.append(s[i:j])
print(substrings)    
        
        
#Compare the 2 strings and find the substrings are palindrome if find the indexing number
str1 = "takeuforwardforward"
str2 = "forward"
flag=False
substrings=[]

for i in range(len(str1)):
    for j in range(i + 1, len(str1) + 1):
        substrings.append(str1[i:j])
        if str1[i:j] == str2:
            print(i)
            flag=True
        
    if flag == True:
        break