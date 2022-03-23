def minDistance(n, k, point):
 
    # Sorting points in all dimension
    for i in range(n):
        point[i].sort()
 
    # Output the required k points
    for i in range(n):
        print(point[i][((n + 1) // 2) - 1], end =" ")
 
 
# Driver code
n = 3
k = 4
point = [[0,0,1,1],
         [1,3,4,5],
         [0,3,5,9]]
 
# function call to print required points
minDistance(n, k, point)