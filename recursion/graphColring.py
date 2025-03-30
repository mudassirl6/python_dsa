# m = 3
# N = 4

# adj_list = [[1,3],[0,2],[1,3],[0,2]]

# color = [0]*N

# def solve(N,node,adj_list,color,m):
    
#     if node == N:
#         return 1
    
#     count = 0
    
#     for c in range(1,m+1):
        
#         if isSafe(c,node,adj_list,color):
            
#             color[node] = c
#             count += solve(N,node+1,adj_list,color,m)
            
#             color[node] = 0
            
#     return count




# def isSafe(c,node,adj_list,color):
    
#     for element in adj_list[node]:
#         if color[element] == c:
#             return False
        
#     return True


# print(solve(N,0,adj_list,color,m))
            
        
    
def solve(N, node, adj_list, color, m):
    if node == N:
        return 1  # Found a valid coloring

    count = 0
    for c in range(1, m + 1):
        if isSafe(c, node, adj_list, color):
            color[node] = c
            count += solve(N, node + 1, adj_list, color, m)  # Continue to next node
            color[node] = 0  # Backtrack

    return count  # Return the number of valid colorings

def isSafe(c, node, adj_list, color):
    for neighbor in adj_list[node]:
        if color[neighbor] == c:
            return False
    return True

# Test case
N = 4
m = 3
adj_list = [[1,3], [0,2], [1,3], [0,2]]  # Adjacency list
color = [0] * N

ways = solve(N, 0, adj_list, color, m)
print("Number of ways to color the graph:", ways)