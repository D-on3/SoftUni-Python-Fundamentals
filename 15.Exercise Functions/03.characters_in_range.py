


def iteration(arg1,arg2):
    range1=ord(arg1)
    range2=ord(arg2)
    for i in range(range1+1,range2):
        print(chr(i),end=' ')


iteration(input(),input())