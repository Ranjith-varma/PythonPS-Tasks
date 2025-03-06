#Print Duplicates in a list
list1=[1,1,2,2,3,3,4,5,4,6,7,8,7,9]
list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)
    else:
        print(i,"is duplicate")
        
        

# Find a Perfect Number 
perfect_num=int(input("Enter a Number"))
temp=perfect_num

sum=0
for i in range(1,perfect_num):
    if perfect_num % i == 0:
        sum+=i
print(sum)
if perfect_num==sum:
    print("Perfect Number")
else:
    print("Not a Perfect number")
    
    

#find LCM(Least Common Multiple) of two numbers
def lcm_method(a,b):
    num1=a
    num2=b
    divisor=2
    lcm=1
    
    while num1>1 or num2>1:
        if num1 % divisor == 0 or num2 % divisor == 0:
            lcm*= divisor
        
            if num1 % divisor == 0:
                num1 //= divisor
            
            if num2 % divisor ==0:
                num2 //= divisor            
        else:
            divisor +=1        
    return lcm
    
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("LCM of",num1, "and",num2,"is",lcm_method(num1,num2))


#2nd Way LCM Number:
import math

def find_lcm(a, b):
    return (a * b) // math.gcd(a, b)  # LCM formula

# Input numbers
num1 = int(input("Enter 1st Number"))
num2 = int(input("Enter 2nd Number"))

# Print the LCM
print("LCM of", num1, "and", num2, "is:", find_lcm(num1, num2))


#without using function
import math
num1 = int(input("Enter 1st Number"))
num2 = int(input("Enter 2nd Number"))

lcm=(num1*num2 // math.gcd(num1,num2))
print("LCM of",num1, "and",num2,"is",lcm)


#calculate total allocated budget for all even numbered Teams members:
team_budget = {1: 5000, 2: 7000, 3: 6000, 4: 8000, 5: 5500, 6: 7500}

total_even_budget = sum(budget for team, budget in team_budget.items() if team % 2 == 0)

print("Total allocated budget for even-numbered teams:", total_even_budget)
