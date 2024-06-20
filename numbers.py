# Exercise
# 1. You have a football field that is 92 meter long and 48.8 meter wide. Find out total
#    area using python and print it
lenght,width=92,48.8
area=lenght*width
print("The area of the feild is :"+str(area))

The area of the feild is :4489.599999999999

# 2. You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar
#    and you gave shopkeeper 20 dollar.
#    Find out using python, how many dollars is the shopkeeper going to give you back?
quantity,cost,given=9,1.49,20
change=given-(quantity*cost)
print("The change given is: "+str(change))

The change given is: 6.59

# 3. You want to replace tiles in your bathroom which is exactly square and 5.5 feet
#    is its length. If tiles cost 500 rs per square feet, how much will be the total
#    cost to replace all tiles. Calculate and print the cost using python
#    Hint: Use power operator (**) to find area of a square
lenght,cost=5.5,500
area=pow(lenght,2)
cost_total=area*cost
print("The cost of layering the tiles will be :"+str(cost_total))

The cost of layering the tiles will be :15125.0

# 4. Print binary representation of number 17
print("The binary of number 17 is: "+format(17,"b"))

The binary of number 17 is: 10001

