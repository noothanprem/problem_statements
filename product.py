n=int(input("Enter the number of elements in the list : "))
print ("Enter the elements :")
input_list=[]
output_list=[]
for i in range(n):
    input_list.append(int(input("enter the element")))
sum1=1
sum2=1
for i in range(len(input_list)):
    
    for j in range(0,i):
        sum1=sum1*input_list[j]
        
    for k in range(i+1,len(input_list)):
        sum2=sum2*input_list[k]
    
    total=sum1*sum2
    sum1=1
    sum2=1

    output_list.append(total)
print(output_list)
    


