def Hanoi(n,str,mid,des):
    if n == 1:
        print(str+"->"+des)
        return
    Hanoi(n-1,str,des,mid)
    print(str+"->"+des)
    Hanoi(n-1,mid,str,des)
n = int(input())
Hanoi(n,'A','B','C')