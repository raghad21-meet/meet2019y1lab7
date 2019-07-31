import turtle



result=[]
n=num
for count in range(1,n):
    if count%3==0:
        result.append("fizz")
    else:
        result.append(count)

turtle.mainloop()




