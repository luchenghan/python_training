# Write a Python program to check a triangle is valid or not

def checkTriangle(a,b,c):
    if (a>b+c) or (b>a+c) or (c>a+b):
        print('Not a triangle')
    elif (a== b+c) or (b==a+c) or (c==a+b):
        print('Not,it is a degenerated triangle')
    else:
        print('yes,it is a triangle') 

lengthA = int(input('Enter Line A:\n'))
lengthB = int(input('Enter Line B:\n'))
lengthC = int(input('Enter Line C:\n'))

checkTriangle(lengthA,lengthB,lengthC)