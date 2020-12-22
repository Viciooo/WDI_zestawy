sparseMatrix = [[0,0,3,0,4],[0,0,5,7,0],[0,0,0,0,0],[0,2,6,0,0]] 
  
# initialize size as 0 
size = 0
  
for i in range(4): 
    for j in range(5): 
        if (sparseMatrix[i][j] != 0): 
            size += 1
  
# number of columns in compactMatrix(size) should 
# be equal to number of non-zero elements in sparseMatrix 
rows, cols = (3, size) 
compactMatrix = [[0 for i in range(cols)] for j in range(rows)] 
  
k = 0
for i in range(4): 
    for j in range(5): 
        if (sparseMatrix[i][j] != 0): 
            compactMatrix[0][k] = i 
            compactMatrix[1][k] = j 
            compactMatrix[2][k] = sparseMatrix[i][j] 
            k += 1
  
print("row:    ",compactMatrix[0])
print("column: ",compactMatrix[1])
print("value:  ",compactMatrix[2])