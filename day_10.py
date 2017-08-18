if __name__ == '__main__':
    def merge_the_tools(string, k):
        s=string
        n=len(s)
        m=int(n/k)
        sub_str=[]
        new_str=''
        for i in range(m):
            sub_str.append(s[i*m:(i+1)*m])
            ys=sorted(sub_str[i])
            print (ys)
            for j in range(1,m):
                if ys[j]==ys[j-1]:
                    new_str+=ys[j]
                else:
                    new_str += ys[j]
                print(new_str)
            new_str=''



    string, k = input(), int(input())
    merge_the_tools(string, k)