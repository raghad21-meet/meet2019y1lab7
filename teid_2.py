#Writing function
def add_numbers(start,end):
    total=0
    for number in range(start,end+1):
        #print(number)
        total=total+number
    print(start)
    print(end)
    return(total)


#####################################################

#Calling (using) a function
test1=add_numbers(1,2)
print(test1)
test2=add_numbers(1,100)
print(test2)
test3=add_numbers(1000,5000)
print(test3)

