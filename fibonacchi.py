list =[]
buffer_x = 0                                       
buffer_y=1                                       
list =[buffer_x,buffer_y]
for x in range(2,11):
    fibonacchi = buffer_x + buffer_y                           
    list.append(fibonacchi)
    buffer_x = buffer_y
    buffer_y = fibonacchi
print(list)