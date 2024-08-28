#creating arrays using five methods

#lateral method
arr1=[1,2,3,4]
print(arr1)

#list() function method
arr2=([1,2,3,4])
print(arr2)

#list comprehension method
arr3=[i for i in range(1,5)]
print(arr3)

#multiply list method
arr4=[1]*4
arr4=[i+1 for i in arr4]
print(arr4)

#using a for loop
arr5=[]
for i in range(1,5):
	arr5.append(i)
print(arr5)	
