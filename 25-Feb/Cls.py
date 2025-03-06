#Print Fibonacci Numbers
userInput=int(input("Enter a Number"))
int1=0
int2=1
print(int1)
print(int2)

for i in range(2,userInput):
    int3=int1+int2
    print(int3)
    int1=int2
    int2=int3
    

#Print prime Numbers
#3rd way
userPrimeInput=int(input("Enter a Number"))
if userPrimeInput <2:
    print("It is Not a Prime Number")
else:
    count=0
    
    for i in range(2,userPrimeInput):
        if userPrimeInput % i ==0:
            count+=1
    if count==0:
        print("It is Prime Number")
    else:
        print("It is Not a Prime")
        
        
#4th way
spy=True
for i in range(2,userPrimeInput):
    if userPrimeInput % i ==0:
        spy=False
        print("It is not prime")
        break
        
if spy:
    print("It is Prime")
    

#5th way
spy=True
for i in range(2,userPrimeInput//2+1):
    if userPrimeInput % i ==0:
        spy=False
        print("It is not prime")
        break
        
if spy:
    print("It is Prime")

#6th way    
spy=True
for i in range(2,int(userPrimeInput**0.5)+1):
    if userPrimeInput % i ==0:
        spy=False
        print("It is not prime")
        break
        
if spy:
    print("It is Prime")
    
    
    
#login system where user has 3 attempts to enter correct password
userName="Nani varma"
userPassword="call_me_nani"
totalAttempts=3
   
while totalAttempts>0:
        inputUserName=input("Enter Username:")
        inputPassword=input("Enter Password:")
    
        if userName == inputUserName and userPassword == inputPassword:
            print("Login Successfull")
            break
            # "or"
            #totalAttempts=0
        
        else:
            totalAttempts-=1
            print("Invalid details")
            print("remaining attempts is",totalAttempts)
            
        if totalAttempts==0:
            print("Account On Hold")
            

#by using for loop
# Define correct credentials
userName = "admin"
userPassword = "password123"

# Total number of attempts
totalAttempts = 3  

# Loop for a fixed number of attempts
for attempt in range(totalAttempts, 0, -1):  # Counts down from totalAttempts to 1
    inputUserName = input("Enter Username: ")
    inputPassword = input("Enter Password: ")

    if inputUserName == userName and inputPassword == userPassword:
        print("✅ Login Successful!")
        break  # Exit the loop if login is successful
    else:
        print(f"❌ Invalid details. Remaining attempts: {attempt - 1}")

    if attempt - 1 == 0:
        print("🚫 Account On Hold")



        