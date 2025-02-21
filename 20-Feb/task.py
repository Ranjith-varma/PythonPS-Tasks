a=int(input("Enter value1:"))
b=int(input("Enter value2:"))
c=int(input("Enter value3:"))

if a>b and a>c:
  print(a,"is greater than",b,"and",c)
elif b>c and b>a:
  print(b,"is greater than",a,"and",c)
elif c>a and c>b:
  print(c,"is greater than",a,"and",b)
elif a == b == c: 
    print("All numbers are equal.")
    
    
#Leap year
year=int(input("Enter a year:"))
if year%400==0:
    print(year,"is leap year")
elif year%100==0:
    print(year,"is not leap year")
elif year%4==0:
    print(year,"is leap year")
else:
    print(year,"is not leap year")
    
#Vowel or Consonent
char=str(input("Enter a Character:")).lower()
if char in["a","e",'i',"o","u"]:
    print("It is Vowel")
if char in['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'u', 'w', 'x', 'y', 'z']:
    print("It is Consonent")
if char in ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']:
    print("It is an Special Character")
else:
    print("Enter valid Characters")
  
#Student Marks  
marks=int(input("Enter your Marks:"))
if marks>=90 and marks<=100:
    print("Grade A")
elif marks>=80 and marks<=89:
    print("Grade B")
elif marks>=70 and marks<=79:
    print("Grade C")
elif marks<0 or marks>100:
    print("Enter valid Marks")
else:
    print("Fail")
    

#Traingle 
side1=int(input("Enter Side1:"))
side2=int(input("Enter Side2:"))
side3=int(input("Enter Side3:"))
if side1>0 or side2>0 or side3>0:
    print("Enter valid Number Sides must be greater than 0")
elif side1+side2>side3 and side2+side3>side1 and side1+side3>side2:
    print("It is a valid Triangle")
else:
    print("It is Not a valid Triangle")
    
