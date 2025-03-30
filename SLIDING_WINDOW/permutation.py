string1 = "abcdxabcde"
string2 = "abcdeabcdx"

print(len(string1))
print(len(string2))

char = [0]*26
window_size = len(string1)

for char1 in string1:
    char[ord(char1)-ord('a')] += 1
    
    
print(char)
    
freq2 = [0] * 26
i , j = 0,0
flag = False

while j < len(string2):
    
    freq2[ord(string2[j])-ord('a')] += 1
    
    if j >= window_size:
        
        freq2[ord(string2[i])-ord('a')] -= 1
        i += 1
        
        
    if char == freq2:
        print(char)
        print(freq2)
        flag = True
        break
    
    j += 1
    
    
print(flag)


        
        
        
        