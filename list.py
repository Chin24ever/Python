# 1. Let us say your expense for every month are listed below,
# 	1. January -  2200
#  	2. February - 2350
#     3. March - 2600
#     4. April - 2130
#     5. May - 2190
#
# Create a list to store these monthly expenses and using that find out,
#
# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this


# 1. In Feb, how many dollars you spent extra compare to January?

expense=[2200,2350,2600,2130,2190]
print("Extra expense in feb compared to jan: "+str(expense[1]-expense[0]))

Extra expense in feb compared to jan: 150

# 2. Find out your total expense in first quarter (first three months) of the year

print("Total expense in first quarter: ",str(expense[0]+expense[1]+expense[2]))

Total expense in first quarter:  7150

# 3. Find out if you spent exactly 2000 dollars in any month

a=0
for x in range(0,4):
    if expense[x]==2000:
        print("Yes i have spent 2000 dollars in a month")
        a=1
if a==0:
    print("No i have not spent exactly 2000 dollars in a month")
  
No i have not spent exactly 2000 dollars in a month

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list

expense.append(1980)
print(expense)

[2200, 2350, 2600, 2130, 2190, 1980]

# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

expense[3]=expense[3]-200
print(expense)

[2200, 2350, 2600, 1930, 2190, 1980]

# 2. You have a list of your favourite marvel super heros
# heros=['spider man','thor','hulk','iron man','captain america']
# Using this list

# 1. Length of the list

heros=['spider man','thor','hulk','iron man','captain america']
print(len(heros)

5

# 2. Add 'black panther' at the end of this list

heros.append("Black Panther")
print(heroes)

['spider man', 'thor', 'hulk', 'iron man', 'captain america', 'Black Panther']

# 3. You realize that you need to add 'black panther' after 'hulk',
# so remove it from the list first and then add it after 'hulk'

heros.pop()
heros.insert(3,"Black Panther")
print(heroes)

['spider man', 'thor', 'hulk', 'Black Panther', 'iron man', 'captain america']

# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.

heros[1:3]=["Doctor Strange"]
print(heroes)

['spider man', 'Doctor Strange', 'Black Panther', 'iron man', 'captain america']

# 5. Sort the list in alphabetical order

heros.sort()
print(heroes)

['Black Panther', 'Doctor Strange', 'captain america', 'iron man', 'spider man']
