#Reverse a String 
#by using Slice
str1= "Nani varma"
print(str1[::-1])

#Reverse a list
list1=[1,2,3,4,5]
print(list1[::-1])

#by using loop
rev_string=''
for i in str1:
    rev_string=i+rev_string

print(rev_string)

# str2="Ranjith varma"
# low=0
# high=len(str2)-1

# while low < high:
#     str2[low],str2[high] =  str2[high],str2[low]
#     low += 1
#     high -= 1
    
# print(str2)   Error Str item does not support item assignment 
#Just for Error idea


str3="a+((b-c)+d)"
emp_str=''
for i in str3:
   if i not in '()':
       emp_str += i
        
print(emp_str)

#2nd Approach
emp=''
for i in str3:
    if i not in '()[]{}':
        emp += i
        
print(emp)

#Remove (,) brackets and count the (,)
str3="{a+((b-c)+d)}"
count=0
close_cnt=''
open_cnt=''
close=0
open=0
for i in str3:
    if i in '([{':
        open_cnt +=i
        count+=1
        open +=1
    elif i in ')}]':
        close_cnt +=i
        count +=1
        close +=1
        
print("Total Count",count)
print('Open bracket',open_cnt,open)
print("Close bracket",close_cnt,close)

#Check a string is palindrome or not
#Approach 1
palindrome= "malayalam"
low_str=0
high_str=len(palindrome)-1
flag = False
while low_str < high_str:
    if palindrome[low_str] == palindrome[high_str]:
        low_str += 1
        high_str-=1
        # print("palindrome")
    else:
        # print("It is not palindrome")
        flag=True
        break
if  flag == False:
    print(f"{palindrome} is a palindrome")
if flag:
    print(f"{palindrome} is not a palindrome")
    
    
    
#Print Unique vowels in a given string 
vowels="take u forward is awesome"
emp_dict={}
for i in vowels:
    if i in 'aeiou':
        if i not in emp_dict:
            emp_dict[i] = 1
        else:
            emp_dict[i] +=1
            
print(emp_dict)

out_put={}
for i,j in emp_dict.items():
    if j == 1:
        # print(i)
        out_put[i] =j
    
       
print(out_put)
   
   

#Find the longest string in a given string
string1="Google docs are much better than word docs"

words=string1.split()
print(words)

longest_word= []
max_length=0

for word in words:
    if len(word) > max_length:
        max_length = len(word)
        longest_word = [word]
    elif len(word) == max_length:
        longest_word.append(word)
print(max_length)
print(longest_word)


#2nd Appraoch
string1="Google docs are much better than word docs"

words = string1.split()
print(words)

largest_word= max(words, key=len)
print(largest_word)



#['aaaaaaaaa', 'bbbbbb', 'cabde'] - Sort strings based on lengths using bubble sort
#['cabde', 'bbbbbb', 'aaaaaaaa']

string_sort= ['aaaaaaaaa', 'bbbbbb', 'cabde']

for i in range(len(string_sort)-1):
    for j in range(len(string_sort)-1 -i):
        if len(string_sort[j]) > len(string_sort[j+1]): #here we used len bcz to find length of string without len it is sorts alphabetics in a lexicographical order
            string_sort[j],string_sort[j+1] = string_sort[j+1],string_sort[j]
            
print(string_sort) 