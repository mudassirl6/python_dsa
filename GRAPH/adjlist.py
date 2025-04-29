def adjlist():
    n,m = map(int,input().split())
    
    adj = [[] for i in range(n+1)]
    
    print(adj)    
    for i in range(m):
        
       
        u,v = map(int,input().split())
        adj[u].append(v)
        adj[v].append(u)
        
        
    print(adj)   
    
    
adjlist()      
        

        