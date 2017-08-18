n=int(input())
S=[]
even=str()
odd=str()
for i in range(n):
    s=input()
    S.append(s)
    for j in range(len(S[i])):
        if j%2==0:
            even+=(S[i][j])
        else:
            odd+=(S[i][j])
    s0=(even)
    even=str()
    s1=(odd)
    odd=str()
    print(s0, s1)