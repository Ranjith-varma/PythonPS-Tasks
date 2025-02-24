# #Print all numbers from 1 to 100 that are divisible by 3 and 5
# #using a for loop.

# for i in range(1,101):
#     if i % 3 ==0:
#         print("divisible by 3",i)
#     elif i % 5 ==0:
#         print("divisible by 5",i)
        

# #Check if a given number is a prime number using a for
# #loop.

# num = int(input("Enter a number: "))

# if num < 2:
#     print(f"{num} is not a prime number.")
# else:
#     count = 0  

#     for i in range(1, num + 1):
#         if num % i == 0:
#             count += 1  

#     if count == 2:  
#         print(f"{num} is a prime number.")
#     else:
#         print(f"{num} is not a prime number.")
        
# #2nd way
# number=int(input("Enter a Number:"))
# flag=0
# for i in range(2,number+1):
#     if number%i==0:
#         flag+=1
        
# if flag==1:
#     print(number,"is Prime Number")
# else:
#     print(number,"is Not Prime Number")
    
#Write a program to calculate the factorial of a number using
#a while loop.

fact=int(input("Enter a Fact Number:"))
fact_number=1 #Mul of 0 is always gives 0
i=1

if fact<0:
    print("Enter a Postive Number")
elif fact==0:
    print(fact," factorial number is 1")
else :   
    while i<=fact:
        fact_number*=i #fact_number=fact_number*i 1*1=1,1*2=2,2*3=6,6*4=24
        i+=1 #increases the i value for each iteration 2,3,4
    print(fact,"of factorial Number is-",fact_number)

#2nd Way factorial number
fact=int(input("Enter a Fact Number:"))
fact_number=1 #Mul of 0 is always gives 0

if fact<0:
    print("Enter a Postive Number")
elif fact==0:
    print(fact," factorial number is 1")
else:    
    while fact > 1:
        fact_number *= fact #fact_number=fact_number*i 1*5=5,5*4=20,20*3=60,60*2=120
        fact-=1 #Decreases the i value for each iteration 5,4,3,2,1,iteration stops
    print(fact,"of factorial Number is-",fact_number)



