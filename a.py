n = int(input())
a = list(map(int, input().split()))
count1=0
count2=0
count3=0
for i in range(len(a)):
    if(a[i]%3==0):
        count1 +=1
    elif(a[i]%3==1):
        count2+=1
    else:
        count3+=1

    
ans = count1+min(count2,count3)
print(ans)