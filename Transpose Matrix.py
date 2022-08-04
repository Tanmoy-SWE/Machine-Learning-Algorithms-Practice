#PYTHON program to find the transpose of a Matrix

#input row and col

p = int(input("Enter number of rows : "))
q = int(input("Enter number of column : "))

#creating a matrix

print("Enter the value of matrix 1 : \n")
matrix1 = [[int(input()) for i in range(p)] for j in range(p)]
print("matrix1 : \n")
for i in range(p):
  for j in range(q):
    print(matrix1[i][j], end="  ")
  print()
result = [[0 for i in range(p)] for j in range(q)]

#Transpose Matrix Calculation
for i in range(q):
  for j in range(p):
    result[i][j] = matrix1[j][i]

#Printing the result
print("Transpose Matrix of Matrix1 : \n")
for i in range(q):
  for j in range(p):
    print(format(result[i][j],"<4"), end="")
  print()
