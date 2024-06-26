info=[600,630,620]
ril=[1430,1490,1567]
mtl=[234,180,160]
dic={"info":info,"ril":ril,"mtl":mtl}

def main():
    n="no"
    sum=0
    while n=="no":
        inp=int(input("Enter 1 to print the dictionary\n"
                      "Enter 2 to add elements to the dictionary: "))
        print("")
        while inp != 1 and inp != 2:
            inp = input("Choose correctly!!! Enter (1/2): ")
            print("")
        if inp==1:
            prin()
        elif inp==2:
            add()
        n = input("Do you want to end the programme? Enter (yes/no): ")
        print("")
        while n != "no" and n != "yes":
            n = input("Choose correctly!!! Enter (yes/no): ")
            print("")

def prin():

    for key, value in dic.items():
        sum=0
        for i in range(0,len(value)):
            sum=sum+value[i]
            avg=sum / len(value)
        print(key + " ==> " + str(value) + " ==> " + '{:.2f}'.format(avg))
    print("")

def add():
    inp=input("Enter the stock you want to add a value in: ")
    print("")
    for key,value in dic.items():
        if inp==key:
            val=int(input("Enter the value: "))
            print("")
            value.append(val)
            prin()

    if inp not in dic.keys():
        val = int(input("Enter the value: "))
        print("")
        val1=[val]
        dic.update({inp:val1})
        prin()

if __name__=="__main__":
    main()

"""
Enter 1 to print the dictionary
Enter 2 to add elements to the dictionary: 1

info ==> [600, 630, 620] ==> 616.67
ril ==> [1430, 1490, 1567] ==> 1495.67
mtl ==> [234, 180, 160] ==> 191.33

Do you want to end the programme? Enter (yes/no): no

Enter 1 to print the dictionary
Enter 2 to add elements to the dictionary: 2

Enter the stock you want to add a value in: info

Enter the value: 600

info ==> [600, 630, 620, 600] ==> 612.50
ril ==> [1430, 1490, 1567] ==> 1495.67
mtl ==> [234, 180, 160] ==> 191.33

Do you want to end the programme? Enter (yes/no): no

Enter 1 to print the dictionary
Enter 2 to add elements to the dictionary: 2

Enter the stock you want to add a value in: new

Enter the value: 100

info ==> [600, 630, 620, 600] ==> 612.50
ril ==> [1430, 1490, 1567] ==> 1495.67
mtl ==> [234, 180, 160] ==> 191.33
new ==> [100] ==> 100.00

Do you want to end the programme? Enter (yes/no): yes
"""
