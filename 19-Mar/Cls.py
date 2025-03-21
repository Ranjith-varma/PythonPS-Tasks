#Find the Maximum key in a Dictionary
dict1= {'1':2,'str':4, '55':12, 'apple':11}

max_value= float('-inf')
max_key = ''

for i,j in dict1.items():
    if j > max_value:
        max_value = j
        max_key = i
        
if max_value != float('-inf'):
    print(max_key)
else:
    print("Dictionary is Empty no Max key to print")
    
#Convert keys into values and values into keys
dict1= {'1':2,'str':4, '55':12, 'apple':11,'5':2}
result_dict={}
for i,j in dict1.items():
    if j not in result_dict:
       result_dict[j] = [i]
    else:
        result_dict[j].append(i)
        
print(result_dict)

#8. Given two dictionaries, merge them into one. If a key exists in both, sum their values.
dict1= {'1':2,'str':4, '55':12, 'apple':11,'5':2}
dict2={'1':2, 'nani':5}

output_dict={}

for i,j in dict1.items():
    output_dict[i] = j
    
for i,j in dict2.items():
    if i in output_dict:
        output_dict[i] += j
    else:
        output_dict[i] = j

print(output_dict)

#9. Find if 2 strings are anagrams
str1="below"
str2="elbow"

dict3={}
dict4={}

def check_anagram(a,b):
    if len(str1) != len(str2):
        return False
        
    for i in str1:
        if i in dict3:
            dict3[i] += 1
        else:
            dict3[i] = 1
        
    for j in str2:
        if j in dict4:
            dict4[j] += 1
        else:
            dict4[j] = 1
            
    if dict3 == dict4:
        print("This is Anagram")
        return True
        
    return False
        
print(check_anagram(str1,str2))


#7. Given a list of numbers, return a dictionary of elements that appear 
# more than once along with their counts.

list2=[1,1,1,2,3,3,4,5]
dict5={}
output_dict={}

for i in list2:
    if i not in dict5:
        dict5[i] = 1
    else:
        dict5[i] +=1
        
print(dict5)

for i,j in dict5.items():
    if j >= 2:
        output_dict[i] = j
        
print(output_dict)


#Assignments:
#Finding the frequency of elements in an array.
#arr = [10, 30, 10, 20, 10, 20, 30, 10]  O/p: 10=> 4 30 =>2  20=> 2

array=[10, 30, 10, 20, 10, 20, 30, 10]
emp_arr={}
count=0
for i in array:
    if i not in emp_arr:
        emp_arr[i] = 1
    else:
        emp_arr[i] += 1
      
print(emp_arr)


# Count Occurrences of Each Digit
# input: 2788
# output: 2=> 1
# 7=> 1
# 8=> 2

inp= 2788
temp_inp = inp
freq_inp={}
res_rem=[]
while temp_inp > 0:
    rem = temp_inp % 10
    res_rem.append(rem)
    temp_inp //= 10

res_rem.sort()  
# sort_list=sorted(res_rem) 
# print(sort_list)
print(res_rem)
for i in res_rem:
    if i not in freq_inp:
        freq_inp[i] = 1
    else:
        freq_inp[i] +=1
        
print(freq_inp)    


# Wap to print the number of pairs formed by the array of elements
#  Input: 10 20 10 30 20 20	  Output: 2 pairs
#  Input: 30 50 30 50 20 50 50 20 50 50    Output : 5 pairs

def count_pairs(inp):
    freq_arr={}
    pairs=0
    
    for i in inp:
        if i in freq_arr:
            freq_arr[i] += 1
        else:
            freq_arr[i] =1
            
    print(freq_arr)
    
    for i,j in freq_arr.items():
        # if j >= 2:
        pairs += j //2
        
    return pairs

arr = [30, 50, 30, 50, 20, 50, 50, 20, 50, 50]
arr2=[10,20,10,30,20,20]

result=count_pairs(arr)
arr2_result=count_pairs(arr2)

print("Total",result,'pairs')
print("Total",arr2_result,'pairs')