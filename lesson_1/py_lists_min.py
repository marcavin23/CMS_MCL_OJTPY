
def minposition(A, n):

    minposition = A.index(min(A))
    print("least occuring element in the list :", minposition + 1)
    

A=list()
n=int(input("Enter the size of the List ::"))
print("Enter the Element ::")
for i in range(int(n)):
   k=int(input(""))
   A.append(k)
minposition(A,n)