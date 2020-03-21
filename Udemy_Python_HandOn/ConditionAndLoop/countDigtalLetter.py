# Write a Python program that accepts a string and calculate the number of digits and letters
# Sample Data : "Python 3.2"
# Expected Output :
# Letters 6 
# Digits 2

inputString = input("Input a string : ")
Digtal = 0
Letter = 0
notDigtalAndLetter = 0
for i in inputString:
    if i.isdigit():
        Digtal=Digtal+1
    elif i.isalpha():
        Letter=Letter+1
    else:
        notDigtalAndLetter=notDigtalAndLetter+1
print("Digtals : ",Digtal)
print("Letters : ",Letter)
print("Not Digtal And Letter : ",notDigtalAndLetter)