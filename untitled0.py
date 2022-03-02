num_of_rows=int (input("enter the number of rows:"))
num_of_colums=int (input("enter the number of colums:"))

print("Enter the elements for matrix: ")    
matrix=[[int (input()) for i in range(num_of_colums)] for j in range(num_of_rows)]
print("the current matrix: ")
for i in range(num_of_rows):
     for j in range (num_of_colums):
        print(format(matrix[i][j],"<4" ),end="")
     print()     

result=[[0 for i in range(num_of_rows)] for j in range(num_of_colums)] 
for i in range(num_of_colums):
    for j in range(num_of_rows):
        result[i][j]=matrix[j][i] 
print("the transpose matrix is :")
for i in range(num_of_colums):
     for j in range (num_of_rows):
        print(format(result[i][j] ,"<4"),end="")
     print()    