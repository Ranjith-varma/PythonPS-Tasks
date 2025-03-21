#print sum of Matrix numbers
mat1 = [[-4,2,10],[5,8,-7],[0,1,-2]]
sum = 0
for i in mat1:
    for j in i:
        print(j)
        sum += j
print("Sum of matrix numbers",sum)

#Print First row (or) list of list
for i in range(0,len(mat1)):
    for j in range(0,len(mat1[i])):
        if i == 0:
            print(mat1[i][j], end=' ')
            
    print()
            
#Print First column (or) list of list
for i in range(0,len(mat1)):
    for j in range(0,len(mat1[i])):
        if j == 0:
            print(mat1[i][j], end=' ')
            
#Print all the elements in matrix            
mat1 = [[-4,2,10],[5,8,-7],[0,1,-2]]
for i in range(0,len(mat1)):
    for j in range(0,len(mat1[i])):
            print(mat1[i][j], end=' ')
            
    print()
    
 #print bounderies of an list   
for i in range(0,len(mat1)):
    for j in range(0,len(mat1[i])):
        if i ==0 or j == 0 or i == len(mat1) -1 or j == len(mat1[i]) -1:
            print(mat1[i][j], end=' ')
        else:
            print(' ',end=' ')
    
    print()
    
    
#Sum of boundarys in a list
mat1 = [[-4,2,10],[5,8,-7],[0,1,-2]]
boundary_sum=0

for i in range(0,len(mat1)):
    for j in range(0,len(mat1[i])):
        if i ==0 or j == 0 or i == len(mat1) -1 or j == len(mat1[i]) -1:
            boundary_sum += mat1[i][j]
            print(mat1[i][j], end=' ')
        else:
            print(' ',end=' ')
    
    print()
print(boundary_sum)

#Sum of Diagnol numbers
mat1 = [[-4,2,10],[5,8,-7],[0,1,-2]]
diagnol_sum=0

for i in range(0,len(mat1)):
    for j in range(0,len(mat1[i])):
        if i == j or i + j == len(mat1) -1 :
            diagnol_sum += mat1[i][j]
            if i == j and i+ j == len(mat1) -1:
                diagnol_sum += mat1[i][j] 

print(diagnol_sum)

#Transpose of Matrix
mat2= [[1,2,3],[4,5,6],[7,8,9]]
def print_matrix(mat2):
    for i in range(0,len(mat2)):
        for j in range(0,len(mat2[i])):
            print(mat2[i][j], end=' ')
        
        print()
        
print_matrix(mat2)
for i in range(0,len(mat2)):
    for j in range(0,len(mat2)):
        if i >= j:
            mat2[i][j], mat2[j][i] = mat2[j][i], mat2[i][j]
            
print_matrix(mat2)

#2nd Approach
for i in range(0,len(mat2)):
    for j in range(0,i):
        mat2[i][j], mat2[j][i] = mat2[j][i], mat2[i][j]

print_matrix(mat2)

#Task:
#print only diagonal elements
#Addition of Matrix
