#palindrome by using Finctions
userinput=int(input("enter a number"))
def reverse_num(inputs):
    replace=userinput
    revNum=0
    
    while replace > 0:
        digit= replace % 10
        revNum= revNum * 10 + digit
        replace //= 10
        
    return revNum
print(reverse_num(userinput))

def palindrome(userinput):
    if userinput==reverse_num(userinput):
        return True
    return False
    
print(palindrome(userinput))

#Factorial by using Functions
num1=int(input("enter a factorial number"))    
def num_factorial (input_num):
    if input_num < 0 :
        print("Invalid Number")
        return 
    
    res = 1
    for i in range(1, input_num + 1):
        res *= i
    return res
    
print(num_factorial(num1)) 


#reverse the list by using Functions
list1=[20.5,3+5j,True,10,[15.7,5+5j],False]
def reverse_list(list_input):
    reverse=[]
    
    for i in list1:
        reverse.insert(0,i)
    return reverse 
      
print(reverse_list(list1))

#2nd way to reverse the list by using Functions
list1=[20.5,3+5j,True,10,[15.7,5+5j],False]
def reverse_list(list_input):
    reverse=[]
    
    # for i in list1:
    #     reverse.insert(0,i)
    for i in range(len(list1)-1,-1,-1):
        reverse.append(list1[i])
    return reverse 
      
print(reverse_list(list1))

#3rd way to reverse the list by using Functions
list1=[20.5,3+5j,True,10,[15.7,5+5j],False]
def swaping_num(digits):
    low=0
    high=len(digits)-1
    
    while low < high:
        digits[low],digits[high] = digits[high], digits[low]
        low += 1
        high -=1
    return digits
    
swaping_num(list1)
print(list1)

#4th way to reverse second half of the list by using Functions
list1=[20.5,3+5j,True,10,[15.7,5+5j],False]
def swaping(digits):
    low=len(digits)//2
    high=len(digits)-1
    
    while low < high:
        digits[low],digits[high] = digits[high], digits[low]
        low += 1
        high -=1
    return digits
    
swaping(list1)
print(list1)

