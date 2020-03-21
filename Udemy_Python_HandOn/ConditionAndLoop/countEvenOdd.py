# Count the number of even and odd numbers from a series of numbers
# Input 
# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) # Declaring the tuple
# Output
# Number of even numbers : 4                                                                                    
# Number of odd numbers : 5

numbers = (1,1,3,4,5,6,7,8,91)

countOdd = 0
countEven = 0

for i in numbers:
    if(i%2!=0):
        countOdd=countOdd+1
    else:
        countEven=countEven+1

print('Number of Odd numbers : ',countOdd)
print('Number of Even numbers : ',countEven)