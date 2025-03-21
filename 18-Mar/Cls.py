#Find Sum of a number by using Recursion
num1 = 54672
def find_sum_digits(input_num):
    if input_num <= 0:
        return 0
    return (input_num % 10) + find_sum_digits(input_num // 10)
print(find_sum_digits(num1))

#reverse a string by using recursion
str1= 'Desktop'
def reverse_string(str1):
    if len(str1) <=1 :
        return str1
    return str1[-1] + reverse_string(str1[:-1])
print(reverse_string(str1))

#max elements in a list using recursion
list1= [-2,0,10,-27,101,65,32,95]
def find_list_max(input_list):
    if len(input_list) == 0:
        return 'No maximum'
    if len(input_list) == 1:
        return input_list[0]
    rem_max = find_list_max(input_list[1 : ])
    if input_list[0] > rem_max:
        return input_list[0]
    else:
        return rem_max
    
print(find_list_max(list1))


#Dictionary Problems
#Frequency of Numbers in list
list2 = [1,2,'string',5.5,2,2,7,1,10]
freq = {}
for i in list2:
    if i not in freq:
        freq[i]=1
    else:
        freq[i] += 1
        
print(freq)

#Find Duplicate and unique Numbers
unique =[]
dup=[]

for i,j in freq.items():
    if j > 1:
        dup.append(i)
    else:
        unique.append(i)
        
print("Unique Numbers",unique)
print('Duplicate Numbers',dup)

#Assignment questions:

#2. Given a list of words, return a dictionary where the keys are words and values are their lengths.
#3. Given a string, return a dictionary where keys are characters and values are their occurrence.
#4. Given two lists of equal length, create a dictionary where one list contains keys and the other contains values.