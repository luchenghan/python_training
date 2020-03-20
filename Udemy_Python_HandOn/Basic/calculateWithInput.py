num =int(input("Input an Integer : "))
n1 = int("%s" % num)
n2 = int("%s%s" % (num,num))
n3 = int("%s%s%s" % (num,num,num))

print("Expected Result :",n1+n2+n3)

total = num + ((num*10) + num) + ((num*100)+(num*10)+num)

print(total)