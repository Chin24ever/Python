## Exercise: Python If Condition
# 1. Using following list of cities per country,
#     ```
#     india = ["mumbai", "banglore", "chennai", "delhi"]
#     pakistan = ["lahore","karachi","islamabad"]
#     bangladesh = ["dhaka", "khulna", "rangpur"]
#     ```
# Write a program that asks user to enter a city name and it should tell which country the city belongs to

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

guess=input("Enter a city name: ")
for i in range(0,4):
    if guess==india[i]:
        print("The city is in India")
for i in range(0,3):
    if guess==pakistan[i]:
        print("The city is in Pakistan")
for i in range(0,3):
    if guess==bangladesh[i]:
        print("The city is in Bangladesh")

Enter a city name: dhaka
The city is in Bangladesh

OPTIMISED CODE

if guess in india:
    print("The city is in India")
elif guess in pakistan:
    print("The city is in Pakistan")
elif guess in bangladesh:
    print("The city is in Bangladesh")
else:
    print("Enter correct city")

Enter a city name: mumbai
The city is in India

#Write a program that asks user to enter two cities and it tells you if they both are in same
#country or not. For example if I enter mumbai and chennai, it will print "Both cities are in
#India" but if I enter mumbai and dhaka it should print "They don't belong to same country"

guess1=input("Enter second city: ")

if guess in india and guess1 in india:
    print("The cities are in India")
elif guess in pakistan and guess1 in pakistan:
    print("The cities are in Pakistan")
elif guess in bangladesh and guess1 in bangladesh:
    print("The cities are in Bangladesh")
else:
    print("Enter correct cities")

Enter a city name: mumbai
Enter second city: banglore
The cities are in India

## Exercise: Python If Condition
# 2. Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.
#     1. Ask user to enter his fasting sugar level
#     2. If it is below 80 to 100 range then print that sugar is low
#     3. If it is above 100 then print that it is high otherwise print that it is normal

sugar=int(input("Enter your sugar level: "))

if sugar<=80:
    print("Sugar is low")
elif sugar>80 and sugar<100:
    print("Enter sugar level is normal")
else:
    print("Sugar level is high")

 Enter your sugar level: 100
Sugar level is high
