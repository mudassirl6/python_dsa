arr = [12, -1, -7, 8, -15, 30, 16, 28]


i , j = 0,0
window_size = 3
new_list = []
answer = []

while i < len(arr):
    
    if arr[i] < 0:
        new_list.append(arr[i])
        
        
    if i-j+1 == window_size:
        
        if len(new_list):
            answer.append(new_list[0])
            
        else:
            answer.append(0)
           
            
        if arr[j] in new_list:        
            new_list.remove(arr[j])
            
        j += 1
        
    i += 1
        
print(answer)
        


        