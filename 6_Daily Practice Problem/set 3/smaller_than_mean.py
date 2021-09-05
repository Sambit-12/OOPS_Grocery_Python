import statistics
l= [34,5,25,9,387,3,8,99,466,43,588,52]
mean_n = statistics.mean(l)
count=0
for i in l:
    if i<mean_n:
        count+=1

print(count)