import math

print("Welcome to your new banking app")
print("Investment - to calculate the amount of interest you'll earn on your investment")
print("Bond - to calculate the amount you'll have to pay on a home loan")

# str.casefold makes a users entry all lower case to avoid user entry error
choice = str.casefold(input("What investment you would like? (Investment, Bond) "))


if choice == ("investment"):
    print("You have selected Investment")
     
elif choice == ("bond"):
    print("You have selected Bond")

else:
    print("That is an invalid choice")   # Need to see how to rerun the code after error


# "INVESTMENT" Now to gather deposit / rate / time & intrest rates from the customer

if choice == ("investment"):
    deposit = int(input("How much would you like to deposit? "))
    rate1 = int(input("What is the interest rate? (Numbers only not percentage sign) "))
    time1 = int(input("How many years are you planning on investing? "))
    interest = str.casefold(input("Would you like a (simple) or (compound) interest"))
    
    if interest == str("compound"):
        interest = deposit * math.pow((1+rate1/100),time1)
        print("Choosing the Investment option with a compound interest would generate =")
        print(int(interest))
    
    if interest == str("simple"):
        interest = deposit * (1+rate1/100*time1)
        print("Choosing the Investment option with a simple interest would generate =")
        print(int(interest))

    

elif choice == ("bond"):
     house = int(input("What is the present value of your house? "))
     rate1 = int(input("What is the interest rate? (Numbers only not percentage sign) "))
     month = int(input("The number of months you plan to take to repay the bond? eg.120 "))
     rate1 = rate1/100
     repayment = int((rate1/12 * house)/(1 - (1 + rate1/12)**(-month)))
     print(repayment)

# Now to use the formula to work out compound & simple calculations for the user entry 'Investment'
#nothing here?









    
                


    

    
