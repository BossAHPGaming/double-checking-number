number = int(input("Enter Number to check: "))
print("number to be checked :", number)

if number>50:
    print("number is greater than 50")
    if number%2==0 :
        print("This is even number")
    else:
         print("This is an odd number")

else:
    print("Number is not greater than 50")
