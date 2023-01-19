#Write a python function to compute the sum of all odd numbers in a range. Your function will take two numbers as input (that specifies a range) and return a number.
def sum_odd(x, y):
    sum = 0 
    for i in range(x, y+1):
        if i%2 !=0:
            sum += i 
    return sum 

print(sum_odd(1, 10))

