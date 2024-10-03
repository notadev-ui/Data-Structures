l = list()
n = int(input("Enter the number of element to be inserted into list"))
print("Enter",n,"values")
for i in range(n):
    l.append(int(input()))
s = int(input("Enter the element to be searched"))
if s in l:
  print(s,"is found at",l.index(s),"postion" )
        
else:
    print("not")