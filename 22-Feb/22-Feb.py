#print all numbers from 1-100
for i in range(1,101):
    print(i)
    
#print sum of n natural number
n=10
sum=0
for i in range(1,n+1):
    sum+=i
    print(i)
print(sum)
#2nd Method to print sum of Numbers
print(n*(n+1)/2)

#Reverse a number
num1=54321
rev_num=0

while num1>0:
    rem=num1 % 10 #reminder #1 #2 #3 #4 #5
    rev_num=rev_num*10 + rem #1 #12 #123 #1234 #12345
    num1=num1 // 10 #5432 #543 #54 #5 #0 loop breaks
    
print(rev_num)

#Practice     
num=int(input("Enter A Number"))
reverse_num=0
sum=0
length=0

while num> 0:
    rem=num % 10
    sum+=rem
    reverse_num= reverse_num*10 + rem
    num=num//10
    length+=1
    
print(reverse_num)
print(sum)
print(length)

#Write a program that keeps asking the user to enter numbers
#until they enter a negative number. Use a while loop.
input_sum=0
input_len=0
while True:
    user_input=int(input("Enter a digit"))
    input_sum+=user_input
    input_len+=1
    if user_input < 0:
        break
print("Sum",input_sum)
print("length",input_len)

#2nd Way
input_num=0
while input_num >= 0:
    input_num=int(input("Enter a digit"))
    
    
#print Even Numbers from 1-50
start_num=2
while start_num <= 50: 
    print(start_num)
    start_num+=2
 
 #2nd Way   
while start_num <= 50:
    if start_num%2 ==0:
        print(start_num)
    start_num+=1
    
    
#Write a program to display the multiplication table of a given
#number. First 20
user=int(input("Enter a Number"))
for i in range(1,21):
    print(user,"*",i,"=",user*i)
    
#By Using While loop
i=1
while i<=20:
    print(user,"*",i,"=",user*i)
    i+=1
    
    
    