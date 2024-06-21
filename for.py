# ## Exercise: Python for loop
# 1. After flipping a coin 10 times you got this result,
# ```
# result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
# ```
# Using for loop figure out how many times you got heads

j,k=0,0
for i in range(0,10):
    if result[i]=="heads":
        j=j+1
    elif result[i]=="tails":
        k=k+1
print("Number of times heads occured is "+str(j)+" and number of times tails occured is "+str(k))

Number of times heads occured is 4 and number of times tails occured is 6

# 2. Print square of all numbers between 1 to 10 except even numbers

for i in range (1,11):
    if (i)%2!=0:
        print(pow(i,2))

1
9
25
49
81

# 3. Your monthly expense list (from Jan to May) looks like this,
# ```
# expense_list = [2340, 2500, 2100, 3100, 2980]
# ```
# Write a program that asks you to enter an expense amount and program
# should tell you in which month that expense occurred. If expense is not
# found then it should print that as well.

guess,j=int(input("Enter the amount: ")),0
expense_list = [2340, 2500, 2100, 3100, 2980]

for i in range(0,len(expense_list)):
    if guess==expense_list[i]:
        j=1
        print("The expense occured in ",i+1," month")
if j==0:
    print("The expense did not occur")

Enter the amount: 2980
The expense occured in  5  month

# 4. Lets say you are running a 5 km race. Write a program that,
#    1. Upon completing each 1 km asks you "are you tired?"
#    2. If you reply "yes" then it should break and print "you didn't finish the race"
#    3. If you reply "no" then it should continue and ask "are you tired" on every km
#    4. If you finish all 5 km then it should print congratulations message

j=0
for i in range(0,4):
    print("You completed ",i+1," km")
    ans=input("Are you tired enter yes or no : ")
    if ans=="yes":
        j=1
        break
if j==1:
    print("you didnt finish the race")
else:
    print("You finished the race")

You completed  1  km
Are you tired enter yes or no : no
You completed  2  km
Are you tired enter yes or no : no
You completed  3  km
Are you tired enter yes or no : no
You completed  4  km
Are you tired enter yes or no : no
You finished the race

# 5. Write a program that prints following shape
# ```
# *
# **
# ***
# ****
# *****
# ```

for i in range(0,5):
    for j in range(0,5):
        if j<=i:
            print("*",end="")
    print("\n")

*

**

***

****

*****
