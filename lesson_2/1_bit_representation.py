
def bin(n):
    count=0
    while(n>=1):
        if(n%2==0):
            n=n//2
        else:
            count+=1
            n=n//2
    print("Output:",count)
num=int(input("Input: "))
bin(num)