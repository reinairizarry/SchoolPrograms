#Reina Irizarry
#Matchmaker program

#Print statemnts include, program version, company name and details on how to play
print()
print("|*******************************************| ") 
print("|        \t Matchmaker 1.0\t            | ")
print("|\tHelping you find luv since 94       |")
print("|             \tReina, Inc.                 |")
print("|*******************************************| ") 
print("(\__/) ||")
print("(•ㅅ•) ||") 
print("/ 　 づ")
print("***************************************************************")
print("This program will determine if we are meant to be.")
print()
print("There will be five questions.Type 5 if you strongly agree, ")
print("4 if you agree, 3 if you somewhat agree, 2 if you disagree,")
print("and lastly, type 1 if you strongly disagree.")
print("***************************************************************")

#question one 
print()
puppies = int(input("1. How much do you love puppies? "))

#question two
breakfast = int(input("2. Breakfast is acceptable to eat at anytime of the day. "))

#question three
cc = int(input("3. How important is climate change? "))

#question 4
pr = int(input("4. Parks and Recreation is better than The Office. " ))

#question 5
mario = int(input("5. Super Mario is the best game ever made. "))
print()

#calculation
count = (puppies+breakfast+cc+pr+mario)

#print satements
print("Your total is",count, "points.")
print()
print("Calculating...")
print()

#if statements
if count >= 25:
    print("Lets be best freinds!")
elif count >= 15:
    print("Lets be freinds!")
elif count >=6:
    print("You are a horrible person.")
else:
    print("Hello? is there a pulse?")
