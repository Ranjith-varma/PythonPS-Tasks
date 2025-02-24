# Data Types
#Numeric data types
#Sequensive data type

#Numeric Data types
#Int data type
num=10
print(num)

#float data type
flt=10.5
print(flt)
print(type(flt))

#complex data type
comp=5+7j
print(comp)
print(type(comp))

#String data type
str="Nani Varma"
print(str)
print(type(str))
#It is an Immutable

#Boolean data type
Bool=True
print(Bool)
print(type(Bool))

#None Data type
none=None
print(none)
print(type(none))

#Sequence data type
#list data type
List=[1,True,22.5,[10+5j,10.5],"Ranjith"]
print(List)
print(type(List))

#Tuple data type
tup=(10,True,2.5,(15+5j,10.25),"Ranjith")
print(tup)
print(type(tup))
#It is an Immutable

#range data types
r=range(0,10)
print(list(r))
print(type(r))

# for num1 in range(0,10):
#     print(num1,end=", ")

#set data type
Set={1,2,2,4,7,5,9,9,10,10,15}
print((Set))
print(type(Set))
#It doesn't allow duplicate numbers

#Dictionary Data type
dic={"name":"Ranjith","age":25,"batch":29}
print((dic))
print(type(dic))
#It is an Unordered data type

#Types of Operators
#Arthematic Operators
a=10
b=5
print(a+b)#Addition
print(a-b)#Substraction
print(a*b)#Multiplication
print(a/b)#Division
print(a**b)#Exponentiation
print(a//b)#Floor Division
print(a%b)#Modulus (Remainder)

#Relational or Comparision operators
print(a==b)
print(a!=b)
print(a>=b)
print(a>b)
print(a<=b)
print(a<b)

#Assignment Operators
a=10
print(a)
a=a+5
print(a)
a=a-3
print(a)
a=a*3
print(a)
a=a/5
print(a)
a=a%3
print(a)
a=a//2
print(a)

#Logical Operators
print(2 and 3)
print(3 and 2)
print(0 and 3)
print("" and 0)
print(3 and 0)
# if both conditions are true it output True

print(3 or 2)
print(0 or 5)
print(0 or "")
print(-1 or -3)
#Returns True if at least one condition is true

print(not 5)
print(not 0)
print(not -3)

#Bitwise Operators
print(5&3)
print(5|3)
print(5^3)
print(5>>3)
print(5<<3)
print(~3)

print("Conditional Statements")
#Conditional Statements
#If Condition  Executes if the condition is True.
#elif Condition  Checks another condition if the first one is False.
#else Condition Runs if no previous conditions were True.

weather= 29#int(input("Enther Weather"))

if weather>40:
    print(weather,"Weather is too Hot")
elif weather>30:
    print(weather,"weather is Hot")
elif weather>20:
    print(weather,"Weather is Normal")
elif weather>10:
    print(weather,"Weather is Cold")
elif weather>=1:
    print(weather,"Weather is too Cold")
elif weather<=0:
    print(weather,"Weather is - degrees")
else:
    print("Enter valid Number")
    
#Loops
print("loops")
#Even Numbers
for i in range(1,21):
    if i%2==0:
        print(i)
#Odd Numbers
print("Odd Numbers")
for i in range(1,31,2):
    print(i,end=",")

#While Loop
print("While Loop")
count=0
while count<5:
    print(count)
    count+=1
#While loops runs Until condition gets true

#Jump Statements
print("Jump Statements")
#Break staement: When applies break terminate the complete loop while exicuting
str="Nani Varma"
for r in str:
    if r =="V":
        break
    print(r)
    
#Continue Statement: Its skip the current iteration and enter into the another iteration
print("Continue statement")
List=[1,10,25.2,False,25+5j,[10.5,2+2j],True]
for v in List:
    if v==False:
        continue
    print(v)
    
#Challange
for i in range(1,20):
    if i%3==0:
        continue
    print(i)
#pass Statement
for i in range(1, 6):
    if i == 3:
        pass  # Placeholder (does nothing)
    print(i)
    
    
#Functions: are used to reusable the block of code to make your code easier,efficient and understand
print("functions")
def nani():
    numbers=[]
    for i in range(1,20,3):
        numbers.append(i)
    return numbers
print(i)

#Challange Duplicate words
str1="nani Varma"
def name(text):
  emp=set()
  result=""
  for char in text:
    if char not in emp:
      emp.add(char)
      result+=char
  return result
  

print(name(str1))
