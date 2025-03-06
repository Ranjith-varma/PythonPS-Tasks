def smallest_prime_digit(number):
    # Filter only prime digits (2, 3, 5, 7) directly
    prime_numbers = list(filter(lambda x: x in "2357", str(number)))

    return min(prime_numbers) if prime_numbers else "No prime digits found."

# Input: Fingerprint converted number
num = int(input("Enter the fingerprint-derived number: "))
print("Smallest prime digit:", smallest_prime_digit(num))


#Wap to print sum of Non-primes in a number
non_prime_numbers=[]
def check_prime(inputs):
    if inputs < 2:
        return False
    for i in range(2,inputs):
        if inputs % i == 0:
            return False
    return True
    
nonPrime=int(input("Enter a Number"))
temp=nonPrime
non_prime_sum=0
while temp > 0:
    digit= temp % 10
    # print(digit)
    if check_prime(digit)== False:
        non_prime_numbers.append(digit)
        non_prime_sum+= digit
    temp= temp // 10


print("Sum of Non Prime Numbers is",non_prime_sum)
print(non_prime_numbers)


#Wap to print sum of Odd digits in a number
def check_odd_numbers(n):
   return n % 2 != 0
    
oddNumbers=int(input("Enter a numbers"))
replace=oddNumbers
odd_numbers_sum=0
odd_numbers=[]
while replace > 0:
    numbers= replace % 10
    # print(numbers)
    if check_odd_numbers(numbers):
        odd_numbers.append(numbers)
        odd_numbers_sum+= numbers
    replace = replace // 10
    
print("Sum of Odd Numbers",odd_numbers_sum)
print(odd_numbers)
    

#Armstrong Number
numberInput=int(input("Enter a Number"))
tempNumber=numberInput
sum_armNumber=0
while tempNumber > 0:
    nums=tempNumber % 10
    sum_armNumber+= nums ** len(str(numberInput))
    # print(nums)
    tempNumber//=10
print(sum_armNumber)  

if sum_armNumber == numberInput:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
    
    
#Armstrong range of Numbers by using function
input1=int(input("Enter Min Number"))
input2=int(input("Enter Max Number"))

def check_armstrong(receive):
    temp_receive = receive
    sum_armstrong_num=0
    
    while temp_receive > 0:
        rem= temp_receive % 10
        # print(rem)
        sum_armstrong_num+= rem ** len(str(receive))
        temp_receive//=10
    
    if sum_armstrong_num ==  receive:
        return True
    else:
        return False
        
for i in range(input1,input2+1):
    if check_armstrong(i):
        print(i)
   