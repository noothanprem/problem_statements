n=int(input("Enter the number of elements : "))
print("Enter the elements : ")
list1=[]
for i in range(n):
    list1.append(int(input("Enter the element : ")))
print(list1)
n=int(input("Enter the element : "))
for i in range(len(list1)):
    if(list1[i] == n):
        print("Element found at ",i)
        break
    else:
        if(i == len(list1)-1):
            for j in range(len(list1)-1):
                if(n < list1[j]):
                    if(j == 0):
                        print("at : ",j)
                        break
                elif(list1[j] < n < list1[j+1]):
                    print("at : ",j+1)
                    break
                else:
                    if(j == len(list1)-2):
                        print("at : ",len(list1))
                        break
