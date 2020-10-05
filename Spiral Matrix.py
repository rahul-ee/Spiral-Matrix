#n = int(input())
#matrix = [[int(x) for x in input().split(' ')] for in range(n)]

def unwrap(matrix,top,left,bottom,right):
    res=[]
    flag = False
    for i in range(top,right):             #start,end
        flag =True
        res.append(matrix[top][i])     #start
    if flag == True:
        flag = False
        for i in range(top+1,bottom):
            flag = True                                    #start+1,end
            res.append(matrix[i][right-1])
    if flag == True:
        flag = False        #end-1
        for i in range(right-2,top-1,-1):
            flag = True         #end-2,start-1
            res.append(matrix[bottom-1][i])
    if flag == True:
        flag = False          #end-1
        for i in range(bottom-2,top,-1):
            #flag = True#end-2,start
            res.append(matrix[i][top]) #start
    return res


matrix = [[1,2,3,4,5,76],[6,7,8,9,10,98],[11,12,13,14,15,54]]

for i in matrix:
    for j in i:                     #top = 1, right = 5
        print(j,end=' ')            #bottom = 2
    print()
u=[]
top =0
right = len(matrix[0])
bottom =len(matrix)
left = 0
while True:
    if top>=bottom or top>=right:
        break
    if len(unwrap(matrix,top,left,bottom,right)) == 0:
        break
    #print(unwrap(matrix,top,left,bottom,right))
    u.extend(unwrap(matrix,top,left,bottom,right))
    top = top+1
    right = right - 1
    bottom = bottom - 1
    
    
    
return (u)
    
    
    
    
