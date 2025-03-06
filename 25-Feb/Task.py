#Square a Number 
#Cube a Number
#Exist
while True:
    print("1 to square")
    print("2 to Cube")
    print("3 to Exit")
    User_Input=int(input("Enter your option:"))
    
    if User_Input==3:
        print("Existed ")
        break
    
    elif User_Input==1: #or elif User_Input in [1,2]: we can use this also
        inputValue=int(input("Enter a Digit:"))
        print(inputValue,"Sqaure is",inputValue ** 2)
        
    elif User_Input == 2:
        inputValue=int(input("Enter a Digit:"))
        print(inputValue,"Cube is",inputValue ** 3)    
    else:
        print("Enter a valid Number")
        

#Wap if a number is Palindrome or Not
palindromeNum=int(input("Enter a Number"))
temp=palindromeNum
rev_num=0

while temp>0:
    rem=temp%10
    rev_num=rev_num*10 +rem
    temp=temp//10
    
print(rev_num)

if palindromeNum== rev_num:
    print("Palindrome Number")
else:
    print("Not palindrome Number")    