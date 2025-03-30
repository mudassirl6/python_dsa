jobs = [
    [1,2],
    [3,4],
    [5,6],
    [0,4],
    [4,7],
    [8,9],
        ]

jobs = sorted(jobs,key = lambda x:x[1])
take = 1
end_job = jobs[0][1]
print(jobs)
for i in range(1,len(jobs)):
    if jobs[i][0] >= end_job:
        take += 1
        end_job = jobs[i][1]
        
        
print(take)
        