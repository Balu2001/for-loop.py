
n=int(input())
#even number using for loop
for balu in range(2,n,2):
    print(balu,end=' ')
print()

#odd number using for loop

for balu in range(1,n+1,1):
    if balu%2==0:
        continue
    print(balu,end=' ')
print()

#sum of natural number using for loop 

s=0
for i in range(1,n+1):
    s+=i
print(s)