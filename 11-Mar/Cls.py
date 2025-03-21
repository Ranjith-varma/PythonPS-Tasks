#Find the numbers in the list which are in increasing order
def check_inc_order(inputs):
    temp=inputs
    prev_digit= 10
    
    while temp > 0:
        rem = temp % 10
        if rem >= prev_digit:
            return False
        prev_digit= rem
        # print(rem)
        temp //= 10
    return True
    

list1=[123,341,566,223,11]
result=[]
for i in list1:
    remaining_num=check_inc_order(i)
    result.append(remaining_num)
    
print(result)
    
    
    
# Find a user given number in binary search 
userInput=int(input("Enter a Number"))
list5=[23,75,88,250,353,452,576]
def bin_search(list5,userInput):
    low = 0
    high= len(list5) -1
    
    while low <= high:
        mid = (low + high) // 2
        
        if list5[mid] == userInput:
            return mid
            
        elif list5[mid] > userInput:
            high = mid - 1
            
        else:
            low = mid + 1
        
    return -1
    
print(bin_search(list5,userInput))


#Bobble sort Example
list2=[2,5,-7,-55,84,23,47,92]

for i in range(len(list2)-1):
    for j in range(len(list2)-1 -i):
        if list2[j] > list2[j + 1]:
            list2[j], list2[j + 1] = list2[j + 1], list2[j]
            
print(list2)    