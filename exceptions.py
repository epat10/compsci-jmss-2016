my_list = [1,2,3,5]

try:
    x = my_list[5]
except IndexError:
    print("Out of Range")

    
notDone = True
while notDone:
    response = input("Do you like people?")
    if response.lower() == "yes":
        print("I like people too.")
        notDone = False
    elif response.lower() == "no":
        print("Oh, ok.")
        notDone = False
    else:
        print("Enter yes or no please!")
