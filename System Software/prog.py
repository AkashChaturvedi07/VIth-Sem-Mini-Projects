import mathADD.py
import mathSUB.py
import mathMUL.py
import mathDIV.py
import qSort.py


a=add(5,8)
print(a)


b=sub(5,8)
print(b)


c=mul(5,8)
print(c)


d=div(5,8)
print(d)


arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
  print ("%d" %arr[i])
