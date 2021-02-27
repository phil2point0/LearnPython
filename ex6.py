# This section is making two variables. types_of_people is an integer
# and x is a string that also has types_of_people inserted into it.
types_of_people = 10
x = f"There are {types_of_people} types of people."

#This section is making three variables, and inserting the first two into
#the y variable which is a string.
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

#This is printing the two string variables x and y.
print(x)
print(y)

#This is printing two strings with the x and y string variables inserted
print(f"I said: {x}")
print(f"I also said: '{y}'")

# This section is making two variables. One Boolean and one a string
#Then it is printing out the string but formatting it by the Boolean variable
hilarious = False
joke_evaluation = "Isn't the joke so funny?! {}"
print(joke_evaluation.format(hilarious))

#This section is making two more string variables
#then it is printing them out by adding them together
#String + String = A combined String
w = "This is the left side of..."
e = "a string with a right side."

print(w+e)
