#www.codeforces.com
#4A. Watermelon 
#4이상의 짝수면 yes

A = int(input())
if (A >= 4) and (A%2==0):
    print('yes')
else :
    print('no')
    
#A. Adaptation Stories
A=int(input())
lst=input().split(' ')
s=0
r=0
for i in lst:
    s+=int(i)
    if s<0:
        r-=s
        s=0
print(r)

#1A. Theatre Square
lst=input().split(' ')

x = int(lst[0])/int(lst[2])
if x%1!=0:
    x = int(x+1)

y = int(lst[1])/int(lst[2])
if y%1!=0:
    y = int(y+1)
    
print(int(x*y))

#71A. Way Too Long Words
n=int(input())
lst=dict()

for i in range(n):
    lst[i]=input()

for i in range(n):
    if len(lst[i])>10:
        print(lst[i][0]+str(len(lst[i])-2)+lst[i][-1])
    else:
        print(lst[i])

#158A. Next Round
n, k=map(int, input().split(' '))
if n < k:
    z = n
    n = k
    k = z

lst = input().split(' ')
a = int(lst[k-1])
output = 0
for i in lst:
    if int(i)>0:
        if int(i)>=a:
            output+=1
print(output)            
        
#118A. String Task
A = input()
A = A.lower()
str = ''
for i in A:
    if i not in  ['a','o','y','e','u','i']:
        str += '.'
        str += i

print(str)

#50A. Domino piling
m, n=map(int, input().split(' '))
print(int(m*n/2))

#231A. Team
n=int(input())
output=0
for i in range(n):
    a, b, c = map(int, input().split(' '))
    if a+b+c>=2:
        output+=1
print(output)

#282A. Bit++
n=int(input())
output=0
for i in range(n):
    op = input()
    if '--' in op:
        output -=1
    else:
        output +=1
print(output)

#96A. Football
inp=input()
for i in range(len(inp)):
    if inp[i:i+7]=='0000000':
        print('YES')
        break;
    elif inp[i:i+7]=='1111111':
        print('YES')
        break;
    elif i == len(inp)-1:
        print('NO')
        
#112A. Petya and Strings
l1=input().lower()
l2=input().lower()

alp='abcdefghijklmnopqrstuvwxyz'

for i in range(len(l1)):
    if alp.index(l1[i])>alp.index(l2[i]):
        print(1)
        break;
    elif alp.index(l1[i])<alp.index(l2[i]):
        print(-1)
        break;
    elif i == len(l1)-1:
        print(0)
