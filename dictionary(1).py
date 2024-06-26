dic={"China":143,
         "India":136,
         "USA":32,
         "Pakistan":21}
def main():
    n="no"
    while n=="no":

        inp=int(input("To print the dictionary select 1\nTo add values "
                    "to the dictionary select 2\nTo remove a value from "
                    "the dictionary select 3\nTo query about a specific "
                    "country select 4\n\nEnter what you want to do: "))
        print("")
        if inp == 1:
            prin()
        elif inp == 2:
            add()
        elif inp == 3:
            remove()
        elif inp == 4:
            query()
        n=input("Do you want to end the programme? Enter (yes/no): ")
        print("")
        while n!="yes" and n!="no":
            n = input("Choose correctly!!! Enter (yes/no): ")
            print("")

def prin():
    for key, value in dic.items():
        print(key + " ==> " + str(value))
    print("")

def add():
    key = input("Enter the country you want to add: ")
    if key in dic.keys():
        print("\nThis country already exist in the dictionary")
    else:
        value = input("Enter the population of that country in millions: ")
        dic.update({key: value})
        print("The updated dictionary is: \n")
        print("New dictionary:\n")
        for key, value in dic.items():
            print(key + " ==> " + str(value))
    print("")

def remove():
    key = input("Enter the country you want to remove: ")
    if key in dic.keys():
        dic.pop(key)
        print("New dictionary:\n")
        for key, value in dic.items():
            print(key + " ==> " + str(value))
    else:
        print("\nThe country does not exist in dictionary")
    print("")

def query():
    key = input("Enter the country you want information about: ")
    if key in dic.keys():
        print("\nThe country " + key + " has " + str(dic[key]) + " million population\n")
    else:
        print("\nThe country does not exist in dictionary\n")

if __name__=="__main__":
    main()


"""
To print the dictionary select 1
To add values to the dictionary select 2
To remove a value from the dictionary select 3
To query about a specific country select 4

Enter what you want to do: 1

China ==> 143
India ==> 136
USA ==> 32
Pakistan ==> 21

Do you want to end the programme? Enter (yes/no): a

Choose correctly!!! Enter (yes/no): no

To print the dictionary select 1
To add values to the dictionary select 2
To remove a value from the dictionary select 3
To query about a specific country select 4

Enter what you want to do: 2

Enter the country you want to add: Korea
Enter the population of that country in millions: 10
The updated dictionary is: 

New dictionary:

China ==> 143
India ==> 136
USA ==> 32
Pakistan ==> 21
Korea ==> 10

Do you want to end the programme? Enter (yes/no): no

To print the dictionary select 1
To add values to the dictionary select 2
To remove a value from the dictionary select 3
To query about a specific country select 4

Enter what you want to do: 2

Enter the country you want to add: Korea

This country already exist in the dictionary

Do you want to end the programme? Enter (yes/no): no

To print the dictionary select 1
To add values to the dictionary select 2
To remove a value from the dictionary select 3
To query about a specific country select 4

Enter what you want to do: 3

Enter the country you want to remove: Korea
New dictionary:

China ==> 143
India ==> 136
USA ==> 32
Pakistan ==> 21

Do you want to end the programme? Enter (yes/no): no

To print the dictionary select 1
To add values to the dictionary select 2
To remove a value from the dictionary select 3
To query about a specific country select 4

Enter what you want to do: 3

Enter the country you want to remove: Korea

The country does not exist in dictionary

Do you want to end the programme? Enter (yes/no): no

To print the dictionary select 1
To add values to the dictionary select 2
To remove a value from the dictionary select 3
To query about a specific country select 4

Enter what you want to do: 4

Enter the country you want information about: India

The country India has 136 million population

Do you want to end the programme? Enter (yes/no): no

To print the dictionary select 1
To add values to the dictionary select 2
To remove a value from the dictionary select 3
To query about a specific country select 4

Enter what you want to do: 4

Enter the country you want information about: I

The country does not exist in dictionary

Do you want to end the programme? Enter (yes/no): yes
"""
