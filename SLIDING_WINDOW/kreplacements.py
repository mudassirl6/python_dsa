
s = "AABAABA"
k = 2

dict1 = {}
max_freq = 0
j = 0
max_len = 0

for i in range(len(s)):
    dict1[s[i]] = dict1.get(s[i],0)+1
    max_freq = max(max_freq,dict1[s[i]])
    
    if (i-j+1)-max_freq > k:
        dict1[s[j]] -= 1
        j += 1
        
    max_len = max(max_len,i-j+1)


print(max_len)
    
    
