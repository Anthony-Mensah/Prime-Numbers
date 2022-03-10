#This program accepts a number and output prime numbers within the number
#ACCEPT AN INPUT
try:
    number = int(input("Enter number: "))
    if number < 1:
        for i in range(100):
            print("Enter a number greater than 0")
            number = int(input("Enter number: "))
            if number > 0:
                break
except ValueError:
    print('Enter a postive integer')

#SUM VARIABLE
add = 0
for i in range(1,number+1):
    sum = 0
    for x in range(1,i + 1):
        if i % x == 0:
            sum+= 1
    if sum == 2:
        print("{} is a prime number.".format(i))
        add+=1

print("There are {} prime numbers from 1 to {}".format(add,number))

