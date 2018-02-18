#Reina Irizarry
# This program will do the following:
'''Repeatedly ask the user for numbers until they enter a 0 or negative. 
For each number they enter, the program will report if the number was even or odd,
whether it is a perfect square, the sum of the squares of the numbers up to 
and including the number, and the sum of the digits in the number'''

import math
print()
print("************************** Number Analyzer ***************************")
print("  This program is designed to help my ten year old school sister")
print("with math exercises. She will first enter in a number and the program")
print("will determine if it is odd or even. Then determine if it is a perfect ")
print("square, sum of the perfect square and lastly, the sum of the digits.")
print("**********************************************************************")
print()

#This section determines if it is odd or even
num = int(input("Enter a number (0 or negative to quit): "))
while num >0:
    if num == "q":
 break
    if num %2 == 0:
            print("The number is even.")
    else:
          print("The number is odd.")
    
    #This section will determine if it is a perfect square
    if math.sqrt(num) == round(math.sqrt(num)):
        print("The number is a perfect square.")
    else:
        print("The number is not a perfect square.")
    
    #The section will add the the square roots
    addition = 0
    for i in range(num+1):
        addition = addition + math.pow (i,2)
    print("The sum of the first %d squares is %d" % (num,addition))
    
    #This section counts the sum of the digits. 
    factorial = 1
    for i in range(num):
        factorial = factorial * (i + 1) 
    print("The factorial of %d is %d" % (num,factorial))
    #This section will determine the sum of the digits.
    num=num
    sum_digits=0
    while(num>0):
        integer=num%10
        sum_digits=sum_digits+integer
        num=num//10
    print("The sum of digits is",sum_digits)
    num = int(input("Enter a number (0 or negative to quit): "))
