
def maxposition(A, n):


   maxposition = A.index(max(A)) 
   print ("most occuring element in the list:", maxposition + 1) 

A=list()
n=int(input("Enter the size of the List ::"))
print("Enter the Element ::")
for i in range(int(n)):
   k=int(input(""))
   A.append(k)
maxposition(A,n)