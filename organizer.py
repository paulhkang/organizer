# This will help you make and organize a grocery list.

glist = []

while True:
    add = input("Add item to list, Y or N? ")
    # if add is "Y":
    #     glist.append(input("Please input a thing to add to the list: "))
    # elif add is "N":
    #     break
    # else:
    #     print("Invalid input.")

    match add:
        case "Y" | "y":
            glist.append(input("Please input a thing to add to the list: "))
        case "N" | "n":
            break
        case _:
            print("Invalid input.")


print(glist)

# if add is "Y" or add is "y":
#   do this