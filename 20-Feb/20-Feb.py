#1st Question
num=0.5
if(num>0):
    print("It is Positive number")
elif(num<0):
    print("It is Negative Number")
else:
    print("It is 0")
    
#2nd Question   
number=9
if(number%2==0):
    print("It is Even Number")
else:
    print("It is Odd Number")
 
#3rd Question   
Vote=10
if(Vote>=18):
    print("Eligible to vote")
else:
    print("Not Eligible to Vote")

#4th Question
inp1=20
inp2=10
if(inp1>inp2):
    print("inp1 is greater")
elif(inp1<inp2):
    print("Inp2 is greater") 
elif(inp1==inp2):
    print("both values are matching")   

#5th Question
marks=40
if(marks>40):
    print("You are Promoted")
elif(marks<35):
    print("you are failed")
elif(marks>=35 and marks<40):
    print("Need to improve Yourself")

#6th Question   
day=8
if(day==1):
    print("Monday")
elif(day==2):
    print("Tuesday")
elif(day==3):
    print("Webnesday")
elif(day==4):
    print("Thursday")
elif(day==5):
    print("Friday")
elif(day==6):
    print("Saturday")
elif(day==7):
    print("Sunday")
else:
    print("Enter valid day")

#7th Question  
num1=10
num2=10
cal="div"
if(cal=="add" or cal=="+"):
    print(num1+num2)
elif(cal=="sub" or cal=="-"):
    print(num1-num2)
elif(cal=="mul" or cal=="*"):
    print(num1*num2)
elif(cal=="div" or cal=="/"):
    if(num2==0):
        print("div with O is not possible")
    else:
        print(num1/num2)
else:
    print("Enter valid method")
 
#8th Question   
month=13
if(month==1):
    print("January")
elif(month==2):
    print("February")
elif(month==3):
    print("March")
elif(month==4):
    print("April")
elif(month==5):
    print("May")
elif(month==6):
    print("June")
elif(month==7):
    print("July")
elif(month==8):
    print("August")
elif(month==9):
    print("September")
elif(month==10):
    print("October")
elif(month==11):
    print("November")
elif(month==12):
    print("December")
else:
    print("Enter valid Month")
