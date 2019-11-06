#n=int(input("Enter the number of elements : "))
list1=[1,2,3,4,5]
print("Enter the elements : ")
# list1=[]
# for i in range(n):
#     list1.append(int(input("Enter the element : ")))
print(list1)
k=int(input("Enter the number of positions to shift : "))
list_len=len(list1)
mid=list_len-k
part1=list1[:mid]
part2=list1[mid:]
rotated_list=part2+part1
print(rotated_list)


    