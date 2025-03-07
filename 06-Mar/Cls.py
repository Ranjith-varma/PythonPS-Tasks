#by using for loop
list1=[1,2,20.5,5+7j,"hello"]
for i in list1:
    print("for in i",i)

for j in range(len(list1)):
    print(j)
    print("for in j",list1[j])
    
#by using while loop
i=0
while i < len(list1):
    print(list1[i])
    print(i)
    i+=1
    

#print sum of list
list2=[1,2,3,4,5,6,7,8,9,10]
sum=0

for i in list2:
    sum+=i
print(sum)



# print min value and max value of list
list2=[1,2,3,4,5,6,7,8,9,10]
min_num=list2[0]
max_num=list2[0]
for i in list2:
    if i < min_num:
        min_num = i
    elif i > max_num:
        max_num = i
        
print(min_num)
print(max_num)


# k position in list
k=-5
list1=[22,10,5,9,85,33,61,73,25,-6]
min=list1[0]
max=list1[0]

if k <= -len(list1) or k >= len(list1):
    print("provide Valid Number")
else:
    print(list1[k])
        
print(list2[k])      
        
if k > len(list2):
    print("invalid number")
else:
    print(list2[k])
    
    
#Wap to find duplicates and unique Numbers
list2=[1,2,3,42,51,63,72,8,9,10,51,3,8]
dup=[]
unique=[]

for i in list2:
    if i not in unique and i not in dup:
        unique.append(i)
    elif i in  unique:
        dup.append(i)
        unique.remove(i)
        
    if i in dup:
        dup.append(i)
        
        
        


#by using dictionary method find duplicates and unique Numbers TASK:
list2=[1,2,3,42,51,63,72,8,9,10,51,3,8]
dup=[]
unique=[]
count_dict={}

for i in list2:
    if i in count_dict:
        count_dict[i] += 1
    elif i not in count_dict:
        count_dict[i] = 1
        
for j in count_dict:
    if count_dict[j] == 2:
        for k in range(count_dict[j]): 
            dup.append(j)
            print(j,"duplicate number")
    elif count_dict[j] == 1:
        unique.append(j)
        print(j,"Unique Number")
        
print("duplicate Numbers:",dup)
print("unique Numbers:",unique)