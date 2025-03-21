#Find Missing number in a given input
number=int(input("Enter a number"))
emp_list=[]
def find_min_max(inputs):
    temp=inputs
    while temp > 0:
        rem= temp % 10
        emp_list.append(rem)
        # print(rem)
        temp //= 10
        
find_min_max(number)
print(emp_list)

min_value= min(emp_list)
max_value = max(emp_list)
# print(min_value,max_value)

flag=True
for i in range(min_value,max_value+1):
    if i not in emp_list:
        flag=False
        print(i)
        
if flag:
    print("No missing number b/w",number)
        
        
#Find missing even numbers in a list
emp_list=[-2,4,10,18]
min_num= emp_list[0]
max_num= emp_list[0]
for i in emp_list:
    if i < min_num:
        min_num = i
    if i > max_num:
        max_num = i

print(min_num,max_num)

for i in range(min_num,max_num):
   if i % 2 == 0:
       if i not in emp_list:
           print(i)
           
           
#Find second largest maximum number
list4=[-100,45.5,33,15,-10,2,57]
first_max=float("-inf")
second_max= float("-inf")
for i in list4:
    if i > first_max:
        first_max=i
        
print(first_max)

for i in list4:
    if i!=first_max and i > second_max:
        second_max= i
        
print(second_max)

#2nd approach if any duplicates in list
duplicate_list = [1,2,3,3,5,5,4,7,15,15,2]

set1= set(duplicate_list) #Converted list to set
print(set1)

temp_dup_list = list(set1) #again converted set to list
print(temp_dup_list)

temp_dup_list.sort()
print(temp_dup_list[-2])
