#Print sum of Even numbers in a list 
def digit_sum(input_num):
    temp=input_num
    sum=0
    
    while temp > 0:
        rem= temp % 10
        if rem % 2 ==0:
            sum += rem
        temp //= 10
        
    return sum
    
list1=[122,202,89,8872]
res_list = []
for i in list1:
    temp_res = digit_sum(i)
    res_list.append(temp_res)
    
print(res_list)


#If there is a duplicates in list return True or else return False:
def digit_sum(input_num):
    temp=input_num
    sum=0
    dup_num=[]
    while temp > 0:
        rem= temp % 10
        if rem in dup_num:
            return True
        else:
            dup_num.append(rem)
        temp //= 10
    return False
       
list1=[122,202,89,8872,108]
res_list = []
for i in list1:
    temp_res = digit_sum(i)
    res_list.append(temp_res)
    
print(res_list)

#Comparision of 2 lists if list1 1 values are in list2 print subset or not a subset
list1=[1,3,4,6,5,2,16]
list2=[2,4,3,1,7,5,15] 
flag= True
for i in list1:
    if i not in list2:
       flag= False
       print("list1 is not a subset of list2")
       break
    
if flag:
    print("list1 is Subset of list2")
    
    
#By Using Function
def comparision_lists(list1,list2):
    for i in list1:
        if i not in list2:
            return False
        return True
    
    

#Find if a user given number in list return True or False (linear Search)
list3=[1,4,10,-9.2,7]
userInput=int(input("Enter a number"))

def finding_num(inputs):
    temp=inputs
    for i in list3:
        if userInput not in list3:
            print(userInput,"not in list")
            return False
            # break
        else:
            print(userInput,"in list")
            return True
            
finding_num(list3)



#Need to check after chatgpt corrected the retun statement
def increasing_num(numbers):
    temp_num = numbers
    rev_num = 0

    while temp_num > 0:
        res = temp_num % 10
        rev_num = rev_num * 10 + res
        temp_num //= 10

    return rev_num  # Return the reversed number

list4 = [568, 89, 122, 88, 571]
res_num = []

for i in list4:
    remaining_num = increasing_num(i)  # Store the returned value
    res_num.append(remaining_num)  # Append the reversed number

print(res_num)  # Print the final list of reversed numbers
