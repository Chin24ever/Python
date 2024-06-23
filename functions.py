# 1. Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. Equation of an area of a triangle is,
# ```
# area = (1/2)*base*height
# ```

base=float(input("Enter the base of the triangle: "))
height=float(input("Enter the height of the triangle: "))
ans=area(base,height)
print("Area of the triangle is: "+str(ans))

Enter the base of the triangle: 8
Enter the height of the triangle: 6
Area of the triangle is: 24.0

# 2. Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape type it will calculate area. Equation of rectangle's area is,
# ```
# rectangle area=length*width
# ```
# If no shape is supplied then it should take triangle as a default shape

# Calculate area of triangle whose base is 10 and height is 5

base=float(input("Enter the base of the shape: "))
height=float(input("Enter the height of the base: "))
shape=input("Enter the shape: ")
ans=list(area(base,height,shape))
print("Area of the "+str(ans[1])+" is: "+str(ans[0]))

Enter the base of the shape: 4
Enter the height of the base: 2
Enter the shape: 
Area of the triangle is: 4.0

# 3. Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,
# ```
# *
# **
# ***
# ```
# if input is 4 then it should print
# ```
# *
# **
# ***
# ****
# ```
# Basically number of lines it prints is equal to that number. (Hint: you need to use two for loops)

def shape(h):
    for i in range(0,h):
        for j in range (0,i+1):
            print("*",end="")
        print("\n")

height=int(input("Enter the height of pyramid you want: "))
shape(height)

*

**

***

****

