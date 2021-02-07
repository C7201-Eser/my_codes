number = int(input("Enter a number is it is prime number or not :"))
prime_list = []
for item in range(2, number + 1):
    Prime = True
    for inner_item in range(2, item):
        if item % inner_item == 0:
            Prime = False
    if Prime:
        prime_list.append(item)
print ("These are prime numbers  : ",prime_list)