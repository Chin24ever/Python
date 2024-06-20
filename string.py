# 1. Create 3 variables to store street, city and country, now create address variable to
# store entire address. Use two ways of creating this variable, one using + operator and the other using f-string.
# Now Print the address in such a way that the street, city and country prints in a separate line
street,city,country="Gotri","Vadodara","India"
address=street+"\n"+city+"\n"+country
print("Using + operator\n"+address)

add=f"{street}\n{city}\n{country}"
print("\nUsing f string\n"+add)

Using + operator
Gotri
Vadodara
India

Using f string
Gotri
Vadodara
India

# 2. Create a variable to store the string "Earth revolves around the sun"
#     1. Print "revolves" using slice operator
#     2. Print "sun" using negative index
string="Earth revolves around sun"
print(string[6:14])
print(string[-3:])

revolves
sun

# 3. Create two variables to store how many fruits and vegetables you eat in a day.
# Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits that you eat everyday.
# Use python f string for this.
print(f"I eat {x} vegetables and {y} fruits a day")

I eat 5 vegetables and 6 fruits a day

# 4. I have a string variable called s='maine 200 banana khaye'. This of course is a
# wrong statement, the correct statement is 'maine 10 samosa khaye'.
# Replace incorrect words in original strong with new ones and print the new string.
# Also try to do this in one line.
s="Maine 200 bananas khaye"
s=s.replace("200","10").replace("bananas","samosas")
print(s)

Maine 10 samosas khaye
