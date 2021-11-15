#Antonio
#Practice  using expression and conditonal statments

#An expresion is a problem that must be solved
# 5 + 5 is an "arithmetic" expression
x = 5 + 5

#Functions/methods must be resolved as expressions as well 
answer = input("what is your name?")

#Comparison expression resolve as True/false
print( 7>7 )
print( 7 >= 7 )
print( x == 10 )
print( x > 10 or x < 10 )

#A conditional statements run if its condition is True / not False
if answer == "Bob":
    print("Hello, Bob! Welcome back!")
    print("This line also prints if your name is Bob")
elif answer == "Vadim":
    print("Hey! You still owe me money!")
else:
    print("sorry, I only talk to Bobs")
print("This line isn't inside of the if statement, and  prints regardless")

# ^ If checks a condition
# ^ Elif checks a condition if the previous conditions were not true
# ^ You can have as many  elif's as you want
# ^ Else runs if no prior conditions were true
age = input ( "what is you age")
age=int(age)
if age >= 10:
    print("Congradulations you can get your license")
elif age == 9:
 print("you have one more year to go")
else:
    print("your are to young")
