#22-Mar Pattern tasks
#Task:1
userInput=6
for i in range(userInput):
    for j in range(userInput):
        if j in [0,userInput-1] or i==j or i+j ==userInput-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
            
    print()

print("...........") 
  
#Task:2
for i in range(userInput):
    for j in range(userInput):
        if i in [0,userInput-1] or i==j or i+j==userInput-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
            
    print()
    
    
#swaping Methods
#Method 1
a,b=10,20
a,b = b,a
print(a,b)

#Method 2
#Efficient and useful Approch
str1= "varma"
str2 = "nani"
temp = str1

str1=str2
str2=temp
print(str1,str2)

#Method 3
c=10
d=20

c = c + d
d = c - d
c = c - d
print(c,d)

#Method 4
num1= 10
num2= 20

num1 = num1 ^ num2
num2 = num1 ^ num2 
num1 = num1 ^ num2

print(num1,num2)

#Ascending Order function 
def ascending_order(a):
    
    for i in range(len(a)-1):
        if a[i] > a[i + 1]:
            return False
            
    return True
    
list1=[10,15,20,25,35,99]

print(ascending_order(list1))

#Decending Order Function
def decending_order(b):
    for j in range(len(b)-1):
        if b[j] < b[j+1]:
            return True
             
    return False
    
list1=[10,15,20,25,35,99]    

print(decending_order(list1))
    

#Patterns
num=7
#printing patterns
for i in range(num):
    for j in range(num):
        print("*", end=" ")
    print()
    
print(".........")   

#Printing boundaries of patterns
for i in range(num):
    for j in range(num):
        if i in [0,num-1] or j in [0,num-1]:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
print(".........")   

#Printing left up diagnol
for i in range(num):
    for j in range(num):
        if i <= j:
           print("*", end=" ")
        else:
            print(" ", end=" ")
            
    print()

#Print right up diagnol
for i in range(num):
    for j in range(num):
        if i <= j:
            print("*", end=" ")
    print()
    
#Print right down diagnol
for i in range(num):
    for j in range(num):
        if i >= j:
            print("*", end=" ")
    print()

#Print Down Left pattern
for i in range(num):
    for j in range(num):
        if i+j==num-1 or j==num-1 or  i >= num - j - 1:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()
    
print('.........')

#Print Horizontal Diagnol
for i in range(num):
    for j in range(num):
        if i >= j:
            print("*", end=" ")
    print()

for i in range(num-1):
    for j in range(num-1):
        if i <= j:
            print("*", end=" ")
    print()

print(".........")

#Print left up doundary diagnol
for i in range(num):
    for j in range(num):
        if i == 0 or j == num-1 or i == j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
            
    print()
    
print(".........")

#Print Right Upper boundary diagnol
for i in range(num):
    for j in range(num):
        if i == 0 or j == 0 or i +j == num-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
            
    print()     

print('.........') 

#print Down left boundary pattern
for i in range(num):
    for j in range(num):
        if j==num-1 or i==num-1 or i+j==num-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
print('.........')
    
#Print Down Right boundary Pattern
for i in range(num):
    for j in range(num):
        if j==0 or i==num-1 or i==j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
            
    print()  
print('.........') 

#Print Horizontal Boundary Diagnol
for i in range(num):
    for j in range (num):
        if j==0 or i==j:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print() 
    
for i in range(num):
    for j in range(num):
        if j==0 or i+j==num-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()  
    
print('.........')
    
    
    
    
    
    
    
    
    
    
    
    
    
    